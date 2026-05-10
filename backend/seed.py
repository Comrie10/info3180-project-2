"""
Seed script for DriftDater database.
Run: python seed.py
"""

from app import create_app, db
from app.models import User, Profile, Interest
from datetime import date, datetime

app = create_app()


INTERESTS = [
    'hiking', 'photography', 'gaming', 'cooking', 'travel',
    'music', 'reading', 'fitness', 'art', 'movies',
    'dancing', 'yoga', 'cycling', 'surfing', 'coffee'
]

USERS = [
    {
        'email': 'alice@example.com',
        'username': 'alice_w',
        'password': 'password123',
        'first_name': 'Alice',
        'last_name': 'Wonder',
        'dob': date(1999, 3, 15),
        'gender': 'female',
        'looking_for': 'male',
        'bio': "Love hiking and adventure! Let's explore the world together.",
        'city': 'Kingston',
        'country': 'Jamaica',
        'latitude': 17.9970,
        'longitude': -76.7936,
        'occupation': 'Teacher',
        'education_level': 'bachelor',
        'education': 'UWI',
        'profile_picture': "https://i.pravatar.cc/400?img=1",
        'interests': ['hiking', 'photography', 'travel', 'yoga', 'coffee']
    },
    {
        'email': 'bob@example.com',
        'username': 'bob_builder',
        'password': 'password123',
        'first_name': 'Bob',
        'last_name': 'Builder',
        'dob': date(1997, 7, 22),
        'gender': 'male',
        'looking_for': 'female',
        'bio': "Software developer by day, photographer by night.",
        'city': 'Kingston',
        'country': 'Jamaica',
        'latitude': 17.9970,
        'longitude': -76.7936,
        'occupation': 'Software Developer',
        'education_level': 'master',
        'education': 'UWI Mona',
        'profile_picture': "https://i.pravatar.cc/400?img=2",
        'interests': ['photography', 'gaming', 'hiking', 'cycling', 'coffee']
    },
    {
        'email': 'grace@example.com',
        'username': 'grace_g',
        'password': 'password123',
        'first_name': 'Grace',
        'last_name': 'Gamer',
        'dob': date(2000, 11, 5),
        'gender': 'female',
        'looking_for': 'any',
        'bio': "Gamer and coffee enthusiast. Let's play!",
        'city': 'Montego Bay',
        'country': 'Jamaica',
        'latitude': 18.4762,
        'longitude': -77.8939,
        'occupation': 'Game Designer',
        'education_level': 'bachelor',
        'education': 'UTech',
        'profile_picture': "https://i.pravatar.cc/400?img=3",
        'interests': ['gaming', 'coffee', 'movies', 'music', 'art']
    },
    {
        'email': 'carol@example.com',
        'username': 'carol_cook',
        'password': 'password123',
        'first_name': 'Carol',
        'last_name': 'Cook',
        'dob': date(1998, 6, 18),
        'gender': 'female',
        'looking_for': 'male',
        'bio': "Chef and coffee lover. Looking for someone to cook for!",
        'city': 'Portmore',
        'country': 'Jamaica',
        'latitude': 17.9500,
        'longitude': -76.8833,
        'occupation': 'Chef',
        'education_level': 'other',
        'education': 'Culinary School',
        'profile_picture': "https://i.pravatar.cc/400?img=4",
        'interests': ['cooking', 'travel', 'music', 'fitness', 'dancing']
    },
    {
        'email': 'emma@example.com',
        'username': 'emma_artist',
        'password': 'password123',
        'first_name': 'Emma',
        'last_name': 'Artist',
        'dob': date(2001, 2, 28),
        'gender': 'female',
        'looking_for': 'any',
        'bio': "Artist and creative soul. Let's create art together!",
        'city': 'Spanish Town',
        'country': 'Jamaica',
        'latitude': 17.9916,
        'longitude': -76.9559,
        'occupation': 'Artist',
        'education_level': 'bachelor',
        'education': 'Edna Manley College',
        'profile_picture': "https://i.pravatar.cc/400?img=5",
        'interests': ['art', 'music', 'reading', 'travel', 'photography']
    },
]
def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def seed():
    with app.app_context():
        print("Dropping old tables...")
        db.drop_all()

        print("Creating tables...")
        db.create_all()

        # ------------------------
        # INTERESTS
        # ------------------------
        interest_map = {}

        for name in INTERESTS:
            interest = Interest(name=name)
            db.session.add(interest)
            interest_map[name] = interest

        db.session.commit()
        print(f"Created {len(INTERESTS)} interests")

        # ------------------------
        # USERS + PROFILES
        # ------------------------
        for u in USERS:
            user = User(
                email=u['email'],
                username=u['username']
            )
            user.set_password(u['password'])

            db.session.add(user)
            db.session.flush()

            age = calculate_age(u['dob'])

            profile = Profile(
    user_id=user.id,

    first_name=u['first_name'],
    last_name=u['last_name'],
    age=age,
    date_of_birth=u['dob'],

    gender=u['gender'],
    looking_for=u['looking_for'],
    bio=u['bio'],

    # ✅ ADD THESE (THIS IS WHAT YOU WERE MISSING)
    city=u['city'],
    country=u['country'],
    location=f"{u['city']}, {u['country']}",

    latitude=u['latitude'],
    longitude=u['longitude'],

    occupation=u['occupation'],
    education_level=u['education_level'],
    education=u['education'],

    # ✅ PROFILE PICTURE FIX
    profile_picture=u['profile_picture'],

    is_public=True,

    min_age_preference=18,
    max_age_preference=35,
    max_distance_km=200
)
            for interest_name in u['interests']:
                profile.interests.append(interest_map[interest_name])

            db.session.add(profile)

        db.session.commit()

        print(f"Created {len(USERS)} users with profiles\n")

        print("Test accounts:")
        for u in USERS:
            print(f"Email: {u['email']} | Password: {u['password']}")

        print("\nSeeding complete!")


if __name__ == "__main__":
    seed()