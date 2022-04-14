# Enunciado: Hacer un script en Python que ejecute en Linux el comando "ps aux" y guarde 
# los resultados parseados en un archivo de tipo 'csv' o 'json'. 
#
# Suma +1 puntos: documentarlo, subirlo y compartirlo en github.
# Suma +2 puntos: hacerlo en docker.
# Suma +3 puntos: almacenar los datos en una base de datos (mariadb, mysql, sqlite, etc)

import os
import sqlite3 as db
import pandas as pd


def generar_archivo():
    """Esta función toma la salida del comando ps aux y lo exporta a un archivo csv"""
    comando =  str("ps aux | awk '{print $1 \",\" $2 \",\" $3 \",\" $4 \",\" $5 \",\" $6 \",\" $7 \",\" $8 \",\" $9 \",\" $10 \",\" $11}' > salida.csv")
    os.system(comando)
    print("Archivo generado satisfactoriamente.")

def importar_información():
    """ Esta función crea un dataframe a partir del contenido de un archivo csv.
       :return: Dataframe con la información de los procesos.
    """
    print("Cargando datos")
    data = pd.read_csv("salida.csv")
    print("Los datos han sido cargados")
    print("Información")
    print(data)

    return data

def exportar_informacion(p_dataframe):
    """Esta función toma un dataframe y lo inserta en una base de datos sqlite"""
    
    df = pd.DataFrame(p_dataframe)
    con = db.connect("psinfo.db")

    df.to_sql(name="process_info",con=con ,if_exists="append")

    con.close()
    print("Conexion Cerrada")

def main():
    generar_archivo()
    exportar_informacion(importar_información())
    user_input = input("Presione 'y' para cerrar la conexión")

    if user_input == "y":
        print("********")

if __name__ == '__main__':
    main()
