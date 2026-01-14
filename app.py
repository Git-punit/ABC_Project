from flask import Flask, jsonify
import pandas as pd
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Academic Bank of Credits System Running"

@app.route("/load_data")
def load_data():
    df = pd.read_csv("data/students.csv")
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO students (name, credits, institution) VALUES (%s, %s, %s)",
            (row['name'], row['credits'], row['institution'])
        )

    conn.commit()
    conn.close()
    return jsonify({"status": "Data Loaded Successfully"})

if __name__ == "__main__":
    app.run(debug=True)
