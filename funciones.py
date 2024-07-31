import os
import json
import pathlib
from leer_json import *





desicion=("1.Si","2.No")
modificar=("1.Nombre", "2.Poblacion Estimada", "3.Pais perteneciente", "4.Salir")


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
                if Gestion.get(postal,None)==None:
                    print("Error la ciudad no existe aun.")
                    continue
                else:
                    print("~"*100)
                    print("¿Que desea modificar?")
                    for i in modificar:
                        print(i)
                    opc = int(input("-->"))
                    if opc==4:
                        print("Saliendo...")
                        return
                    elif opc==1:
                        print("~"*100)
                        print(f"Numero de ciudad {postal}")
                        for llave, valor in Gestion[postal].items():
                            print(f"{llave}: {valor}")
                        print("~"*100)
                        nombre=input("Escriba el nuevo nombre de la ciudad:\n-> ").strip().lower()
                        Gestion[postal]["Nombre"]=nombre
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
                            guardar_JSON(Gestion,Archivo)
                        else:
                            print("Digite un valor correcto")
                            continue 
                        print("¿Desea cambiar algo mas?")
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
                            continue
                    elif opc==2:
                        print("~"*100)
                        print(f"Numero de ciudad {postal}")
                        for llave, valor in Gestion[postal].items():
                            print(f"{llave}: {valor}")
                        print("~"*100)
                        poblacion=input("Escriba la nueva poblacion estimada de la ciudad:\n-> ").strip().lower()
                        Gestion[postal]["Poblacion"]=poblacion
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
                            guardar_JSON(Gestion,Archivo)
                        else:
                            print("Digite un valor correcto")
                            continue 
                        print("¿Desea cambiar algo mas?")
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
                            continue
                    elif opc==3:
                        print("~"*100)
                        print(f"Numero de ciudad {postal}")
                        for llave, valor in Gestion[postal].items():
                            print(f"{llave}: {valor}")
                        print("~"*100)
                        pais=input("Escriba el nuevo pais perteneciente:\n-> ").strip().lower()
                        Gestion[postal]["Pais"]=pais
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
                            guardar_JSON(Gestion,Archivo)
                        else:
                            print("Digite un valor correcto")
                            continue 
                        print("¿Desea cambiar algo mas?")
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
                            continue
                    else:
                        print("Digite un valor correcto")
                        continue
            else:
                print("Digite un valor correcto")
                print("~"*100) 
                continue
        except ValueError:
            print("Digite un valor correcto")
            print("~"*100) 
            continue 


def buscar_ciudad_codigo():
    clear_screen()
    while True:
        try:
            Archivo="Registro_Ciudades.json"
            Gestion= crear_leer_json(Archivo)
            postal=input("Escriba el codigo postal de la ciudad:\n-> ")
            if Gestion.get(postal,None)==None:
                print("Error la ciudad no existe aun.")
                continue
            else:
                print("~"*100)
                print("La ciudad es: ",Gestion.get(postal))
                print("~"*100)
        except:
            print("hubo un error al mostrar las tarjetas del cliente")
            continue



def buscar_ciudad_nombre():
    clear_screen()
    while True:
        try:
            Archivo="Registro_Ciudades.json"
            Gestion= crear_leer_json(Archivo)
            nombre=input("Escriba el nombre de la ciudad:\n-> ").strip().lower()
            print("~"*100)
            for llave, ciudad_info in Gestion.items():
                if ciudad_info.get("Nombre")==nombre:
                    print(f"Ciudad: {ciudad_info.get('Nombre')}")
                    print(f"Codigo Postal: {llave}")
                    print(f"Pais: {ciudad_info.get('Pais')}")
                    print(f"Poblacion: {ciudad_info.get('Poblacion')}")
                else:
                    print("Ciudad no encontrada")
                    continue
            print("~"*100)
            print("desea continuar con la consulta por nombre?")
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
        except:
            print("hubo un error al mostrar las tarjetas del cliente")
            continue


def buscar_ciudad_pais():
    clear_screen()
    while True:
        try:
            Archivo="Registro_Ciudades.json"
            Gestion= crear_leer_json(Archivo)
            pais=input("Escriba el nombre del pais:\n-> ").strip().lower()
            print("~"*100)
            for llave, ciudad_info in Gestion.items():
                if ciudad_info.get("Pais")==pais:
                    print(f"Ciudad: {ciudad_info.get('Nombre')}")
                    print(f"Codigo Postal: {llave}")
                    print(f"Pais: {ciudad_info.get('Pais')}")
                    print(f"Poblacion: {ciudad_info.get('Poblacion')}")
                    print("~"*100)
                else:
                    print("Ciudad no encontrada")
                    continue
            print("~"*100)
            print("desea continuar con la consulta por pais?")
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
        except:
            print("hubo un error al mostrar las tarjetas del cliente")
            continue










