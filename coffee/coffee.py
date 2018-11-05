from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/coffee")
def coffee():
    return jsonify({'cost':5.5})

if __name__ == '__main__':
    app.run(debug=True)
