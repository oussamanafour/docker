from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, IFIAG DevOps Students!'

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

# Uniquement pour le dev local
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)