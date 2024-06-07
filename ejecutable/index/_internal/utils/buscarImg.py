import os


def buscarImg(ruta):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logo_path = os.path.join(dir_path, ruta)
    return logo_path
