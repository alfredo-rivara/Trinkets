import os
import csv
import tkinter as tk
from tkinter import filedialog

def agregar_prefijo():
    """
    Agrega un prefijo a cada archivo .docx en la misma carpeta donde se encuentra el script,
    leyendo los prefijos desde un archivo CSV seleccionado por el usuario a través de una ventana.
    """

    # 1. Obtener la ruta de la carpeta donde se encuentra el script
    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    print(f"La ruta de la carpeta del script es: {ruta_carpeta}")

    # 2. Solicitar la ubicación del archivo CSV al usuario
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    print("Selecciona el archivo CSV que contiene los prefijos...")
    ruta_csv = filedialog.askopenfilename(
        title="Selecciona el archivo CSV de prefijos",
        filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
    )

    if not ruta_csv:
        print("No se seleccionó ningún archivo CSV.")
        return

    archivos = os.listdir(ruta_carpeta)
    # Filtrar para obtener solo archivos .docx
    archivos_docx = [archivo for archivo in archivos if archivo.lower().endswith(".docx")]
    archivos_docx.sort()
    print(f"Archivos DOCX encontrados: {archivos_docx}")

    prefijos = []
    try:
        with open(ruta_csv, 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            # next(lector_csv, None)  # Se elimina la línea que saltaba el encabezado
            for i, fila in enumerate(lector_csv):
                # Se añade la validación para saltar la primera fila si es un encabezado no deseado
                if i == 0 and not fila[0].startswith("CMA-"):  # Comprueba si la primera fila parece ser un encabezado
                    print(f"Saltando la línea de encabezado: {fila[0]}")
                    continue  # Saltar la primera fila
                prefijo = fila[0]
                print(f"Leyendo línea {i + 1}: Prefijo leído: '{prefijo}', Longitud: {len(prefijo)}")
                prefijos.append(prefijo + "_")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo CSV en la ruta: {ruta_csv}")
        return
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return

    print(f"Lista de prefijos completa: {prefijos}")
    print(f"Cantidad de archivos DOCX: {len(archivos_docx)}, Cantidad de prefijos: {len(prefijos)}")

    if len(archivos_docx) != len(prefijos):
        print("Error: La cantidad de archivos DOCX y prefijos no coincide.")
        print(f"Archivos DOCX: {len(archivos_docx)}, Prefijos: {len(prefijos)}")
        return

    for i, archivo in enumerate(archivos_docx):
        ruta_antigua = os.path.join(ruta_carpeta, archivo)
        nuevo_nombre = prefijos[i] + archivo
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        os.rename(ruta_antigua, ruta_nueva)
        print(f"Archivo '{archivo}' renombrado a '{nuevo_nombre}'")

    print("Proceso completado.")

# Llamar a la función principal
agregar_prefijo()

# Mantener la consola abierta hasta que se presione Enter
input("Presiona Enter para salir...")