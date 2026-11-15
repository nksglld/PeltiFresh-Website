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

@app.route("/register")
def register():
    return "Sign-up page (coming next)"

if __name__ == "__main__":
    app.run(debug=True)