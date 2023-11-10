from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'secret'

# In-memory storage (replace this with a database in a production setting)
storage = {}

@app.route('/recruit/data', methods=['POST'])
def handle_recruit_result():

    data = request.get_json()
    # Store data in the in-memory storage
    storage['recruit_data'] = data   

    return jsonify(data)

@app.route('/recruit/result')
def hello():

    # Retrieve data from the in-memory storage
    data = storage.get('recruit_data', {})
    return jsonify(data)

if __name__ == '__main__':
    # Run the app on the local network, allowing external access
    app.run(host='0.0.0.0', port=5000, debug=True)
