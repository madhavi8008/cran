from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the vBBU!"

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    # Simulate processing
    result = {"status": "processed", "data": data}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
