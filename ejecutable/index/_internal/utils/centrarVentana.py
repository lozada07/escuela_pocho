
def centrar_ventana(ventana,ancho,alto):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_alto = ventana.winfo_screenheight()

    x = int((pantall_ancho/3))
    y = int((pantall_alto/2) - (alto/2))

    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


