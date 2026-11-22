from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def select_login():
    return render_template("select_login.html")

@app.route("/login/admin", methods=["GET", "POST"])
def login_admin():
    if request.method == "POST":
        pass  # real login check comes later
    return render_template("login.html", role="admin")

@app.route("/login/user", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        pass  # real login check comes later
    return render_template("login.html", role="user")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pass  # saving the account to the database comes later
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        username="User",
        last_updated="--",
        door_open=False,
        temp="--", temp_min=10, temp_max=13, temp_status="--",
        batches=[
            {"name": "Batch 1", "present": True},
            {"name": "Batch 2", "present": True},
            {"name": "Batch 3", "present": False},
            {"name": "Batch 4", "present": True},
        ],
        log=[],
    )

@app.route("/batches")
def batches():
    return "Batches page (coming next)"

if __name__ == "__main__":
    app.run(debug=True)