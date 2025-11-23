from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (Example initialization)
# NOTE: In a real app, this list would be shared/imported, 
# but we include it here for the file to be runnable.
items = [{"name": "Initial Item 1", "price": 10}, {"name": "Initial Item 2", "price": 20}]


# ===============================================
# Task 3: Update Item (PUT)
# ===============================================
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    # Check for invalid index (out of bounds)
    if index < 0 or index >= len(items):
        return jsonify({"error": "Item not found"}), 404
    
    # Get the JSON data from the request body
    data = request.get_json()

    # Basic input validation
    if not data:
        return jsonify({"error": "Invalid input or missing JSON data"}), 400

    # Update the item at the specified index
    items[index] = data
    
    # Return a success response
    return jsonify({"message": "Item updated", "item": data})


# Add necessary run block for testing
if __name__ == '__main__':
    print("Running Update Endpoint (Task 3)...")
    print(f"Current items: {items}")
    app.run(debug=True)