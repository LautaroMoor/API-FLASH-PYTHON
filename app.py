from flask import Flask, jsonify, Response
import json
from os import system
from http import HTTPStatus

app = Flask(__name__)

#Leer JSONs
with open ('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/usuarios.json','r') as archivoJson:
    usuarios = json.load(archivoJson)

with open ('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json','r') as archivoJson:
    peliculas = json.load(archivoJson)

with open ('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/directores.json','r') as archivoJson:
    directores = json.load(archivoJson)

with open ('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/generos.json','r') as archivoJson:
    generos = json.load(archivoJson)

with open ('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/comentarios.json','r') as archivoJson:
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
    with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
        json.dump(peliculas, archivoJson, indent=4)
    return jsonify(peliculas)

@app.route("/peliculas/delete/<id>", methods=['DELETE'])
def deletePelicula(id):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            peliculas.remove(pelicula)
            with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
                json.dump(peliculas, archivoJson, indent=4)
            return jsonify(peliculas)

@app.route("/peliculas/<id>")
def getPeliculaByCodigo(id):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            return jsonify(pelicula)
    return Response("{}", status=HTTPStatus.NOT_FOUND)

#MENU PRINCIPAL
def MenuBienvenida():
    opcion = 0
    while not(opcion>=1 and opcion<=3):
        system("cls")
        print('=====================')
        print('\tBienvenido')
        print('=====================')
        print('1) Iniciar sesion')
        print('2) Ingresar como invitado')
        print('3) Para salir')
        print('=====================')
        opcion = int(input('Ingresar opcion: '))
    return opcion

#LOGEO USUARIO
def opcionIniciarSesion():
    system("cls")
    exitoso = False
    while True:
        system('cls')
        print('=====================')
        print('Inicio sesion usuarios')
        print('=====================')
        usuarioIngresado = input('Ingrese su usuario: ').lower()
        contrasenaIngresada =  input('Ingrese su contrasena: ').lower()
        print('=====================')
        for usuario in usuarios:
            if usuario["usuario"] == usuarioIngresado and usuario["contrasena"] == contrasenaIngresada:
                input('Logeo exitoso!! Enter para continuar!')
                return usuario["id"]
        if exitoso==False:
            print('Error al logear!')
            input('Enter para volver a intentarlo...')

#MENU USUARIO LOGEADO
def menuUsuario():
    opcion = 0
    while not(opcion>=1 and opcion<=7):
        system("cls")
        print('=====================')
        print('\tMenu principal')
        print('=====================')
        print('1) Ver ultimas 10 peliculas agregadas')
        print('2) Agregar pelicula')
        print('3) Modificar pelicula')
        print('4) Borrar pelicula')
        print('5) Buscar pelicula por ID o titulo')
        print('6) Comentarios')
        print('7) Salir/Deslogear')
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

#Opcion 1
def ultimasDiezPeliculas():
    contador = 0
    system("cls")
    for pelicula in reversed(peliculas):
        contador = contador + 1
        print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, \
el director fue {directores[int(pelicula["idDirector"])-1]["nombre"]}, el genero es {generos[int(pelicula["idGenero"])-1]["nombre"]}, \
la sinopsis es "{pelicula["sinopsis"]}" y la imagen es {pelicula["imagen"]}')
        if contador == 10:
            break
    input('Ingrese enter para continuar...')

#Opcion 2
def agregarPelicula():
    system ("cls")
    idPeliculaNueva = int(peliculas[-1]["id"]) + 1
    print('=====================')
    print("registrar pelicula")
    print('=====================')
    titulo=input("Ingrese titulo: ")
    while (titulo == ""):
        system ("cls")
        print('=====================')
        print("El titulo no puede estar vacío.")
        print('=====================')
        titulo=input("Ingrese titulo: ")
    system("cls")
    ano=input("Ingrese año de la pelicula: ")
    while (len(ano) != 4):
        system("cls")
        print("=====================")
        print(ano, "no es un año valido.")
        print("=====================")
        ano=input("Ingrese año de la pelicula: ")
    idDirector=menuDirectores()
    idGenero=menuGeneros()
    system("cls")
    sinopsis=input("Ingrese sinopsis: ")
    while (sinopsis == ""):
        system ("cls")
        print('=====================')
        print("la sinopsis no puede estar vacía.")
        print('=====================')
        sinopsis=input("Ingrese sinopsis: ")
    system("cls")
    imagen=input("Ingrese URL imagen: ")
    while (imagen == ""):
        system ("cls")
        print('=====================')
        print("Es necesaria una URL de imagen.")
        print('=====================')
        imagen=input("Ingrese URL imagen: ")
    nuevaPelicula={"id":str(idPeliculaNueva),"titulo":titulo, "ano":ano, "idDirector":idDirector, "idGenero":idGenero, "sinopsis":sinopsis, "imagen":imagen, "idComentarios":[]}
    peliculas.append(nuevaPelicula)
    print("=====================")
    print("Pelicula registrada correctamente.")
    print("=====================")
    with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
        json.dump(peliculas, archivoJson, indent=4)

#Opcion 3
def modificarPelicula():
    opcion = 0
    system('cls') 
    print('=====================')
    print('Modificar una pelicula')
    print('=====================')
    modificar = input('Ingrese id o titulo de la pelicula: ')
    for pelicula in peliculas:
        if pelicula["id"] == modificar or pelicula["titulo"].lower() == modificar.lower():
            encontrada = True
            while opcion != 7:
                opcion = menuModificar()
                if opcion == 1:
                    while True:
                        valor = input(f"El titulo actualmente es '{pelicula['titulo']}', Cual es el titulo modificado?:")
                        if valor != '':
                            pelicula['titulo'] = valor
                            modificacionExitosa()
                            break
                        else:
                            print('Error, ponga minimo una letra')
                elif opcion == 2:
                    while True:
                        valor = input(f"El ano es '{pelicula['ano']}', Cual es el ano modificado?:")
                        if len(valor) == 4:
                            pelicula['ano'] = valor
                            modificacionExitosa()
                            break
                        else:
                            print('Error, ingrese un ano de cuatro cifras')
                elif opcion == 3:
                    valor = menuDirectores(pelicula['idDirector'])
                    pelicula['idDirector'] = valor
                    modificacionExitosa()
                elif opcion == 4:
                    valor = menuGeneros(pelicula['idGenero'])
                    pelicula['idGenero'] = valor
                    modificacionExitosa()
                elif opcion == 5:
                    while True:
                        valor = input(f"La sinopsis es '{pelicula['sinopsis']}', Cual es la sinopsis modificada?:")
                        if valor != '':
                            pelicula['sinopsis'] = valor
                            modificacionExitosa()
                            break
                        else:
                            print('Error, ponga minimo una letra')
                elif opcion == 6:
                    while True:
                        valor= input(f"El imagen es '{pelicula['imagen']}', Cual es la imagen modificada?:")
                        if valor != '':
                            pelicula['imagen']  = valor
                            modificacionExitosa()
                            break
                        else:
                            print('Error, ponga minimo una letra')
                
    if encontrada == True:
        print('Pelicula modificada exitosamente')
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
    else:
        print('Error')

#Opcion 4
def borrarPelicula():
    encontrada = False
    system("cls")
    print('=====================')
    print('Borrar una pelicula')
    print('=====================')
    borrar = input('Ingrese el id o el nombre de la pelicula que desea borrar: ')
    for pelicula in peliculas:
        if pelicula["id"] == borrar or pelicula["titulo"].lower() == borrar.lower():
            peliculas.remove(pelicula)
            encontrada = True
    if encontrada == False:
        print('No se pudo borrar porque no existe')
    else:
        print('Borrado exitoso')
    with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
        json.dump(peliculas, archivoJson, indent=4)
    input('Ingrese enter para continuar...')

#Opcion 5
def getPeliculaByCodigo():
    system("cls")
    encontrada = False
    buscar = input('Ingrese la id o titulo: ')
    for pelicula in peliculas:
        if pelicula["id"] == buscar or pelicula["titulo"].lower() == buscar:
            print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, \
                el director fue {directores[int(pelicula["idDirector"])-1]["nombre"]}, el genero es {generos[int(pelicula["idGenero"])-1]["nombre"]}\
                la sinopsis es "{pelicula["sinopsis"]}" y la imagen es {pelicula["imagen"]}')
            encontrada = True
    if encontrada == False:
        print('No fue encontradada')
    input('Ingrese enter para continuar...')

#MENU COMENTARIOS OPCION 6
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

#Opcion 6 opcion 1
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
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/comentarios.json', 'w') as archivoJson:
            json.dump(comentarios, archivoJson, indent=4)
    input('Ingrese enter para continuar...')

#Opcion 6 opcion 2
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
            system("cls")
            print("===================================================")
            print('Error, ingreso un numero que no es suyo o no existe')
            print("===================================================")
    
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
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/comentarios.json', 'w') as archivoJson:
            json.dump(comentarios, archivoJson, indent=4)
    else:
        print('Error al borrar')
    input('Ingrese enter para continuar...')

#Opcion 6 opcion 3
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
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/peliculas.json', 'w') as archivoJson:
            json.dump(peliculas, archivoJson, indent=4)
        with open('C:/Users/santi/Desktop/final pro2/API-FLASK-PYTHON/jsons/comentarios.json', 'w') as archivoJson:
            json.dump(comentarios, archivoJson, indent=4)
    else:
        print('Error al modificar')
    input('Ingrese enter para continuar...')

#MENU DIRECTORES
def menuDirectores(anterior = None):
    system("cls")
    opcion = 0
    while not(opcion>=1 and opcion<=contador):
        contador = 0
        if anterior != None:
            for director in directores:
                if director['id'] == anterior:
                    print(f'El director actual es {director["nombre"]}')
        print('=====================')
        print("Los directores disponibles son:")
        print('=====================')
        for director in directores:
            contador = contador + 1
            print(f'{contador}) {director["nombre"]}')
        print('=====================')
        opcion= int(input("Ingrese opcion: "))
        if not(opcion>=1 and opcion<=contador):
            system("cls")
            print('=====================')
            print(f"{opcion} no es una ID válida.")
            print('=====================')
    return str(opcion)

#MENU GENEROS
def menuGeneros(anterior = None):
    system("cls")
    opcion = 0
    while not(opcion>=1 and opcion<=contador):
        contador = 0
        if anterior != None:
            for genero in generos:
                if genero['id'] == anterior:
                    print(f'El genero actual es {genero["nombre"]}')
        print('=====================')
        print("Los generos disponibles son:")
        print('=====================')
        for genero in generos:
            contador = contador + 1
            print(f'{genero["id"]}) {genero["nombre"]}')
        print('=====================')
        opcion= int(input("Ingrese opcion: "))
        if not(opcion>=1 and opcion<=contador):
            system("cls")
            print('=====================')
            print(f"{opcion} no es una ID válida.")
            print('=====================')
    return str(opcion)

#MENU MODIFICACION EXITOSA
def modificacionExitosa():
    print('Modificacion exitosa')
    input('Pulse enter para seguir modificando...')

#MENU MODIFICAR
def menuModificar():
    opcion = 0
    while not(opcion>=1 and opcion<=7):
        system('cls')  
        print('=====================')
        print('Menu editor')
        print('=====================')
        print('1) Titulo')
        print('2) Año')
        print('3) Director')
        print('4) Generos')
        print('5) Sinopsis')
        print('6) Imagen')
        print('7) Terminar/Salir')
        print('=====================')
        opcion = int(input('Opcion: ')) 
    return opcion

def main():
    opcionMenuBienvennida = 0
    while opcionMenuBienvennida != 3:
        opcionMenuBienvennida = MenuBienvenida()
        #Inicio sesion
        if opcionMenuBienvennida == 1:
            idUsuario=opcionIniciarSesion()
            while True:
                opcion = menuUsuario()
                if opcion == 1:
                    ultimasDiezPeliculas()
                if opcion == 2:
                    agregarPelicula()
                if opcion == 3:
                    modificarPelicula()
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
                if opcion == 7:
                    break

        #Invitado
        if opcionMenuBienvennida == 2:
                ultimasDiezPeliculas()
        

main()