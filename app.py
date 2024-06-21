from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    number = data['number']
    result = number * 10
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)