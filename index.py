import os
from controllers.IndexController import IndexController
from utils.centrarVentana import centrar_ventana
import customtkinter 
from views.loginVentana import LoginVentana
from constantes import  constantes as c
from utils.db import ConectarDb


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Fundación Escuela de Fútbol El Pocho Echenausi')

        #Conexión a la base de datos
        self.db = ConectarDb()
        self.db.conectar_db()

        self.controller= IndexController(self)

        #Aparaciencia
        customtkinter.set_appearance_mode("dark")      
        self.tema= customtkinter.get_appearance_mode()
    
        # Cambio de Icono de la pantalla  
        dir_path = os.path.dirname(os.path.realpath(__file__))
        icon_path = os.path.join(dir_path, "img", "Logo.ico")
        self.iconbitmap(icon_path)


        # Centrar la ventana
        centrar_ventana(self, ancho=700, alto=550)
        
        # Hace que la ventana no se pueda expandir
        self.resizable(False, False)
        #Colores por defecto dependiendo del tema
        self.configure(fg_color=(c.LIGHT_TEMA, c.DARK_TEMA ))
    
        #Label para mostrar notificaciones
        self.label_errores = customtkinter.CTkLabel(self, text="", fg_color=c.DARK_COLOR_SEGUNDARIO, bg_color=c.DARK_COLOR_SEGUNDARIO, height=40,  width=200, compound="left", corner_radius=10)

        self.Ckframe = LoginVentana(self)
        self.Ckframe.main()
        self.Ckframe.pack(expand=True, fill='both')
        
        self.mainloop()


    



app = App()


