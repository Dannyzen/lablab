from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/shoes")
def shoes():
    return jsonify({'cost':85})

if __name__ == '__main__':
    app.run(debug=True)
