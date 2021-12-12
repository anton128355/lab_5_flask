from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_car(car_id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM cars WHERE id = ?',
                       (car_id,)).fetchone()
    conn.close()
    if car is None:
        abort(404)
    return car


@app.route('/')
def main_page():  # put application's code here
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return render_template('index.html', cars=cars)


@app.route('/about_page')
def about_page():  # put application's code here
    return render_template('about.html')


@app.route('/consultation_<int:car_id>')
def car(car_id):
    car = get_car(car_id)
    return render_template('consultation.html', post=car)


if __name__ == '__main__':
    app.run()
