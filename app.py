from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def route_highlight_delete():
    return render_template("textbook.html")


if __name__ == '__main__':
    app.run()
