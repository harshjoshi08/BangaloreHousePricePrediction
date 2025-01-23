from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('cleaned_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locations')
def get_locations():
    locations = sorted(data['location'].dropna().unique())
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

