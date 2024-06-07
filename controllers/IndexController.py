
from PIL import Image
from utils.cargarImg import cargarImagenes
from views.panelVentana import PanelVentana
import customtkinter 


class IndexController:
    def __init__(self, vista):
        self.vista = vista
    

    # Función para cambiar Ventanas  
    def cambiarVentana(self):
        self.vista.Ckframe.destroy()  # Destruye el marco de login
        self.vista.Ckframe = PanelVentana(self.vista)  # Crea un nuevo marco de panel
        self.vista.Ckframe.main()
        self.vista.Ckframe.pack(expand=True, fill='both')  # Em

    
 

    def mostrar_mensaje(self,type,mensaje, posicion):
        typeImg=None
        if type == "error":
            typeImg= cargarImagenes("../img/icon/error.png", "../img/icon/error.png", 20, 20)
        else: 
            typeImg= cargarImagenes("../img/icon/exitoso.png", "../img/icon/exitoso.png", 20, 20)

        if posicion=="top-left":
            x=5
            y=8
        elif posicion=="top-right":
            x=460
            y=8
        elif posicion=="top-center":
            x=250
            y=8

        self.vista.label_errores.configure(text="   "+mensaje, image=typeImg)
        self.vista.label_errores.place(x=x, y=y)
        self.vista.label_errores.lift()
        self.vista.after(2000, self.eliminar_notificacion)

    def eliminar_notificacion(self):
        # Elimina la notificación
        self.vista.label_errores.configure(text="", fg_color="transparent", bg_color="transparent")
        self.vista.label_errores.place_forget() 
