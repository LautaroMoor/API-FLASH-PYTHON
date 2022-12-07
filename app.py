from flask import Flask 
import json
from os import system

app = Flask(__name__)

with open ('jsons/usuarios.json','r') as j:
    usuarios = json.load(j)

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
        print('Ingresar opcion: ')
        opcion = int(input('Ingresar: '))
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
                return inicioExitoso 
            
def main():
    opcionMenuBienvennida = 0
    while opcionMenuBienvennida != 3:
        opcionMenuBienvennida = MenuBienvenida()
        if opcionMenuBienvennida == 1:
            opcionIniciarSesion()

main()