from flask import Flask
from flask import render_template
import sqlite3 as sql
from flask import g
from flask import request
import datetime
from flask import jsonify

DATABASE = 'database.db'

app = Flask(__name__)


# Humidity, pressure, temperature, timestamp
def insert_data(data_dict):
    db = sql.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("INSERT INTO sensors (humidity, barometric_pressure, temperature, time_stamp) VALUES (?, ?, ?, ?)", (data_dict['humidity'], data_dict['barometric_pressure'], data_dict['temperature'], datetime.datetime.now().__str__()))
    db.commit()
    db.close()


# Returns all saved data
def get_all_data():
    db = sql.connect(DATABASE)
    cursor = db.cursor()
    data_key = ['id', 'humidity', 'pressure', 'temperature', 'time_stamp']
    data = []
    for row in cursor.execute('select * from sensors'):
        id, hum, pre, temp, timestmp = row
        data.append({
            id: {
                'humidity' : hum,
                'pressure' : pre,
                'temperature' : temp,
                'timestamp' : timestmp
            }
        })

    # data = [row for row in cursor.execute('select * from sensors')]
    return data

# Only returns latest data
def get_latest_data():
    db = sql.connect(DATABASE)
    cursor = db.cursor()
    return cursor.execute('select * from sensors').fetchone()

@app.route('/api/clear_data', methods=['GET'])
def clear_all():
    db = sql.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('delete from sensors')
    db.commit()
    return jsonify({'success' : 'cleared all'})


@app.route('/api/insert_data', methods=['GET'])
def api_insert_data():
    humidity = request.args.get('h', '0')
    temperature = request.args.get('t', '0')
    pressure = request.args.get('p', '0')

    data_dict = {
        'humidity' : float(humidity),
        'barometric_pressure' : float(pressure),
        'temperature' : float(temperature)
    }

    insert_data(data_dict)

    return jsonify({'success' : 'ok'})


@app.route('/api/get_data', methods=['GET'])
def api_get_data():
    return jsonify({
       'all_data' : get_all_data()
    })

@app.route('/api/data', methods=['GET'])
def api_get_latest_data():
    try:
        return jsonify({
            'latest' : get_all_data()[-1]
        })
    except:
        return jsonify({
            'error' : 'NO data available'
        })

@app.route('/')
def index():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)