### Put and Delete - HTTP Verbs
### Working with APIs - JSON    

from flask import Flask, jsonify, request   

app = Flask(__name__)

## Initial data in TO-DO list
items=[
    {'id':1, 'name':'Item 1', 'description':'This is Item 1'},
    {'id':2, 'name':'Item 2', 'description':'This is Item 2'},
]

@app.route('/')
def home():
    return "Welcome to the todo list app"


## Get: Retrieve all the items
@app.route('/items', methods=["GET"])
def get_items():
    return jsonify(items) #return all the elements in json format

## Get: Retrieve a specific item by id
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in items if item['id']==id), None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

## Post: Create a new task - API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json: #If data is not in json format or name variable is not there in json
        return jsonify({'error':'Item not found'})
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)


## Put: Update an existing item
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({'error':'Item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

## Delete: Delete an item
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item["id"]!=id]
    return jsonify({'result':'Item deleted'})

    

if __name__ == '__main__':
    app.run(debug=True)
