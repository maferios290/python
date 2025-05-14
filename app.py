#se importan las librerias a usar en el proyecto

import request
import configparser

#habilita las capacidades de servidor en la aplicacion, es la libreria encargada de gestionar la renderizacion de las vistas
from flask import Flask, render_template, request # type. ignore

#el objeto principal de la aplicacion se llama app
app=FLask(_name_)



#iniciamos con la logica de la aplicacion

#se  gestiona la ruta inicial de la aplicacion
#ruta principal
@app.route ('/')

#aqui va el nombre de la funcion o metodo que gestiona la ruta
def weather_dashboard():
    return render_template ('home.html')


#ruta que pinta los resultados
@app.route ('/results')
def render_resultados 

#para poder mostrar los resultados antes debo saber cual es la ciudad que digito en el formulario
    cityname= request.form['cityName']

    #es pasarle el valor de la ciudad que el usuario digito al api

    #esta variable esta lamcenando el valor de api key que se encuentra en el archivo config.ini
    api= get_api_key();

    #vamos a conectarnos al api y cpnsumirlo
    data = get_wather_results(cityname, api)
    #se toma lña temperatura del json
    temp = "{0:.2f}"format (data['main']['temp'])


def get_wather_results(cityname, apy_key)
    
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname,appi_key)

    r = request.get(url)
    return r.json
    
    


def get_api_key():

    #esta funcion obtiene el valor del api key que se va
    #a utilizar para consumir el servicio web

    #se lee el archivo que guarda la api key del servicio web
    config = configparser.configparser()
    config.read('config.ini')
    return config ['openweathermap']['api']




#esta condicion siempre va en los proyectos de python
#e indica que por defecto el metodo principal 

if _name_ =="_main_":
app.run(debug=True)