import sqlite3 as sql
import pandas as pd
from datetime import datetime


def createtb():
    conn = sql.connect("basefinanciera.db")
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS basefinanciera(
            Date TEXT PRIMARY KEY NOT NULL,
            Volumen INTEGER,
            Val_W REAL NOT NULL,
            Open REAL NOT NULL,
            Close REAL NOT NULL,
            High REAL NOT NULL,
            Low REAL NOT NULL,
            Timestamp INTEGER NOT NULL,
            n INTEGER,
            Accion TEXT
        )"""
    )
    conn.commit()
    conn.close()

def insert_rows(lista_de_tuplas):
    conn = sql.connect("basefinanciera.db")
    cursor = conn.cursor()
    cursor.executemany(f"""INSERT or IGNORE INTO basefinanciera(Date, Volumen, Val_W, Open, Close, High, Low, Timestamp, n, Accion) VALUES (?,?,?,?,?,?,?,?,?,?)""", lista_de_tuplas)
    conn.commit()
    conn.close()

def convierte_datos(lista):
    lista_final = []
    if len(lista) > 0:
        for i in range (len(lista)):
            a = (str(datetime.fromtimestamp(float(lista[i]['t']) /1000).strftime('%y-%m-%d')), int(lista[i]['v']),
            float(lista[i]['vw']), float(lista[i]['o']), float(lista[i]['c']), float(lista[i]['h']), float(lista[i]['l']),
            float(lista[i]['t']/1000), float(lista[i]['n']), str(lista[i]['s']))
            lista_final += [tuple(a)]
    return lista_final


def read_rows(row):
    try:
        conn = sql.connect('basefinanciera.db')
        cursor = conn.cursor()
        cursor.execute( f"""SELECT Date,Volumen,Val_W,Open,Close,High,Low from basefinanciera WHERE Accion = '{row}'""")
        records = cursor.fetchall()
        return(records)    

    except sql.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")

def find_stock():
    try:
        conn = sql.connect('basefinanciera.db')
        cursor = conn.cursor()
        cursor.execute( """SELECT accion FROM basefinanciera GROUP by Accion""")
        records = cursor.fetchall()
        return(records)    

    except sql.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")

def read_fechMIN(stock):
    conn = sql.connect('basefinanciera.db')
    cursor = conn.cursor()
    cursor.execute( f"""SELECT date FROM basefinanciera WHERE Accion='{stock}' AND date <= date ORDER BY date DESC Limit 1""")
    records = cursor.fetchall()
    return(records)    

def read_fechMAX(stock):
    conn = sql.connect('basefinanciera.db')
    cursor = conn.cursor()
    cursor.execute( f"""SELECT date FROM basefinanciera WHERE Accion='{stock}' AND date <= date ORDER BY date ASC Limit 1""")
    records = cursor.fetchall()
    return(records)  




if __name__ == "__main__":

   #createtb()
   pass
   

