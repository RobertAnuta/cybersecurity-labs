from werkzeug.security import generate_password_hash
from app import app
from models import db, User, Module

with app.app_context():
    db.create_all()

    if not User.query.filter_by(username="testuser").first():
        test_user = User(
            username="testuser",
            password_hash=generate_password_hash("Test1234"),
            role="employee",
        )
        db.session.add(test_user)

    if not Module.query.filter_by(title="Phishing & Social Engineering Defense").first():
        module_1 = Module(
            title="Phishing & Social Engineering Defense",
            compliance_mapping="NIST PR.AT-1, ISO A.6.3",
        )
        db.session.add(module_1)

    db.session.commit()
    print("Database seeded. Test login: testuser / Test1234")
