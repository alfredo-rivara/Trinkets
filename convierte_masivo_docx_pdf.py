import os
import sys
from docx2pdf import convert

def convertir_docx_a_pdf(ruta_carpeta):
  """
  Convierte todos los archivos DOCX de una carpeta a PDF.

  Args:
    ruta_carpeta: La ruta de la carpeta que contiene los archivos DOCX.
  """

  for filename in os.listdir(ruta_carpeta):
    if filename.endswith(".docx"):
      ruta_docx = os.path.join(ruta_carpeta, filename)
      ruta_pdf = os.path.join(ruta_carpeta, filename[:-5] + ".pdf")
      convert(ruta_docx, ruta_pdf)
      print(f"Archivo convertido: {filename}")

if __name__ == "__main__":
  ruta_carpeta = os.getcwd()  # Obtiene la ruta de la carpeta actual
  convertir_docx_a_pdf(ruta_carpeta)
  print("Conversión completada.")