from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (Example initialization)
# NOTE: In a real app, this list would be shared/imported, 
# but we include it here for the file to be runnable.
items = [{"name": "Initial Item 1", "price": 10}, {"name": "Initial Item 2", "price": 20}]


# ===============================================
# Task 4: Delete Item (DELETE)
# ===============================================
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    # Check for invalid index (out of bounds)
    if index < 0 or index >= len(items):
        return jsonify({"error": "Item not found"}), 404
        
    # Remove the item at the specified index and store it
    removed_item = items.pop(index)
    
    # Return a success response
    return jsonify({"message": "Item deleted", "item": removed_item})


# Add necessary run block for testing
if __name__ == '__main__':
    print("Running Delete Endpoint (Task 4)...")
    print(f"Current items: {items}")
    app.run(debug=True)