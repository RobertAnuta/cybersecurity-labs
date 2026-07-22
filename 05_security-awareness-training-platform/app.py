from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from datetime import datetime
from models import db, User, Module, Completion

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-in-a-real-deployment"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///training.db"

db.init_app(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return render_template("login.html", error="Username and password are required")

        if len(username) > 80 or len(password) > 255:
            return render_template("login.html", error="Invalid username or password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["role"] = user.role
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    modules = Module.query.all()
    user_completions = Completion.query.filter_by(user_id=session["user_id"]).all()
    completed_module_ids = {c.module_id for c in user_completions}

    return render_template(
        "dashboard.html",
        modules=modules,
        completed_module_ids=completed_module_ids,
    )


@app.route("/module/<int:module_id>", methods=["GET", "POST"])
def module_page(module_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    module = Module.query.get_or_404(module_id)
    result = None

    if request.method == "POST":
        correct_answers = {"q1": "b", "q2": "true", "q3": "report"}
        submitted_answers = {
            "q1": request.form.get("q1"),
            "q2": request.form.get("q2"),
            "q3": request.form.get("q3"),
        }

        score = sum(
            1 for key, value in correct_answers.items()
            if submitted_answers.get(key) == value
        )
        passed = score >= 2

        completion = Completion.query.filter_by(
            user_id=session["user_id"], module_id=module_id
        ).first()

        if completion:
            completion.score = score
            completion.passed = passed
            completion.completed_at = datetime.utcnow()
        else:
            completion = Completion(
                user_id=session["user_id"],
                module_id=module_id,
                score=score,
                passed=passed,
            )
            db.session.add(completion)

        db.session.commit()
        result = {"score": score, "total": 3, "passed": passed}

    return render_template("module.html", module=module, result=result)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
