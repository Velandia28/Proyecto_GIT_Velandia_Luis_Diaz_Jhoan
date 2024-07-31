import os
import json
import pathlib
from leer_json import *
from funciones import *
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
                    clear_screen()
                    print("***********************************************")
                    print("NUEVA CIUDAD")
                    print("***********************************************")
                    registrar_Ciudad()
                elif opcion == 2:
                    clear_screen()
                    print("***********************************************")
                    print("MODIFICAR ")
                    print("***********************************************")
                    modificar_ciudad()
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


menu_informacion = ('1. Mostrar informacion de ciudades por nombre de la ciudad', "2. Mostrar informacion de ciudades por pais", "3.Mostrar informacion de ciudades por codigo postal ", "4. VOLVER")

def menu_info():
    clear_screen()
    while True:
            try:
                print("***********************************************")
                print("BIENVENIDOS A LA OPCION DE MOSTRAR INFORMACION ")
                print("************************************************")
                print("Que opcion desea seleccionar para avanzar ")
                print("***********************************************")
                for u in menu_informacion:
                    print(u)
                opc =int(input("Ingrese el numero segun la opcion seleccionada:  "))
                if opc ==1:
                    clear_screen()
                    print("***********************************************")
                    print("ESTA ES LA INFORMACION POR EL NOMBRE DE LA CIUDAD ")
                    print("***********************************************")
                    Buscar_ciudad_nombre()
                elif opc == 2 :
                    clear_screen()
                    print("***********************************************")
                    print("ESTA ES LA INFORMACION POR EL PAIS ")
                    print("***********************************************")
                    buscar_ciudad_pais()
                elif opc== 3:
                    clear_screen()
                    print("***********************************************")
                    print("ESTA ES LA INFORMACION POR EL CODIGO POSTAL ")
                    print("***********************************************")
                    buscar_ciudad_codigo()
                     



menu_principal()
menu_info()