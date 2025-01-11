from flask import *
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()


@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('page2.html')

@app.route('/about')
def about():
    return render_template('page3.html')

@app.route('/contact')
def contact():
    return render_template('page4.html')


app.run(debug=True)