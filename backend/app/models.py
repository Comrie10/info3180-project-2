from datetime import datetime
from app import db
from flask_bcrypt import Bcrypt
from app import bcrypt


# =========================
# ASSOCIATION TABLE
# =========================
profile_interests = db.Table(
    "profile_interests",
    db.Column("profile_id", db.Integer, db.ForeignKey("profiles.id"), primary_key=True),
    db.Column("interest_id", db.Integer, db.ForeignKey("interests.id"), primary_key=True),
)


# =========================
# USER MODEL
# =========================
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)

    password_hash = db.Column(db.String(255), nullable=False)

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships
    profile = db.relationship('Profile', backref='user', uselist=False, cascade='all, delete-orphan')

    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy='dynamic')
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy='dynamic')

    likes_given = db.relationship('Like', foreign_keys='Like.liker_id', backref='liker', lazy='dynamic')
    likes_received = db.relationship('Like', foreign_keys='Like.liked_id', backref='liked', lazy='dynamic')

    favourites = db.relationship('Favorite', foreign_keys='Favorite.user_id', backref='user', lazy='dynamic')

    # password helpers
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


# =========================
# PROFILE MODEL
# =========================
class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True, index=True)

    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    looking_for = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.Text, nullable=False)

    location = db.Column(db.String(120), nullable=False)

    date_of_birth = db.Column(db.Date, nullable=True)

    city = db.Column(db.String(120))
    country = db.Column(db.String(120))

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    education_level = db.Column(db.String(120))
    is_public = db.Column(db.Boolean, default=True)

    min_age_preference = db.Column(db.Integer, default=18)
    max_age_preference = db.Column(db.Integer, default=99)
    max_distance_km = db.Column(db.Integer, default=100)

    occupation = db.Column(db.String(120), default="")
    education = db.Column(db.String(120), default="")

    profile_picture = db.Column(db.String(255), default="")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    interests = db.relationship(
        "Interest",
        secondary=profile_interests,
        backref=db.backref("profiles", lazy="dynamic"),
    )


# =========================
# INTEREST
# =========================
class Interest(db.Model):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)


# =========================
# LIKE
# =========================
class Like(db.Model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)

    liker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    liked_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    action = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("liker_id", "liked_id", name="unique_like_action"),
    )


# =========================
# MATCH
# =========================
class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)

    user1_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    user2_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("user1_id", "user2_id", name="unique_match"),
    )


# =========================
# MESSAGE
# =========================
class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)

    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"), nullable=False, index=True)

    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    body = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)


# =========================
# FAVORITE
# =========================
class Favorite(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False, index=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("user_id", "profile_id", name="unique_favorite"),
    )