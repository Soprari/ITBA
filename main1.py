#from tkinter import X
from api import pull_data
from base import createtb,insert_rows,convierte_datos,read_fechMAX, read_fechMIN,find_stock
from datetime import datetime
import pandas as pd
from grafico1 import grafica1

#Carga del menu principal

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

1
def menu_principal():
    opciones = {
        '1': ('Actualización de datos', accion1),
        '2': ('Visualización de datos', accion2),
        '3': ('Salir', salir)
    }

    generar_menu(opciones, '3')

#Carga del menu secundario 

def menu_principal2():
    opciones = {
        '1': ('Resumen', accion4),
        '2': ('Grafico', accion5),
        '3': ('Salir', salir)
    }

    generar_menu(opciones, '3')

# Funciones de las opciones seleccionadas

def accion1():

    sticker = input('Ingrese ticker a pedire:\n ')
    date_from = input('Ingrese fecha de inicio(aaaa-mm-dd):\n ')
    date_to = input('Ingrese fecha de fin(aaaa-mm-dd):\n ')
    print('Pidiendo datos ...') 
    a = pull_data(sticker, date_from, date_to)
    lista = convierte_datos(a)
    insert_rows(lista)
    
    if a != []:
        print('Datos guardados correctamente')


      
 
def accion2():
    menu_principal2()
   

def accion4():
    stock = find_stock()
    df1 = pd.DataFrame(stock)
    for i in range(0,(len(df1))):
        dato = df1.iloc[i,0]
        fechMin = read_fechMIN(dato)
        fechMin = pd.DataFrame(fechMin)
        fechMin = fechMin.iloc[0,0]
        fechMax = read_fechMAX(dato)
        fechMax = pd.DataFrame(fechMax)
        fechMax = fechMax.iloc[0,0]
        print(dato+' - '+ fechMin + ' <-> ' + fechMax)
    

def accion5():
    sticker = input('Ingrese ticker a pedire:\n ')
    grafica1(sticker)
   
def salir():
    print('Saliendo')


if __name__ == '__main__':
   
    createtb()
    menu_principal()
