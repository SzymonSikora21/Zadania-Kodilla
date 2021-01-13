import csv
import flask
from flask import render_template, request

app = flask.Flask(__name__)



@app.route("/", method=['GET', 'POST'])
def calculator():
    if request.method == "GET":
        return render_template("currency calculator.html")
    elif request.method == "POST":
        data = request.form
        with open('bank data.csv', mode='r') as bank_data:
            bank_reader = csv.DictReader(bank_data, delimiter=';')
            line_count = 0
            for row in bank_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row['currency']


if __name__ == "__main__":
    app.run()
