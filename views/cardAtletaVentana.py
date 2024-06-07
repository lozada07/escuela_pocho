from PIL import Image
import customtkinter as ctk
from constantes import constantes as c
from utils.buscarImg import buscarImg
from utils.cargarImg import cargarImagenes



class PartidosVentana(ctk.CTkScrollableFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent):
        super().__init__(parent)
        
       
        self.configure(fg_color="transparent",  corner_radius=0 , height=400 )
        self.pack(fill="both", padx=(10,40))
 
    def main(self):
        
        for usuario in self.master.todos_usuarios:                
            ImgFondo = cargarImagenes("../img/fondoUsuario1.png", "../img/fondoUsuario1.png", 500, 120)
            ImgAvatar = cargarImagenes("../img/avatar.png", "../img/avatar.png", 90, 122)
            # Crea un Frame como contenedor principal
            self.master.frame_principal = ctk.CTkFrame(self, fg_color=c.DARK_TEMA, width=500, height=120)
            self.master.frame_principal.pack(fill="both", pady=(0,10), expand=True)

            # Agrega el Label con la imagen de fondo al Frame
            label_fondo = ctk.CTkLabel(self.master.frame_principal, image=ImgFondo, text="")
            label_fondo.pack(fill="both")

            # Agrega el Label con la imagen pequeña y el texto al Frame
            label_pequeño = ctk.CTkLabel(self.frame_principal, text="", fg_color="#F1E751", image=ImgAvatar)
            label_pequeño.place(x=32,y=2)
                    
            ctk.CTkLabel(self.frame_principal, text=f'{usuario.nombre} {usuario.apellido}', font=('yu gothic ui', 17, 'bold'), text_color="white", fg_color="#001938").place(x=160, y=3)
            ctk.CTkLabel(self.frame_principal, text="Portero", font=('yu gothic ui', 13, 'bold'), text_color="#d1d5db",  fg_color="#001938").place(x=160, y=25)
            
            ImgActualizar = cargarImagenes("../img/icon/actualizar.png", "../img/icon/actualizar.png", 14, 14)
            boton_editar=ctk.CTkButton(self.frame_principal, image=ImgActualizar, fg_color=c.DARK_TEXT_COLOR, text="", width=10,hover_color="#FFCA0A", command=lambda usuario=usuario:self.master.controlador.cambiar_ventana(4, usuario))
            boton_editar.configure(cursor="hand2")
            
            boton_editar.place(x=435, y=7)


            ImgBorrar = cargarImagenes("../img/icon/borrar.png", "../img/icon/borrar.png", 14, 14)
            boton_eliminar=ctk.CTkButton(self.frame_principal, image=ImgBorrar, fg_color=c.DARK_TEXT_COLOR, text="", width=10,hover_color="red", command= lambda usuario_id=usuario.id, framer_id=self.frame_principal.winfo_id(): self.controlador.eliminar_modal(usuario_id, framer_id))
            boton_eliminar.configure(cursor="hand2")
            boton_eliminar.place(x=400, y=7)

        

            atleta_estadisticas = ctk.CTkFrame(self.frame_principal, fg_color="#001938", width=270, height=40)
            atleta_estadisticas.place(x=160, y=65)

            lista = [
                ("Partidos", 12, "12"),
                ("Goles", 17, "12"),
                ("Rojas", 17, "12"),
                ("Amarillas", 12, "12"),
                ]

            # Configura el framer para tener 4 columnas
            for i in range(4):
                nombre, x, numero = lista[i]  
                container_atleta_estadisticas = ctk.CTkFrame(atleta_estadisticas, fg_color=c.DARK_COLOR_SEGUNDARIO, width=65, height=50)
                container_atleta_estadisticas.grid(row=0, column=i, sticky='nsew', padx=2)  # Cambia 'nsew' a 'ew'

                ctk.CTkLabel(container_atleta_estadisticas, text=nombre, font=('yu gothic ui', 11, 'bold'), text_color="#d1d5db",  fg_color=c.DARK_COLOR_SEGUNDARIO).place(x=x, y=-2)

                ctk.CTkLabel(container_atleta_estadisticas, text="12", font=('yu gothic ui', 16, 'bold'), text_color="white",  fg_color=c.DARK_COLOR_SEGUNDARIO).place(x=24, y=18)

                atleta_estadisticas.grid_columnconfigure(i, weight=1)
