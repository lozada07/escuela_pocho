import customtkinter as ctk
from constantes import constantes as c
from utils.cargarImg import cargarImagenes
from controllers.panelController import PanelController
from views.atletasVentana import AtletasVentana
from views.listaAtletasVentana import ListaAtletasVentana
from utils.animaciones import up, right


class PanelVentana(ctk.CTkFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent):
        super().__init__(parent)

        #Controlador de la vista
        self.controlador = PanelController(self)
        self.mostrar_errores = self.master.controller.mostrar_mensaje
        # Configura el grid dentro del Frame
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=1)
        
        self.padre = self.master
        #Configura el color del Frame
        self.configure(fg_color="transparent")
        
        self.ancho_navbar = 180
        self.ancho_ventana = 800
        self.alto_ventana = 550


        self.contenedor_contenido = ListaAtletasVentana(self)
        self.contenedor_contenido.place(x=self.ancho_navbar, y=self.alto_ventana, relwidth=1 - self.ancho_navbar/self.ancho_ventana, relheight=1)
        self.contenedor_contenido.main()

        
        self.controlador.animacion_up()


 
    def main(self):
        
        # !TODO: MENU
        
        contenedor_menu = ctk.CTkFrame(self, fg_color="#1e293b", width=400)
        contenedor_menu.grid(column=0, row=0, sticky='nsew')
        

        #Logo del menu
        logo_img = cargarImagenes("../img/Logo.png", "../img/Logo.png", 120, 110)
        logo_label = ctk.CTkLabel(master=contenedor_menu, image=logo_img, text="", anchor="center" )
        logo_label.pack(pady=(20,20) ,padx=30)

       
        # Elementos del menu
        elementosMenu= [
            ("Atletas", "../img/MenuIconos/AtletaLight.png", "../img/MenuIconos/AtletaDark.png", 20, 20, self.controlador.cambiar_ventana),
            ("Partidos", "../img/MenuIconos/partidoLight.png", "../img/MenuIconos/partidoDark.png", 18, 18, self.controlador.cambiar_ventana ),
            ("Salir", "../img/MenuIconos/salirLight.png", "../img/MenuIconos/salirDark.png", 18, 18, self.controlador.cambiar_ventana)


        ]
        
        # Carga de los elementos del menu
        for indice, (nombre, imagenLight, imagenDark, ancho, alto, accion) in enumerate(elementosMenu):
            imagenes = cargarImagenes(imagenLight, imagenDark, ancho, alto)
            elemento = ctk.CTkButton(master=contenedor_menu, image=imagenes, fg_color="transparent", hover_color=(c.LIGHT_TEMA,c.DARK_TEMA), corner_radius=4, text=nombre, border_spacing=10, anchor="w", font=('Candara', 17, 'bold'), text_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), command=lambda indice=4 if indice==len(elementosMenu)-1 else indice: accion(indice))
            elemento.pack(fill="both", padx=15 , pady=1, side="top" if nombre!="Salir" else "bottom")


