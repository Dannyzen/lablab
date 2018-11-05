from flask import Flask, jsonify, request
import requests 

app = Flask(__name__)
@app.route('/calcPrice', methods=['POST'])
def calcPrice():
    # If there's no items in the json we receive...
    if not request.json or not 'items' in request.json:
        abort(400)
    # If what we receive has items but it's not a list
    if not type(request.json['items']) is list:
        abort(400)
    # If we get items that aren't a service and thus we reach out and do not get a 200...
    total_price = 0
    for item in request.json['items']:
        r = requests.get('http://' + item + '.svc/' + item)
        if r.status_code is not 200:
            abort(500)
        total_price += r.json['cost']
    return jsonify({'total_price':total_price})

if __name__ == '__main__':
    app.run()
