from rich import print
from rich.console import Console
from rich.spinner import Spinner
from time import sleep

console = Console()

def menu():
    print("[bold red]ArtefactosParaTexto[/]")
    print("v.0.1")
    print("Programa con utilidades para el manejo masivo de archivos basado en Python en español latino.")
    print("")
    print("[1] Agrega prefijos a todos los nombres de archivos de una carpeta desde un archivo .CSV")
    print("[2] Convierte todos los archivos .DOCX de una carpeta a .PDF")
    print("[3] Copia los nombres de todos los archivos de una carpeta al portapapeles.")
    print("[4] Elimina prefijos a todos los archivos de una carpeta.")
    print("[5] Mueve los archivos de un grupo de subcarpetas a su raíz y elimina las carpetas vacías.")
    print("[0] Salir.")
    print("")
    while True:
        opcion = input("Selecciona un programa para continuar [1/2/3/4/5/0]:")
        if opcion in ("1", "2", "3", "4", "5", "0"):
            return opcion
        else:
            print("Error al escoger. Vuelva a intentarlo.")

def cargar_programa(opcion):
  with console.status("[bold green]Cargando...", spinner="dots"): # Pasamos el NOMBRE del spinner
    sleep(2)  # Simula un proceso de carga

    if opcion == "1":
        print("Cargando [1]")
        import agrega_prefijos
    elif opcion == "2":
        print("Cargando [2]")
        import convierte_masivo_docx_pdf
    elif opcion == "3":
        print("Cargando [3]")
        import copia_nombres_de_archivo
    elif opcion == "4":
        print("Cargando [4]")
        import elimina_prefijos
    elif opcion == "5":
        print("Cargando [5]")
        import extractor
    elif opcion == "0":
        print("Hasta pronto.")
        exit()

opcion = menu()
cargar_programa(opcion)