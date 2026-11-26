import csv
import io
from datetime import datetime
from flask import Flask, render_template, request, Response, redirect, url_for

BATCHES = [
    {"id": "B-001", "mangos": 5, "date_in": "2026-11-20", "days": 3,
     "previous": "1500 g", "current": "1470 g", "loss": "2.0%"},
    {"id": "B-002", "mangos": 5, "date_in": "2026-11-22", "days": 1,
     "previous": "1450 g", "current": "1445 g", "loss": "0.3%"},
]

USERS = [
    {"id": 1, "name": "Juan Dela Cruz", "email": "juan@peltifresh.local", "active": True},
    {"id": 2, "name": "Maria Santos", "email": "maria@peltifresh.local", "active": False},
]

SETTINGS = {
    "temp_min": 10.0,
    "temp_max": 13.0,
    "cool_on": 13.0,
    "cool_off": 10.5,
    "last_saved": "--/--",
}

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

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        SETTINGS["temp_min"] = request.form.get("temp_min", SETTINGS["temp_min"])
        SETTINGS["temp_max"] = request.form.get("temp_max", SETTINGS["temp_max"])
        SETTINGS["cool_on"] = request.form.get("cool_on", SETTINGS["cool_on"])
        SETTINGS["cool_off"] = request.form.get("cool_off", SETTINGS["cool_off"])
        SETTINGS["last_saved"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        return redirect(url_for("admin"))

    return render_template("admin.html", users=USERS, settings=SETTINGS)

@app.route("/admin/reset/<int:user_id>", methods=["POST"])
def admin_reset_user(user_id):
    # Placeholder until SQLite database is connected
    return redirect(url_for("admin"))

@app.route("/admin/delete/<int:user_id>", methods=["POST"])
def admin_delete_user(user_id):
    global USERS
    USERS = [u for u in USERS if u["id"] != user_id]
    return redirect(url_for("admin"))

@app.route("/batches")
def batches():
    q = request.args.get("q", "").strip().lower()
    rows = [b for b in BATCHES if q in b["id"].lower()]
    return render_template(
        "batches.html",
        username="User",
        last_updated="--",
        active="batches",
        batch_list=rows,
        q=q,
    )

@app.route("/batches/export")
def export_csv():
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["Batch ID", "# of Mangos", "Date In", "Days",
                     "Previous Weight", "Current Weight", "Loss %"])
    for b in BATCHES:
        writer.writerow([b["id"], b["mangos"], b["date_in"], b["days"],
                         b["previous"], b["current"], b["loss"]])
    return Response(
        out.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=batches.csv"},
    )

if __name__ == "__main__":
    app.run(debug=True)


