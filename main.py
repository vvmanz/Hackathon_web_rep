from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/api/flights')
def api_flights():
    departure_city = request.args.get('departure_city')
    destination_city = request.args.get('destination_city')
    departure_date_str = request.args.get('departure_date')
    return_date_str = request.args.get('return_date')

    if not departure_date_str or not return_date_str:
        return jsonify({"error": "Отсутствуют даты вылета или прилета"}), 400

    departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d').strftime('%d.%m.%Y')
    return_date = datetime.strptime(return_date_str, '%Y-%m-%d').strftime('%d.%m.%Y')

    conn = sqlite3.connect('AirTickets.db')
    cursor = conn.cursor()

    cursor.execute("""
           SELECT * FROM Flights WHERE Departure_city=? AND Destination_city=? AND Date_departure=? AND Date_destination=?
       """, (departure_city, destination_city, departure_date, return_date))
    flights = cursor.fetchall()

    if not flights:
        cursor.execute("""
               SELECT * FROM Flights WHERE Departure_city=? AND Destination_city=? AND Date_departure=?
           """, (departure_city, destination_city, departure_date))
        flights = cursor.fetchall()
        print(flights)
        response_data = {'flights': flights, 'alternative_results': True}
    else:
        response_data = {'flights': flights, 'alternative_results': False}

    conn.close()
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)