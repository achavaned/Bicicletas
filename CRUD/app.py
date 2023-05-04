from flask import Flask, jsonify, request, render_template, redirect, url_for
from bson import json_util, ObjectId
import json
import db

app = Flask(__name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/')
def index():
    documents = list(db.db.collection.find())
    return render_template('index.html', documents=documents)

#test to insert data to the data base
@app.route("/test")
def test():
    db.db.collection.insert_one({
        "model": "BMX007",
        "color": "Negro",
        "ubicacion": {
            "longitud": 10000,
            "latitud": 100001
        },

    })
    return "Connected to the data base!"

# Define CRUD operations
@app.route('/bicicletas', methods=['GET'])
def get_bikes():
    bikes = list(db.db.collection.find())
    return render_template('bikes.html', bikes=bikes)
'''
@app.route('/documents', methods=['POST'])
def create_document():
    document = request.get_json()
    result = db.db.collection.insert_one(document)
    return jsonify({'id': str(result.inserted_id)})
'''
@app.route('/bicicletas/api', methods=['GET'])
def get_bikes_api():
    bikes = list(db.db.collection.find())
    return jsonify({'data': parse_json(bikes)})

@app.route('/bicicletas/api/<id>', methods=['GET'])
def get_bike(id):
    document = db.db.collection.find_one({'_id': ObjectId(id)})
    return jsonify({'data': parse_json(document)})

@app.route('/create', methods=['GET'])
def create_bike_form():
    return render_template('create.html')

@app.route('/bicicletas/crear', methods=['POST'])
def create_bike():
    document = {
        'model': request.form['model'],
        'color': request.form['color'],
        'ubicacion': {
            'longitud': request.form['longitud'],
            'latitud': request.form['latitud']
        }
    }
    result = db.db.collection.insert_one(document)
    return redirect(url_for('index'))

@app.route('/bicicletas/update/<id>', methods=['GET'])
def update_bike_form(id):
    bike = db.db.collection.find_one({'_id': ObjectId(id)})
    return render_template('update.html', bike=bike)

@app.route('/bicicletas/<id>', methods=['GET'])
def update_bike(id):
    #data = request.get_json()
    #data['_id'] = ObjectId(id)
    data = {
        'model': request.args.get('model'),
        'color': request.args.get('color'),
        'ubicacion.longitud': request.args.get('longitud'),
        'ubicacion.latitud': request.args.get('latitud')
    }
    result = db.db.collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return redirect(url_for('index'))

@app.route('/bicicletas/<id>', methods=['DELETE'])
def delete_bike(id):
    result = db.db.collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'deleted_count': result.deleted_count})

if __name__ == '__main__':
    app.run(port=8000)