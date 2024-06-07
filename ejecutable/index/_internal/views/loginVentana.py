from PIL import Image
import customtkinter as ctk
from constantes import constantes as c
from controllers.AuthController import AuthController
from utils.cargarImg import cargarImagenes


class LoginVentana(ctk.CTkFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent):
        super().__init__(parent)
        
        #Controlador de la vista
        self.controlador = AuthController(self)
        
        # Configura el grid dentro del Frame
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        self.configure(fg_color="transparent")

        self.login_frame = ctk.CTkFrame( master=self, border_width=0, fg_color="transparent")  # Usa ctk.CTkFrame en lugar de ttk.Frame

        self.labels_errores = {
                "usuario": ctk.CTkLabel(self.login_frame, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
                "contraseña": ctk.CTkLabel(self.login_frame, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
        }

            # Diccionario para almacenar los framerErrores
        self.frames_campos = {
                "usuario":ctk.CTkFrame(self.login_frame, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR)),
                "contraseña":ctk.CTkFrame(self.login_frame, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR)),
           
        }


   
    
    def main(self):
        
        #Imagen del logo
        my_image = cargarImagenes("../img/Login.jpg", "../img/Login.jpg", 325, 550)
        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.grid(column=0, row=0, sticky='nsew')

        # !TODO: FORMULARIO DE INICIO DE SECCIÓN

        self.login_frame.grid(column=1, row=0, sticky='nsew', padx=25,  )
        
      
        
        ctk.CTkButton(self.login_frame, text="", width=5, hover=False, fg_color="transparent" ).pack(pady=(15,20), padx=(283,0) )

        ctk.CTkLabel(self.login_frame, text="Escuela Pocho Echenausi", font=('yu gothic ui', 28, 'bold'),  text_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), anchor="w").pack( fill='both')
        ctk.CTkLabel(self.login_frame, text="Inicia sesión en tu cuenta", font=('yu gothic ui', 13, 'bold'), text_color=("#1e293b","white") , anchor="w").pack(pady=(4, 20), fill='both')



        #Input de usuario

        labelUsuarioImg = cargarImagenes("../img/icon/usuarioIconLight.png", "../img/icon/usuarioIconDark.png", 20, 20)
        
        # !Todo Primer Ejemplo
        # ctk.CTkLabel(self.login_frame,image=labelUsuarioImg, text="  Usuario:", text_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), font=('yu gothic ui', 16, 'bold'), anchor="w", compound="left" ).pack(pady=5, fill='both')
        # self.usuario=ctk.CTkEntry(self.login_frame, width=320, border_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), fg_color=(c.LIGHT_TEMA, c.DARK_TEMA),)
        # self.usuario.pack(ipady=4,   fill='both')
        
        #!TODO Segundo Ejemplo
      
        ctk.CTkLabel(self.login_frame, image=labelUsuarioImg, text="").place(x=0,y=190)
        self.usuario=ctk.CTkEntry(self.login_frame, border_width=0, placeholder_text="Usuario", font=('yu gothic ui', 16, 'bold'),  placeholder_text_color=("black","white"), fg_color=(c.LIGHT_TEMA, c.DARK_TEMA))
        self.usuario.place_configure(x=32, y=285, relwidth=0.95)
        self.frames_campos["usuario"].pack(fill="both", pady=(65, 0))
        self.labels_errores["usuario"].place_configure(x=0, y=330)
        # ctk.CTkFrame(self.login_frame, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR)).pack(fill="both", pady=(65, 0), )


        # Input Contraseña    
       
        labelContraseñaImg = cargarImagenes("../img/icon/contraseñaIconLight.png", "../img/icon/contraseñaIconDark.png", 19, 19)
        
        # !TODO: primer ejemplo
        # ctk.CTkLabel(self.login_frame,image=labelContraseñaImg, text="  Contraseña:", text_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), font=('yu gothic ui', 16, 'bold'), anchor="w", compound="left" ).pack(pady=(30, 5), fill='both')
        # self.contraseña=ctk.CTkEntry(self.login_frame, border_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), show="*",  fg_color=(c.LIGHT_TEMA, c.DARK_TEMA),)
        # self.contraseña.pack(ipady=4,  fill='both')

        # !TODO: segundo ejemplo 
        ctk.CTkLabel(self.login_frame, image=labelContraseñaImg, text="").place(x=0,y=265)
        self.contraseña=ctk.CTkEntry(self.login_frame, border_width=0, placeholder_text="Contraseña", font=('yu gothic ui', 16, 'bold'), placeholder_text_color=("black","white"), fg_color=(c.LIGHT_TEMA, c.DARK_TEMA), show="*")
        self.contraseña.place_configure(x=32, y=400, relwidth=0.95)
        self.frames_campos["contraseña"].pack(fill="both", pady=(75, 0))
        self.labels_errores["contraseña"].place_configure(x=0, y=450 )



        #Boton de inicio de sesición
        ctk.CTkButton(self.login_frame, text="Iniciar sesión", height=37, text_color=("#fff", "black"),  fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color=("#20215C", "#FFCA0A"), font=('yu gothic ui', 16, 'bold'), command=self.controlador.login ).pack(pady=40, fill='both')
        
        #Temporizador
        self.temporizador = None