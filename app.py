from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/admin', methods=['POST'])
def chat():
    