import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_carpeta():
  """Abre un cuadro de diálogo para seleccionar una carpeta."""
  global carpeta_origen
  carpeta_origen = filedialog.askdirectory()
  if carpeta_origen:
    etiqueta_ruta.config(text=carpeta_origen)

def procesar_carpetas():
  """Procesa las subcarpetas de la carpeta origen."""
  for nombre_subcarpeta in os.listdir(carpeta_origen):
    ruta_subcarpeta = os.path.join(carpeta_origen, nombre_subcarpeta)
    if os.path.isdir(ruta_subcarpeta):
      mover_archivos(ruta_subcarpeta)
  eliminar_carpetas_vacias()
  messagebox.showinfo("Proceso completado", "Se han movido los archivos y eliminado las carpetas vacías.")

def mover_archivos(ruta_subcarpeta):
  """Mueve los archivos de una subcarpeta a la carpeta origen, renombrando los duplicados."""
  for nombre_archivo in os.listdir(ruta_subcarpeta):
    ruta_archivo = os.path.join(ruta_subcarpeta, nombre_archivo)
    if os.path.isfile(ruta_archivo):
      nombre_archivo_destino = nombre_archivo
      contador = 1
      while os.path.exists(os.path.join(carpeta_origen, nombre_archivo_destino)):
        nombre, extension = os.path.splitext(nombre_archivo)
        nombre_archivo_destino = f"{nombre}_{contador}{extension}"
        contador += 1
      shutil.move(ruta_archivo, os.path.join(carpeta_origen, nombre_archivo_destino))

def eliminar_carpetas_vacias():
  """Elimina las subcarpetas vacías de la carpeta origen."""
  for nombre_subcarpeta in os.listdir(carpeta_origen):
    ruta_subcarpeta = os.path.join(carpeta_origen, nombre_subcarpeta)
    if os.path.isdir(ruta_subcarpeta) and not os.listdir(ruta_subcarpeta):
      os.rmdir(ruta_subcarpeta)

def salir():
  """Cierra la aplicación."""
  ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mover archivos y eliminar carpetas vacías")

# Botón para seleccionar la carpeta
boton_seleccionar = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta)
boton_seleccionar.pack(pady=10)
boton_seleccionar.bind("<Enter>", lambda event: boton_seleccionar.config(text="Abrir explorador"))
boton_seleccionar.bind("<Leave>", lambda event: boton_seleccionar.config(text="Seleccionar carpeta"))

# Etiqueta para mostrar la ruta de la carpeta seleccionada
etiqueta_ruta = tk.Label(ventana, text="Carpeta no seleccionada")
etiqueta_ruta.pack()

# Botón para procesar las carpetas
boton_procesar = tk.Button(ventana, text="Procesar carpetas", command=procesar_carpetas)
boton_procesar.pack(pady=10)
boton_procesar.bind("<Enter>", lambda event: boton_procesar.config(text="Iniciar proceso"))
boton_procesar.bind("<Leave>", lambda event: boton_procesar.config(text="Procesar carpetas"))

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=10)
boton_salir.bind("<Enter>", lambda event: boton_salir.config(text="Cerrar programa"))
boton_salir.bind("<Leave>", lambda event: boton_salir.config(text="Salir"))

ventana.mainloop()