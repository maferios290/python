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

    api= get_api_key();


def get_api_key():

    #esta funcion obtiene el valor del api key que se va
    #a utilizar para consumir el servicio web

    config = configparser.configparser()




#esta condicion siempre va en los proyectos de python
#e indica que por defecto el metodo principal 
if _name_ =="_main_":
app.run(debug=True)