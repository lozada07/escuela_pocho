from PIL import Image
import customtkinter as ctk
from utils.buscarImg import buscarImg

def cargarImagenes(imagenLight, imagenDark, ancho, alto):
     return ctk.CTkImage(light_image=Image.open(buscarImg(imagenLight)),
                        dark_image=Image.open(buscarImg(imagenDark)),
                        size=(ancho, alto) )