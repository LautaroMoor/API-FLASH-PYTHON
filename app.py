from flask import Flask, jsonify, Response
import json
from os import system
from http import HTTPStatus

app = Flask(__name__)

#Leer JSONs
with open ('jsons/usuarios.json','r') as j:
    usuarios = json.load(j)

with open ('jsons/peliculas.json','r') as j:
    peliculas = json.load(j)

with open ('jsons/directores.json','r') as j:
    directores = json.load(j)

with open ('jsons/generos.json','r') as j:
    generos = json.load(j)

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
@app.route("/peliculas/")
def getPeliculas():
    return jsonify(peliculas)

@app.route("/peliculas/save/<id>", methods=['POST'])
def savePelicula(id):
    return 2

@app.route("/peliculas/delete/<id>", methods=['POST'])
def deletePelicula(id):
    return 2

@app.route("/peliculas/<id>")
def getPeliculaByCodigo(id):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            return jsonify(pelicula)
    return Response("{}", status=HTTPStatus.NOT_FOUND)

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
    while not(opcion>=1 and opcion<=4):
        system("cls")
        print('=====================')
        print('1) Ver ultimas 10 peliculas agregadas')
        print('2) Agregar pelicula')
        print('2) Modificar pelicula')
        print('3) Borrar pelicula')
        print('4) Buscar pelicula por ID')
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

def menuInvitado():
    opcion = 0
    while not(opcion == 1):
        system("cls")
        print('=====================')
        print('1) Ver ultimas 10 peliculas agregadas')
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

def ultimasDiezPeliculas():
    contador = 0
    system("cls")
    for pelicula in reversed(peliculas):
        contador = contador + 1
        print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, el director fue {directores[pelicula["idDirector"]]["nombre"]}, ', end='')
        print('tiene los generos ', end="")
        for generoPelis in pelicula["idGeneros"]:
            for genero in generos:
                if genero["id"] == generoPelis:
                    print(genero["nombre"].lower(),', ', end="")
        print('La sinopsis es:', pelicula["sinopsis"])
        if contador == 10:
            break
    input('Ingrese enter para continuar...')

def main():
    opcionMenuBienvennida = 0
    while opcionMenuBienvennida != 3:
        opcionMenuBienvennida = MenuBienvenida()
        if opcionMenuBienvennida == 1:
            opcionIniciarSesion()
            opcion = menuUsuario()
            if opcion == 1:
                ultimasDiezPeliculas()
        if opcionMenuBienvennida == 2:
            opcion = menuInvitado()
            if opcion == 1:
                ultimasDiezPeliculas()

main()