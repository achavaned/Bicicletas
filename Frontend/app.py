from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapa')
def get_map():
    response = requests.get('http://127.0.0.1:8002/map')
    map = (response.content).decode('UTF-8')
    index = render_template('index.html')
    return f"{index}\n{map}"

@app.route('/bicicletas', methods=['GET'])
def get_bikes():
    response = requests.get('http://127.0.0.1:8000/bicicletas/api')
    json_data = response.json()
    bikes = list(json_data.get('data'))
    return render_template('bikes.html', bikes=bikes)

@app.route('/create', methods=['GET'])
def create_bike_form():
    return render_template('create.html')

@app.route('/bicicletas/crear', methods=['POST'])
def create_bike():
    data = {
        'model': request.form['model'],
        'color': request.form['color'],
        'ubicacion': {
            'longitud': request.form['longitud'],
            'latitud': request.form['latitud']
        }
    }
    url = 'http://localhost:8000/bicicletas/api/create'
    response = requests.post(url, json=data)
    return redirect(url_for('index'))

@app.route('/bicicletas/update/<id>', methods=['GET'])
def update_bike_form(id):
    response = requests.get(f'http://127.0.0.1:8000/bicicletas/api/{id}')
    json_data = response.json()
    bike = json_data.get('data')
    bike.update({'_id': id})
    return render_template('update.html', bike=bike)

@app.route('/bicicletas/updated/<id>', methods=['GET'])
def update_bike(id):
    data = {
        'model': request.args.get('model'),
        'color': request.args.get('color'),
        'ubicacion.longitud': request.args.get('longitud'),
        'ubicacion.latitud': request.args.get('latitud')
    }
    url = f'http://localhost:8000/bicicletas/api/update/{id}'
    response = requests.put(url, json=data)
    return redirect(url_for('index'))

@app.route('/bicicletas/delete/<id>', methods=['GET'])
def delete_bike(id):
    url = f'http://localhost:8000/bicicletas/api/delete/{id}'
    response = requests.delete(url)
    return redirect(url_for('index'))

@app.route('/bicicletas/select/<id>', methods=['GET'])
def select_bike(id):
    url = f'http://localhost:8000/bicicletas/api/select/{id}'
    response = requests.post(url)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8001)
    
#docker build -t Frontend .
#docker run -p 8001:8001 Frontend