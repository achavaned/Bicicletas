from flask import Flask
import folium
import db

app = Flask(__name__)
'''
@app.route('/map', methods=['GET'])
def mapa():
    # Procesar los datos para crear el mapa
    # Crear el mapa utilizando Folium
    m = folium.Map(location=[6.235925, -75.575136111111], zoom_start=13, width=500, height=500)

    # Crear marcadores en el mapa utilizando los datos
    folium.Marker([6.235925, -75.575136111111], popup='Medellin, ANT').add_to(m)

    # Renderizar el mapa en una plantilla HTML utilizando Flask
    #render_template('mapa.html', map=m._repr_html_())
    map=m._repr_html_()
    return map
'''
@app.route('/map', methods=['GET'])
def selected():
    m = folium.Map(location=[6.235925, -75.575136111111], zoom_start=13, height=500)
    bikes = list(db.db.selection.find())
    if bikes:
        for bike in bikes:
            latitud = bike['ubicacion']['latitud']
            longitud = bike['ubicacion']['longitud']
            modelo = bike['model']
            color = bike['color']
            popup = f'{modelo} - {color}'
            folium.Marker([longitud, latitud], popup=popup).add_to(m)
    m.fit_bounds(m.get_bounds())
    map=m._repr_html_()
    return map

if __name__ == '__main__':
    app.run(port=8002)
    
#docker build -t Map .
#docker run -p 8002:8002 Map