from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/beer")
def beer():
    return jsonify({'cost':8})

if __name__ == '__main__':
    app.run(debug=True)
