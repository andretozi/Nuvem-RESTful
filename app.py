from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 10436460, "name": "Andre Tozi"}
]

# 1. Get all items
@app.route("/", methods=["GET"])
def get_items():
    return jsonify({"items": items})

# 2. Get a specific item
@app.route("/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify({"item": item})
    return jsonify({"error": "Item not found"}), 404

# 3. Create a new item
@app.route("/", methods=["POST"])
def create_item():
    new_item = {
        "id": len(items) + 1,
        "name": request.json["name"]
    }
    items.append(new_item)
    return jsonify({"item": new_item}), 201

# 4. Update an existing item
@app.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        item["name"] = request.json["name"]
        return jsonify({"item": item})
    return jsonify({"error": "Item not found"}), 404

# 5. Delete an item
@app.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(debug=True)