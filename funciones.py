from os import system
import requests

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
        while True:
            usuarioIngresado = input('Ingrese su usuario: ').lower()
            contrasenaIngresada =  input('Ingrese su contrasena: ').lower()
            if usuarioIngresado == '' or contrasenaIngresada == '':
                print ('No puede dejar los campos vacios')
                input('Enter para continuar...')
                system('cls')
                continue
            break
        print('=====================')
        check = requests.get(f'http://127.0.0.1:5000/usuario/{usuarioIngresado}/contrasena/{contrasenaIngresada}')
        id = check.text
        if id == 'Error' or id == None:
            print("=====================")
            print('Error')
            print("=====================")
            input('Enter para continuar...')
            continue
        else:
            print("=====================")
            print('Logeo exitoso')
            print("=====================")
            input('Enter para continuar...')
            return id

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
        print('5) Buscar pelicula por ID')
        print('6) Comentarios')
        print('7) Salir/Deslogear')
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

#Opcion 1 MODIFICADO
def ultimasDiezPeliculas():
    contador = 0
    system("cls")
    peliculasData = requests.get('http://127.0.0.1:5000/ultimasdiezpeliculas')
    peliculas = peliculasData.json()
    # for pelicula in reversed(peliculas):
    for pelicula in peliculas:
        directorData = requests.get(f'http://127.0.0.1:5000/directores/{pelicula["idDirector"]}')
        director = directorData.json()
        generoData = requests.get(f'http://127.0.0.1:5000/generos/{pelicula["idGenero"]}')
        genero = generoData.json()
        print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, \
el director fue {director["nombre"]}, el genero es {genero["nombre"]}, \
la sinopsis es "{pelicula["sinopsis"]}" y la imagen es {pelicula["imagen"]}')
    input('Ingrese enter para continuar...')

#Opcion 2 MODIFICADO
def agregarPelicula():
    system ("cls")
    print('=====================')
    print("Registrar pelicula")
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
    nuevaPelicula={"id":"","titulo":titulo, "ano":ano, "idDirector":idDirector, "idGenero":idGenero, "sinopsis":sinopsis, "imagen":imagen, "idComentarios":[]}
    datos = requests.post('http://127.0.0.1:5000/peliculas/create', json=nuevaPelicula)
    mensaje = datos.json
    print("=====================")
    print(mensaje)
    print("=====================")
    input('Enter para continuar...')

#Opcion 3
def modificarPelicula():
    
    opcion = 0
    encontrada = False

    peliculaNuevaDiccionario = {"id":"","titulo":"","ano":"","idDirector":"","idGenero":"","sinopsis":"","imagen":""}

    system('cls') 
    print('=====================')
    print('Modificar una pelicula')
    print('=====================')
    
    modificar = input('Ingrese id: ')
    peliculaData = requests.get('http://127.0.0.1:5000/peliculas')
    peliculas = peliculaData.json()
    for pelicula in peliculas:
        if pelicula["id"] == modificar:
            encontrada = True
            while opcion != 7:
                opcion = menuModificar()
                peliculaNuevaDiccionario = {"id":"","titulo":"","ano":"","idDirector":"","idGenero":"","sinopsis":"","imagen":""}
                if opcion == 1:
                    while True:
                        valor = input(f"El titulo actualmente es '{pelicula['titulo']}', Cual es el titulo modificado?:")
                        if valor != '':
                            peliculaNuevaDiccionario['titulo'] = valor
                            break
                        else:
                            print('Error, ponga minimo una letra')
                elif opcion == 2:
                    while True:
                        valor = input(f"El ano es '{pelicula['ano']}', Cual es el ano modificado?:")
                        if len(valor) == 4:
                            peliculaNuevaDiccionario['ano'] = valor
                            break
                        else:
                            print('Error, ingrese un ano de cuatro cifras')
                elif opcion == 3:
                    peliculaNuevaDiccionario['idDirector'] = menuDirectores(pelicula['idDirector'])
                elif opcion == 4:
                    peliculaNuevaDiccionario['idGenero'] = menuGeneros(pelicula['idGenero'])
                elif opcion == 5:
                    while True:
                        valor = input(f"La sinopsis es '{pelicula['sinopsis']}', Cual es la sinopsis modificada?:")
                        if valor != '':
                            peliculaNuevaDiccionario['sinopsis'] = valor
                            break
                        else:
                            print('Error, ponga minimo una letra')
                elif opcion == 6:
                    while True:
                        valor= input(f"El imagen es '{pelicula['imagen']}', Cual es la imagen modificada?:")
                        if valor != '':
                            peliculaNuevaDiccionario['imagen']  = valor
                            break
                        else:
                            print('Error, ponga minimo una letra')

                peliculaNuevaDiccionario["id"] = modificar
                datos = requests.put(f'http://127.0.0.1:5000/peliculas/save/', json=peliculaNuevaDiccionario)
                mensaje = datos.text
                print("=====================")
                print(mensaje)
                print("=====================")
                input('Enter para continuar...')
    
    if encontrada == False:
        system("cls")
        print("===================================================")
        print('No hay peliculas.')
        print("===================================================")
    
    input('Ingrese enter para continuar...')

#Opcion 4 MODIFICADO
def borrarPelicula():
    encontrada = False
    system("cls")
    print('=====================')
    print('Borrar una pelicula')
    print('=====================')
    borrar = input('Ingrese el id: ')
    datos = requests.delete(f'http://127.0.0.1:5000/peliculas/delete/{borrar}')
    mensaje = datos.text
    print("=====================")
    print(mensaje)
    print("=====================")
    input('Ingrese enter para continuar...')

#Opcion 5 MODIFICADO
def getPeliculaByCodigo():
    system("cls")
    buscar = input('Ingrese la id: ')
    peliculaData = requests.get(f'http://127.0.0.1:5000/peliculas/{buscar}')
    pelicula = peliculaData.json()
    directorData = requests.get(f'http://127.0.0.1:5000/directores/{pelicula["idDirector"]}')
    director = directorData.json()
    generoData = requests.get(f'http://127.0.0.1:5000/generos/{pelicula["idGenero"]}')
    genero = generoData.json()
    print(f'ID {pelicula["id"]} = La pelicula {pelicula["titulo"]} salio en el año {pelicula["ano"]}, \
el director fue {director["nombre"]}, el genero es {genero["nombre"]}\
, la sinopsis es "{pelicula["sinopsis"]}" y la imagen es {pelicula["imagen"]}')
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

#Opcion 6 opcion 1 MODIFICADO
def agregarComentario(idUsuario):
    peliculasData = requests.get('http://127.0.0.1:5000/peliculas')
    peliculas = peliculasData.json()
    agregar = input("Ingrese ID de la pelicula: ")
    encontrado = False
    
    for pelicula in peliculas:
        if pelicula["id"] == agregar:
            encontrado = True
            comentario = input("¿Que comentario quiere agregar?: ")
            nuevoComentario={"id":"","idUsuario":idUsuario,"comentario":comentario}
            datos = requests.post(f'http://127.0.0.1:5000/comentario/create/idPelicula/{agregar}', json=nuevoComentario)
            mensaje = datos.text
            print("=====================")
            print(mensaje)
            print("=====================")
    
    if encontrado == False:
        print("=====================")
        print('Error al crear el comentario')
        print("=====================")
            
    input('Ingrese enter para continuar...')

#Opcion 6 opcion 2 MODIFICADO
def eliminarComentario(idUsuario):
    system("cls")
    #Lista de comentarios by idUsuario
    comentariosUsuarioData = requests.get(f"http://127.0.0.1:5000/comentario/idUsuario/{idUsuario}")
    comentariosUsuario = comentariosUsuarioData.json()
    encontrada = False

    if len(comentariosUsuario) != 0:
        for comentario in comentariosUsuario:
            encontrada = True
            print('Su lista de comentarios es: ')
            print('=====================')
            print("ID=",comentario["id"],"\nComentario:",comentario["comentario"])
            print('=====================')
        
        #Validacion de entrada
        while True:
            borrar = input("Ingrese el ID del comentario que desea eliminar: ")
            encontrada2 = False
            for comentario in comentariosUsuario:
                if borrar == comentario["id"]:
                    encontrada2 = True
                    break

            if encontrada2 == True:
                break
            else:
                system("cls")
                print("===================================================")
                print('Error, ingreso un numero que no es suyo o no existe')
                print("===================================================")
        
        datos = requests.delete(f"http://127.0.0.1:5000/comentario/idUsuario/{idUsuario}/delete/{borrar}")
        mensaje = datos.text
        print("===================================================")
        print(mensaje)
        print("===================================================")

    if encontrada == False:
        system("cls")
        print("===================================================")
        print('No tiene comentarios.')
        print("===================================================")
    
    input('Ingrese enter para continuar...')
    
#Opcion 6 opcion 3 MODIFICADO
def modificarComentario(idUsuario):
    listaComentariosUsuario = []
    encontrada = False
    #Lista de comentarios by idUsuario
    comentariosUsuarioData = requests.get(f"http://127.0.0.1:5000/comentario/idUsuario/{idUsuario}")
    comentariosUsuario = comentariosUsuarioData.json()

    encontrada = False
    
    if len(comentariosUsuario) != 0:
        print('Su lista de comentarios es: ')
        print('=====================')
        for comentario in comentariosUsuario:
            encontrada = True
            if comentario["idUsuario"] == idUsuario:
                listaComentariosUsuario.append(comentario["id"])
                print("ID=",comentario["id"],"\nComentario:",comentario["comentario"])
                print('=====================')

        #Validacion de entrada
        while True:
            modificar = input("Ingrese el ID del comentario que desea modificar: ")
            encontrada2 = False
            for comentario in comentariosUsuario:
                if modificar == comentario["id"]:
                    encontrada2 = True
                    break

            if encontrada2 == True:
                break
            else:
                system("cls")
                print("===================================================")
                print('Error, ingreso un numero que no es suyo o no existe')
                print("===================================================")

        while True:
            comentarioNuevo = input('Ponga su mensaje modificado:')
            if comentarioNuevo != '':
                break

        comentarioNuevoLista = {"id":modificar,"idUsuario":idUsuario,"comentario":comentarioNuevo}
        datos = requests.put('http://127.0.0.1:5000/comentario/save', json=comentarioNuevoLista)
        mensaje = datos.text
        print("=====================")
        print(mensaje)
        print("=====================")

    if encontrada == False:
        system("cls")
        print("===================================================")
        print('No tiene comentarios.')
        print("===================================================")
    
    input('Ingrese enter para continuar...')

#MENU DIRECTORES MODIFICADO
def menuDirectores(anterior = None):
    directoresData = requests.get('http://127.0.0.1:5000/directores')
    directores = directoresData.json()
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
            print(f'{director["id"]}) {director["nombre"]}')
        print('=====================')
        opcion= int(input("Ingrese opcion: "))
        if not(opcion>=1 and opcion<=contador):
            system("cls")
            print('=====================')
            print(f"{opcion} no es una ID válida.")
            print('=====================')
    return str(opcion)

#MENU GENEROS MODIFICADO
def menuGeneros(anterior = None):
    generosData = requests.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
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

def getDirectores():
    directoresData = requests.get('http://127.0.0.1:5000/directores')
    directores = directoresData.json()
    system('cls')
    print('=====================')
    print("Los directores son:")
    print('=====================')
    for director in directores:
        print(f'{director["id"]}) {director["nombre"]}')

def getGeneros():
    generosData = requests.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
    system('cls')
    print('=====================')
    print("Los generos son:")
    print('=====================')
    for genero in generos:
        print(f'{genero["id"]}) {genero["nombre"]}')

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