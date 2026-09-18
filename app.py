from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# the page is fully self-contained, so the only thing that changes is the assets
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 60 * 60 * 24


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/robots.txt")
@app.route("/sitemap.xml")
def crawler_files():
    # crawlers expect these at the root, not under /static
    return send_from_directory(app.static_folder, request.path.lstrip("/"))


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5050)
