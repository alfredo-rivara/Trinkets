import os
import tkinter as tk
from tkinter import filedialog
import argparse

def remover_primeros_cinco_caracteres(ruta):
    """Remueve los primeros 5 caracteres del nombre de cada archivo .docx y .pdf 
       en la carpeta especificada.

    Args:
        ruta: La ruta a la carpeta.
    """

    try:
        archivos = os.listdir(ruta)
    except FileNotFoundError:
        print(f"Error: La carpeta '{ruta}' no fue encontrada.")
        return

    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)

        if extension.lower() in ('.docx', '.pdf'):  # Usar tupla para mejor rendimiento
            if len(nombre) > 5:
                nombre_viejo = os.path.join(ruta, archivo)
                nombre_nuevo = os.path.join(ruta, nombre[5:] + extension)
                try:
                    os.rename(nombre_viejo, nombre_nuevo)
                    print(f"Se renombró '{archivo}' a '{nombre[5:] + extension}'")
                except OSError as e:
                    print(f"Error al renombrar '{archivo}': {e}")


def seleccionar_carpeta():
    """Abre un diálogo para que el usuario seleccione una carpeta."""
    root = tk.Tk()  # Crea una ventana raíz de Tkinter (invisible)
    root.withdraw()  # Oculta la ventana raíz

    ruta_seleccionada = filedialog.askdirectory()  # Abre el diálogo de selección de carpeta

    if ruta_seleccionada:
        return ruta_seleccionada
    else:
        return None  # El usuario canceló la selección

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remueve los primeros 5 caracteres del nombre de cada archivo .docx y .pdf en una carpeta.")
    
    # Si quieres seguir usando argumentos por línea de comandos:
    # parser.add_argument("ruta", nargs="?", default=None, help="La ruta de la carpeta. Si no se especifica, se usará la GUI.")
    # args = parser.parse_args()

    # Si quieres usar solo la GUI:
    ruta = seleccionar_carpeta()  # <-- Aquí se llama a la función GUI

    if ruta:
        remover_primeros_cinco_caracteres(ruta)
    else:
        print("No se seleccionó ninguna carpeta.")