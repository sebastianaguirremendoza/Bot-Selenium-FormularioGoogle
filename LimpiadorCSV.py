import csv
import os
import tkinter as tk
from tkinter import filedialog

# Leer el archivo CSV original y crear una nueva lista de datos limpios
# El codigo no llega a procesar las tildes de las letras es por ello que con el LimpiardorCSV.py
# Se podra limpiar y arreglar estos errores para que las respuestas del formulario
# Sean las mas acertadas posibles
# (Si todo tu CSV no tiene ninguna tilde no necesitas limpiarlo, pero porsiaco es recomendable)
# Crear una ventana de Tkinter
# Crear una ventana de Tkinter
ventana = tk.Tk()
ventana.withdraw()  # Ocultar la ventana principal de Tkinter

# Abrir el explorador de archivos para seleccionar el archivo CSV
archivo_csv = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

# Verificar si se seleccionó un archivo
if archivo_csv:
    # Leer el archivo CSV seleccionado y crear una nueva lista de datos limpios
    datos_limpios = []
    with open(archivo_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Limpiar los datos de nombre y correo electrónico
            nombre = row[0].strip().replace("Ã¡", "á").replace("Ã©", "é").replace("Ã­", "í").replace("Ã³", "ó").replace("Ãº", "ú")
            correo = row[1].strip()
            sexo = row[2].strip()

            # Agregar los datos limpios a la nueva lista
            datos_limpios.append([nombre, correo, sexo])

    # Carpeta donde se guardará el archivo procesado
    carpeta_destino = './CSV/'
    ruta_salida = os.path.join(carpeta_destino, 'datos_limpios.csv')

    # Escribir los datos limpios en un nuevo archivo CSV
    with open(ruta_salida, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(datos_limpios)

    print("Proceso terminado. Archivo guardado en:", ruta_salida)
else:
    print("No se seleccionó ningún archivo.")