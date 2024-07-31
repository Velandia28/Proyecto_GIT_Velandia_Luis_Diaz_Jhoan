import os
import json
import pathlib
from leer_json import *

menu_principal1 =("1. REGISTRAR CIUDAD", "2. MODIFICAR CIUDAD","3. MOSTRAR INFORMACION","4. SALIR DEL APLICATIVO")

def menu_principal():
    clear_screen()
    while True:
            try:
                print("***********************************************")
                print("BIENVENIDOS AL SISTEMA CIUDADES ")
                print("************************************************")
                print("Que opcion desea seleccionar para avanzar ")
                print("***********************************************")
                for i in  menu_principal1:
                     print(i) 
                opcion= int(input("ingrese el numero segun la opcion seleccionada:  "))
                if  opcion == 1:
                    #menu_registrar()
                    clear_screen()
                    print("***********************************************")
                    print("NUEVA CIUDAD")
                    print("***********************************************")
                elif opcion == 2:
                    #menu_modificar()
                    clear_screen()
                    print("***********************************************")
                    print("MODIFICAR ")
                    print("***********************************************")
                elif opcion == 3:
                     #menu_informacion
                     clear_screen()
                     print("***********************************************")
                     print("INFORMACION")
                     print("***********************************************")
                elif opcion == 4:
                     clear_screen()
                     print("*****************************")
                     print(".....SALIENDO ES SALIENDO .....")
                     print("*****************************")
                     break
                else :
                    print("Opción no válida, por favor intente nuevamente.")
                continue
            except ValueError:
                print("Por favor ingrese un número válido.")
                continue
# FUNCION DE REGISTRAR CIUDADES SE LLAMA registrar_Ciudad()
# FUNCION DE MODIFICAR CIUDAD SE LLAMA modificar_ciudad()

menu_principal()

