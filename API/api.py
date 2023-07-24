from flask import Flask, jsonify
import json
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
@app.route('/api/user/<string:column_name>', methods=['GET'])
def get_user(column_name):
    conn = sqlite3.connect("E:\\MDA\\Beta Testing\\Scripting\\native_app_db\\ug_design.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM parameters WHERE user_name=?", (column_name,))
    data = cursor.fetchall()

    conn.close()

    if data:
        # Create a list to store all rows as dictionaries
        data_list = []

        # Convert each tuple to a dictionary
        for row in data:
            data_dict = {
                "name": row[0],
                "parameters": json.loads(row[1]),  # Convert JSON string to dictionary
                "mod_date": row[2]
            }
            data_list.append(data_dict)

        # Return the data as JSON
        return jsonify(data_list[0])
    else:
        # If not, return a message indicating user not found
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
