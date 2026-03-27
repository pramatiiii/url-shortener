from flask import Flask, render_template, request, redirect, abort
from database import init_db, save_url, get_url

app = Flask(__name__)

# Initialize the database when the app starts
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None

    if request.method == "POST":
        original_url = request.form.get("url")

        # Basic validation
        if not original_url.startswith("http"):
            original_url = "https://" + original_url

        code = save_url(original_url)
        short_url = request.host_url + code

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_url(short_code):
    original_url = get_url(short_code)

    if original_url is None:
        abort(404)  # Show a 404 if the code doesn't exist

    return redirect(original_url)


if __name__ == "__main__":
    app.run(debug=True)