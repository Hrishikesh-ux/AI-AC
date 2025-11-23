from flask import Flask, jsonify, request

app = Flask(__name__)

items = [{"name": "Initial Item 1", "price": 10}, {"name": "Initial Item 2", "price": 20}]


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to AI-assisted API"})


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


@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if index < 0 or index >= len(items):
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input or missing JSON data"}), 400

    items[index] = data
    
    return jsonify({"message": "Item updated", "item": data})


@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < 0 or index >= len(items):
        return jsonify({"error": "Item not found"}), 404
        
    removed_item = items.pop(index)
    
    return jsonify({"message": "Item deleted", "item": removed_item})


if __name__ == '__main__':
    app.run(debug=True)