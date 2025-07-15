from flask import Flask, request, jsonify
from mcp import get_clients_data

app = Flask(__name__)

@app.route('/mcp/clients', methods=['GET'])
def mcp_clients():
    data, status = get_clients_data()
    return jsonify(data), status

if __name__ == '__main__':
    app.run(debug=True)
