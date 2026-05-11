from flask import Blueprint, jsonify, request, session
from app import db, bcrypt
from app.models import User, Profile, Interest, Message
from haversine import haversine
from app.forms import Register, Login, Profile
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required, logout_user


bp = Blueprint("bp", __name__)


# --------------------
# HEALTH CHECK
# --------------------
@bp.route("/")
def index():
    return jsonify(message="DriftDater API running")

@bp.before_request
def handle_options():
    if request.method == "OPTIONS":
        return '', 200


# --------------------
# REGISTER
# --------------------
@bp.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON"}), 400

    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409

    user = User(email=email, username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


# --------------------
# LOGIN
# --------------------
@bp.route("/auth/login", methods=["POST", "OPTIONS"])
def login():
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    session["user_id"] = user.id

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username
        },
        
    })


@bp.route("/auth/me", methods=["GET"])
def me():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"user": None}), 401

    user = User.query.get(user_id)
    profile = Profile.query.filter_by(user_id=user_id).first()

    return jsonify({
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username
        },
        "profile": {
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "city": profile.city,
            "country": profile.country,
            "bio": profile.bio,
            "profile_picture": profile.profile_picture
        }
    })
# --------------------
# LOGOUT
# --------------------
@bp.route("/auth/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    return jsonify({"message": "logged out"})


# --------------------
# PROFILES (REAL DATA)
# --------------------
@bp.route("/profiles", methods=["GET"])
@login_required
def profiles():
    profiles = Profile.query.all()

    result = []

    for p in profiles:
        result.append({
            "id": p.id,
            "user_id": p.user_id,

            # BASIC INFO
            "first_name": p.first_name,
            "last_name": p.last_name,
            "age": p.age,
            "gender": p.gender,
            "looking_for": p.looking_for,
            "bio": p.bio,

            # LOCATION
            "location": p.location,
            "city": p.city,
            "country": p.country,
            "latitude": p.latitude,
            "longitude": p.longitude,

            # EXTRA INFO
            "education_level": p.education_level,
            "education": p.education,
            "occupation": p.occupation,

            # SETTINGS
            "is_public": p.is_public,
            "min_age_preference": p.min_age_preference,
            "max_age_preference": p.max_age_preference,
            "max_distance_km": p.max_distance_km,

            # IMAGE
            "profile_picture": p.profile_picture,

            # INTERESTS
            "interests": [i.name for i in p.interests],

            # OPTIONAL (useful for frontend)
            "created_at": p.created_at,
            "updated_at": p.updated_at
        })

    return jsonify(result)

@bp.route("/profile/update", methods=["PUT"])
@login_required
def update_profile():
    user_id = session.get("user_id")

    profile = Profile.query.filter_by(user_id=user_id).first()

    data = request.json

    profile.first_name = data["first_name"]
    profile.last_name = data["last_name"]
    profile.bio = data["bio"]
    profile.city = data["city"]
    profile.country = data["country"]
    profile.occupation = data["occupation"]
    profile.age = data["age"]
    profile.looking_for = data["looking_for"]
    profile.profile_picture = data["profile_picture"]

    db.session.commit()

    return jsonify({"profile": {
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "bio": profile.bio,
        "city": profile.city,
        "country": profile.country,
        "profile_picture": profile.profile_picture
    }})

# --------------------
# MATCHES (placeholder for now but safe)
# --------------------
@bp.route("/matches", methods=["GET"])
@login_required
def matches():
    user_id = session.get("user_id")
    user_profile = Profile.query.filter_by(user_id=user_id).first()
    user_coordinates = (user_profile.latitude, user_profile.longitude)
    max_distance = user_profile.max_distance

    matches = []
    for m in Profile.query.all():
        if m.user_id == user_id:
            continue  

        other_coordinates = (m.latitude, m.longitude)
        if None in user_coordinates or None in other_coordinates:
            continue

        distance = haversine(user_coordinates, other_coordinates)

        if distance <= max_distance:
            matches.append({
                "id": m.id,
                "first_name": m.first_name,
                "last_name": m.last_name,
                "age": m.age,})
    return jsonify(matches)


# --------------------
# MESSAGES
# --------------------
@bp.route("/messages", methods=["GET"])
@login_required
def messages():
    user_id = session.get("user_id")
    message = Message.query.filter(
        (Message.sender_id == user_id) | (Message.receiver_id == user_id)
    ).order_by(Message.timestamp.desc()).all()
    return jsonify([m.to_dict() for m in message])

@bp.route("/messages/send", methods=["POST"])
@login_required
def send_message():
    user_id = session.get("user_id")
    data = request.json

    new_message = Message(
        sender_id=user_id,
        receiver_id=data["receiver_id"],
        content=data["content"]
    )

    db.session.add(new_message)
    db.session.commit()

    return jsonify({"message": "Message sent successfully"}, 201)