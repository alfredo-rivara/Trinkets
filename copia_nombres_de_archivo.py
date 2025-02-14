import os
import pyperclip  # Asegúrate de tener esta biblioteca instalada: pip install pyperclip

# Obtener la ruta del directorio actual
carpeta_actual = os.getcwd()

# Obtenemos una lista con los nombres de los archivos en la carpeta actual
nombres_archivos = os.listdir(carpeta_actual)

# Unimos los nombres de los archivos en un solo string, separados por saltos de línea
nombres_archivos_str = '\n'.join(nombres_archivos)

# Copiamos los nombres de los archivos al portapapeles
pyperclip.copy(nombres_archivos_str)

print("Nombres de archivos copiados al portapapeles.")
