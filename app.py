import funciones as fc

#MAIN
opcionMenuBienvennida = 0
while opcionMenuBienvennida != 3:
    opcionMenuBienvennida = fc.MenuBienvenida()
    #Inicio sesion
    if opcionMenuBienvennida == 1:
        idUsuario = fc.opcionIniciarSesion()
        while True:
            opcion = fc.menuUsuario()
            if opcion == 1:
                print(idUsuario)
                fc.ultimasDiezPeliculas()
            if opcion == 2:
                fc.agregarPelicula()
            if opcion == 3:
                fc.modificarPelicula()
            if opcion == 4:
                fc.borrarPelicula(idUsuario)
            if opcion == 5:
                fc.getPeliculaByCodigo()
            if opcion == 6:
                fc.getPeliculas()
            if opcion == 7:
                fc.getDirectores()
            if opcion == 8:
                fc.getGeneros()
            if opcion == 9:
                fc.getPeliculaByPortada()
            if opcion == 10:
                fc.getPeliculaByDirector()
            if opcion == 11:
                opcionComentario = fc.menuComentarios()
                if opcionComentario == 1:
                    fc.agregarComentario(idUsuario)
                elif opcionComentario == 2:
                    fc.eliminarComentario(idUsuario)
                elif opcionComentario == 3:
                    fc.modificarComentario(idUsuario)
            if opcion == 12:
                fc.getPeliculaRandom()
            if opcion == 13:
                break

    #Invitado
    if opcionMenuBienvennida == 2:
            fc.ultimasDiezPeliculas()