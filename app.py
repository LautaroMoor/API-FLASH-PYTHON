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
                fc.borrarPelicula()
            if opcion == 5:
                fc.getPeliculaByCodigo()
            if opcion == 6:
                opcionComentario = fc.menuComentarios()
                if opcionComentario == 1:
                    fc.agregarComentario(idUsuario)
                elif opcionComentario == 2:
                    fc.eliminarComentario(idUsuario)
                else:
                    fc.modificarComentario(idUsuario)
            if opcion == 7:
                break

    #Invitado
    if opcionMenuBienvennida == 2:
            fc.ultimasDiezPeliculas()