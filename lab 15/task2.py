from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid input or missing JSON data"}), 400
    
    items.append(data)
    
    return jsonify({"message": "Item added successfully", "item": data}), 201

if __name__ == '__main__':
    app.run(debug=True)