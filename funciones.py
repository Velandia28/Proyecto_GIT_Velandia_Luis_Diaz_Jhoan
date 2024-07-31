import os
import json
import pathlib
from leer_json import *





desicion=("1.Si","2.No")


def registrar_Ciudad():
    clear_screen()
    while True:
        try:
            Archivo="Registro_Ciudades.json"
            Gestion= crear_leer_json(Archivo)
            ciudad={}
            postal=input("Escriba el codigo postal de la ciudad:\n-> ")
            if Gestion.get(postal,None)==None:
                nombre = input("Escriba el nombre de la ciudad:\n-> ").strip().lower()
                poblacion=input("Escriba la poblacion estimada de la ciudad:\n-> ").strip()
                pais=input("Escriba el pais al que pertenece la ciudad:\n-> ").strip().lower()
                ciudad[postal]={
                    "Nombre": nombre,
                    "Poblacion": poblacion,
                    "Pais": pais,
                    "Codigo Postal": postal,
                }
                print("~"*100)
                print("Estos son los datos a guardar")
                print(ciudad)
                print("~"*100)
                print ("¿Desea continuar y guardar?")
                for i in desicion:
                    print(i)
                opc1=int(input("--> "))
                if opc1==2:
                    print("Vuelva a empezar")  
                    print("~"*100)  
                    continue
                elif opc1==1: 
                    Gestion.update(ciudad)
                    guardar_JSON(Gestion,Archivo)
                else:
                    print("Digite un valor correcto")
                    continue 
                print("¿Desea agregar otra ciudad?")
                for i in desicion:
                    print(i)
                opc1=int(input("--> "))
                if opc1==2:
                    print("Saliendo...")  
                    print("~"*100) 
                    return
                elif opc1==1:
                    continue
                else:
                    print("Digite un valor correcto")
                    print("~"*100) 
                    continue
            else:
                print("El codigo postal ya existe")
                print("~"*100) 
                continue
        except ValueError:
            print("Digite un valor correcto")
            print("~"*100) 
            continue 
        


def modificar_ciudad():
    clear_screen()
    while True:
        try:
            Archivo="Registro_Ciudades.json"
            Gestion= crear_leer_json(Archivo)
            print("Se va a modificar la informacion de la ciudad pero no su codigo postal")
            print("¿Desea continuar?")
            for i in desicion:
                print(i)
            opc1=int(input("--> "))
            if opc1==2:
                print("Saliendo...")  
                print("~"*100) 
                return
            elif opc1==1:
                postal=input("Escriba el codigo postal de la ciudad:\n-> ")
                








            else:
                print("Digite un valor correcto")
                print("~"*100) 
                continue
            


        except ValueError:
            print("Digite un valor correcto")
            print("~"*100) 
            continue 


