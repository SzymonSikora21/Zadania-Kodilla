import flask

from flask import render_template

app = flask.Flask(__name__)


@app.route('/mypage/me')
def me():
    return render_template("me.html")


@app.route('/mypage/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
