from project import db
from project.models import User, Items
from datetime import datetime

def seed_data():
    # Create sample users
    user1 = User(
        email="user1@example.com",
        password="password1",
        authenticated=True,
        email_confirmation_sent_on=datetime.now(),
        email_confirmed=True,
        email_confirmed_on=datetime.now(),
        registered_on=datetime.now(),
        last_logged_in=None,
        current_logged_in=datetime.now(),
        role="user"
    )
    
    user2 = User(
        email="admin@example.com",
        password="adminpassword",
        authenticated=True,
        email_confirmation_sent_on=datetime.now(),
        email_confirmed=True,
        email_confirmed_on=datetime.now(),
        registered_on=datetime.now(),
        last_logged_in=None,
        current_logged_in=datetime.now(),
        role="admin"
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Create sample items
    item1 = Items(name="Item 1", notes="This is item 1", user_id=user1.id)
    item2 = Items(name="Item 2", notes="This is item 2", user_id=user2.id)

    db.session.add(item1)
    db.session.add(item2)
    
    db.session.commit()

    print("Database seeded successfully.")
