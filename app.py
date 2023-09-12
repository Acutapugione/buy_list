from flask import Flask
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

with sqlite3.connect('my_db.db') as connect:
    connect.execute(
    "CREATE TABLE IF NOT EXISTS PARTICIPANTS(\
       name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)"
    )

from routes import *

if __name__ == '__main__':
    app.run(debug=True)