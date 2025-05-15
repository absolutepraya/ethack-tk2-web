from flask import (
    Flask,
    request,
    render_template,
    render_template_string,
    redirect,
    url_for,
)
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = os.urandom(24)

FLAG = "Part 1: ETHACK{es_es_ti_"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        name = request.form.get("name", "")
        if "." in name:
            return (
                render_template_string(
                    "<h1>Invalid input: the dot character is not allowed.</h1>"
                ),
                400,
            )
        snippet = f"""<div class="message">
    <h2>Hello, {name}!</h2>
    <p>Thank you for visiting our website.</p>
</div>"""
        full_template = f"""<!DOCTYPE html>
<html>
<head>
    <title>Your Message - SSTI Challenge</title>
    <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
</head>
<body>
    <div class="container">
        <h1>Your Message</h1>
        {snippet}
        <div class="footer">
            <a href="{url_for('index')}">Back to Home</a> |
            <a href="{url_for('message')}">Send Another Message</a>
        </div>
    </div>
</body>
</html>"""
        return render_template_string(full_template)
    return render_template("message_form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
