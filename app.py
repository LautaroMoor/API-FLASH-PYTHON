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

with open ('jsons/comentarios.json','r') as archivoJson:
    comentarios = json.load(archivoJson)

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
    while True:
        print('=====================')
        usuarioIngresado = input('Ingrese su usuario: ').lower()
        contrasenaIngresada =  input('Ingrese su contrasena: ').lower()
        print('=====================')
        for usuario in usuarios:
            if usuario["usuario"] == usuarioIngresado and usuario["contrasena"] == contrasenaIngresada:
                input('Logeo exitoso!! Enter para continuar!')
                return usuario["id"]

def menuUsuario():
    opcion = 0
    while not(opcion>=1 and opcion<=6):
        system("cls")
        print('=====================')
        print('1) Ver ultimas 10 peliculas agregadas')
        print('2) Agregar pelicula')
        print('3) Modificar pelicula')
        print('4) Borrar pelicula')
        print('5) Buscar pelicula por ID o titulo')
        print('6) Comentarios')
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

def menuComentarios():
    opcion = 0
    while not(opcion>=1 and opcion<=5):
        system("cls")
        print('=====================')
        print("1) Agregar un comentario.")
        print("2) Eliminar un comentario.")
        print("3) Editar un comentario.")
        print("4) Salir")
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

def agregarComentario(idUsuario):
    encontrada = False
    agregar = input("Ingrese ID o Nombre de la pelicula: ")
    for pelicula in peliculas:
        if pelicula["id"] == agregar or pelicula["titulo"].lower() == agregar:
            comentario = input("¿Que comentario quiere agregar?: ")
            idComentarioNuevo = int(comentarios[-1]["id"]) + 1
            nuevoComentario={"id":str(idComentarioNuevo),"idUsuario":idUsuario,"comentario":comentario}
            pelicula["idComentarios"].append(str(idComentarioNuevo))
            encontrada = True
            comentarios.append(nuevoComentario)   
    if encontrada == False:
        print('Error al intentar crear un nuevo comentario!')
    else:    
        print('Comentario exitoso!!')
        with open('jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
        with open('jsons/comentarios.json', 'w') as archivoJson:
            json.dump(comentarios, archivoJson, indent=4)
    input('Ingrese enter para continuar...')


def eliminarComentario(idUsuario):
    listaComentariosUsuario = []
    encontrada = False
    #Lista de comentarios by idUsuario
    print('Su lista de comentarios es: ')
    print('=====================')
    for comentario in comentarios:
        if comentario["idUsuario"] == idUsuario:
            listaComentariosUsuario.append(comentario["id"])
            print("ID=",comentario["id"],"\nComentario:",comentario["comentario"])
            print('=====================')
    
    #Validacion de entrada
    while True:
        borrar = input("Ingrese el ID del comentario que desea eliminar: ")
        if borrar in listaComentariosUsuario:
            encontrada = True
            break
        else:
            print('Error, ingreso un numero que no es suyo o no existe')
    
    for comentario in comentarios:
        if comentario["id"] == borrar:
            comentarios.remove(comentario)

    for pelicula in peliculas:
        for comentarioRecorrido in pelicula["idComentarios"]:
            if comentarioRecorrido == borrar:
                pelicula["idComentarios"].remove(comentarioRecorrido)
                
    #comentario de salida + guardado de jsons
    if encontrada == True:
        print('Borrado con exito')
        with open('jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
        with open('jsons/comentarios.json', 'w') as archivoJson:
            json.dump(comentarios, archivoJson, indent=4)
    else:
        print('Error al borrar')
    input('Ingrese enter para continuar...')
    
def modificarComentario(idUsuario):
    listaComentariosUsuario = []
    encontrada = False
    #Lista de comentarios by idUsuario
    print('Su lista de comentarios es: ')
    print('=====================')
    for comentario in comentarios:
        if comentario["idUsuario"] == idUsuario:
            listaComentariosUsuario.append(comentario["id"])
            print("ID=",comentario["id"],"\nComentario:",comentario["comentario"])
            print('=====================')
    
    #Validacion de entrada
    while True:
        modificar = input("Ingrese el ID del comentario que desea modificar: ")
        if modificar in listaComentariosUsuario:
            encontrada = True
            break
        else:
            print('Error, ingreso un numero que no es suyo o no existe')

    while True:
        comentarioNuevo = input('Ponga su mensaje modificado:\n')
        if comentarioNuevo != '':
            break

    for comentario in comentarios:
        if comentario["id"] == modificar:
            comentario["comentario"] = comentarioNuevo

    if encontrada == True:
        print('Modificacion con exito')
        with open('jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
        with open('jsons/comentarios.json', 'w') as archivoJson:
            json.dump(comentarios, archivoJson, indent=4)
    else:
        print('Error al modificar')
    input('Ingrese enter para continuar...')

def main():
    opcionMenuBienvennida = 0
    while opcionMenuBienvennida != 3:
        opcionMenuBienvennida = MenuBienvenida()
        #Inicio sesion
        if opcionMenuBienvennida == 1:
            idUsuario=opcionIniciarSesion()
            opcion = menuUsuario()
            if opcion == 1:
                ultimasDiezPeliculas()
            if opcion == 4:
                borrarPelicula()
            if opcion == 5:
                getPeliculaByCodigo()
            if opcion == 6:
                opcionComentario = menuComentarios()
                if opcionComentario == 1:
                    agregarComentario(idUsuario)
                elif opcionComentario == 2:
                    eliminarComentario(idUsuario)
                else:
                    modificarComentario(idUsuario)


        #Invitado
        if opcionMenuBienvennida == 2:
                ultimasDiezPeliculas()
        

main()