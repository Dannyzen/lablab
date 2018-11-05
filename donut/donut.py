from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/donut")
def donut():
    return jsonify({'cost':5})

if __name__ == '__main__':
    app.run(debug=True)
