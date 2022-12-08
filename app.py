from flask import Flask, jsonify, Response
import json
from os import system
from http import HTTPStatus

app = Flask(__name__)

#Leer JSONs
with open ('jsons/usuarios.json','r') as archivoJson:
    usuarios = json.load(archivoJson)

with open ('jsons/peliculas.json','r') as archivoJson:
    peliculas = json.load(archivoJson)

with open ('jsons/directores.json','r') as archivoJson:
    directores = json.load(archivoJson)

with open ('jsons/generos.json','r') as archivoJson:
    generos = json.load(archivoJson)

#Rutas API

@app.route("/directores")
def getDirectores():
    return jsonify(directores)

@app.route("/generos")
def getGeneros():
    return jsonify(generos)

@app.route("/peliculas/director/<id>")
def getPeliculasByDirector(id):
    peliculasByDirector = []
    for pelicula in peliculas:
        if pelicula["idDirector"] == id:
            peliculasByDirector.append(pelicula)
    return jsonify(peliculasByDirector)

@app.route("/peliculas/imagen")
def getPeliculasByPortada():
    peliculasByPortada = []
    for pelicula in peliculas:
        if pelicula["imagen"] != '':
            peliculasByPortada.append(pelicula)
    return jsonify(peliculasByPortada)

#ABM peliculas
@app.route("/peliculas")
def getPeliculas():
    return jsonify(peliculas)

@app.route("/peliculas/save/<id>/titulo/<titulo>/ano/<ano>/idDirector/<idDirector>/sinopsis/<sinopsis>", methods=['PUT'])
def savePelicula(id,titulo,ano,idDirector,sinopsis):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            pelicula["titulo"] = titulo
            pelicula["ano"] = ano
            pelicula["idDirector"] = idDirector
            pelicula["sinopsis"] = sinopsis
    with open('jsons/peliculas.json', 'w') as archivoJson:
        json.dump(peliculas, archivoJson, indent=4)
    return jsonify(peliculas)

@app.route("/peliculas/delete/<id>", methods=['DELETE'])
def deletePelicula(id):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            peliculas.remove(pelicula)
            with open('jsons/peliculas.json', 'w') as archivoJson:
                json.dump(peliculas, archivoJson, indent=4)
            return jsonify(peliculas)

@app.route("/peliculas/<id>")
def getPeliculaByCodigo(id):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            return jsonify(pelicula)
    return Response("{}", status=HTTPStatus.NOT_FOUND)

#Programa
def MenuBienvenida():
    opcion = 0
    while not(opcion>=1 and opcion<=3):
        system("cls")
        print('=====================')
        print('Bienvenido:')
        print('1) Iniciar sesion')
        print('2) Ingresar como invitado')
        print('3) Para salir')
        print('=====================')
        opcion = int(input('Ingresar opcion: '))
    return opcion

def opcionIniciarSesion():
    system("cls")
    inicioExitoso = False
    while True:
        print('=====================')
        usuarioIngresado = input('Ingrese su usuario: ').lower()
        contrasenaIngresada =  input('Ingrese su contrasena: ').lower()
        print('=====================')
        for usuario in usuarios:
            if usuario["usuario"] == usuarioIngresado and usuario["contrasena"] == contrasenaIngresada:
                input('Logeo exitoso!! Enter para continuar!')
                inicioExitoso = True
        if inicioExitoso:
            break

def menuUsuario():
    opcion = 0
    while not(opcion>=1 and opcion<=5):
        system("cls")
        print('=====================')
        print('1) Ver ultimas 10 peliculas agregadas')
        print('2) Agregar pelicula')
        print('3) Modificar pelicula')
        print('4) Borrar pelicula')
        print('5) Buscar pelicula por ID o titulo')
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

def ultimasDiezPeliculas():
    contador = 0
    system("cls")
    for pelicula in reversed(peliculas):
        contador = contador + 1
        print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, el director fue {directores[int(pelicula["idDirector"])-1]["nombre"]}, ', end='')
        print('tiene los generos ', end="")
        for generoPelis in pelicula["idGeneros"]:
            for genero in generos:
                if genero["id"] == generoPelis:
                    print(genero["nombre"].lower(),', ', end="")
        print('La sinopsis es:', pelicula["sinopsis"])
        if contador == 10:
            break
    input('Ingrese enter para continuar...')

def borrarPelicula():
    system("cls")
    print('=====================')
    borrar = input('Ingrese el id o el nombre de la pelicula que desea borrar: ')
    print('=====================')
    for pelicula in peliculas:
        if pelicula["id"] == borrar or pelicula["titulo"].lower() == borrar:
            peliculas.remove(pelicula)
            encontrada = True
    if encontrada == False:
        print('No se pudo borrar porque no existe')
    print('Borrado exitoso')
    with open('jsons/peliculas.json', 'w') as archivoJson:
        json.dump(peliculas, archivoJson, indent=4)
    input('Ingrese enter para continuar...')

def getPeliculaByCodigo():
    system("cls")
    encontrada = False
    buscar = input('Ingrese la id o titulo: ')
    for pelicula in peliculas:
        if pelicula["id"] == buscar or pelicula["titulo"].lower() == buscar:
            print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, el director fue {directores[int(pelicula["idDirector"])-1]["nombre"]}, ', end='')
            print('tiene los generos ', end="")
            for generoPelis in pelicula["idGeneros"]:
                for genero in generos:
                    if genero["id"] == generoPelis:
                        print(genero["nombre"].lower(),', ', end="")
            print('La sinopsis es:', pelicula["sinopsis"])
            encontrada = True
    if encontrada == False:
        print('No fue encontradada')
    input('Ingrese enter para continuar...')

def main():
    opcionMenuBienvennida = 0
    while opcionMenuBienvennida != 3:
        opcionMenuBienvennida = MenuBienvenida()
        #Inicio sesion
        if opcionMenuBienvennida == 1:
            opcionIniciarSesion()
            opcion = menuUsuario()
            if opcion == 1:
                ultimasDiezPeliculas()
            if opcion == 4:
                borrarPelicula()
            if opcion == 5:
                getPeliculaByCodigo()
        #Invitado
        if opcionMenuBienvennida == 2:
                ultimasDiezPeliculas()

main()