from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
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
    # GET: show the module content and the practice exercise
    # POST: score the exercise and save a Completion record
    pass


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)