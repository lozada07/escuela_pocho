import customtkinter as ctk
from constantes import constantes as c
from controllers.PartidoControlller import PartidoController
from utils.cargarImg import cargarImagenes
from controllers.AtletaController import AtletaController
from utils.exportar import exportar_jugadores_pdf



class ListaAtletasVentana(ctk.CTkFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent):
        super().__init__(parent)


        #Fondo de la ventana
        self.configure(fg_color="transparent" )
        
        #Mostrar mensajes
        self.mostrar_errores= self.master.mostrar_errores 

        #controlador 
        self.controlador=AtletaController(self)        
        
        #Cantidad de registro en las tablas
        self.total_usuarios=self.controlador.cantidad_registros()
        self.total_equipos=6
        self.total_partidos=PartidoController(self).cantidad_registros()


        #Imagenes y cantidad de registors
        self.imgEstadisticas=[
            ("../img/MenuIconos/AtletaDark.png", self.total_usuarios),
            ("../img/MenuIconos/equipoDark.png", self.total_equipos), 
            ("../img/MenuIconos/partidoDark.png", self.total_partidos )
                               ]

        #Obtener todos los usuarios
        self.todos_usuarios = self.controlador.obtener_usuarios()    

    def main(self):

        # !TODO: CABECERA
        cabecera_contenedor = ctk.CTkFrame(self,fg_color="transparent")
        cabecera_contenedor.pack(fill="both", pady=(15, 20) )
        label=ctk.CTkLabel(cabecera_contenedor,text="Listado de Atletas", text_color=c.DARK_TEXT_COLOR, anchor="w", font=('yu gothic ui', 26, 'bold'))
        label.grid(row=0, column=1, sticky='nsew', padx=(10,40))

        container_botones=ctk.CTkFrame(cabecera_contenedor,fg_color="transparent")
        container_botones.grid(row=0, column=3, sticky='e', padx=(0,40))

        boton_descargar=ctk.CTkButton(container_botones, text="Descargar", width=12, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color="#FFCA0A", height=10, text_color=c.DARK_TEMA , font=('yu gothic ui', 14, 'bold'), command=lambda: exportar_jugadores_pdf(self.todos_usuarios))
        boton_descargar.configure(cursor="hand2")
        boton_descargar.grid(row=0, column=1, sticky='nsew', padx=(0, 5), ipady=5, ipadx=10)
            
        boton_agregarAtleta=ctk.CTkButton(container_botones, text="Agregar", width=12, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color="#FFCA0A", height=10, text_color=c.DARK_TEMA , font=('yu gothic ui', 14, 'bold'), command=lambda:self.master.controlador.cambiar_ventana(2))
        boton_agregarAtleta.configure(cursor="hand2")
        boton_agregarAtleta.grid(row=0, column=2, sticky='nsew', ipady=5, ipadx=10)
        
        container_botones.grid_columnconfigure(2, weight=1)
        container_botones.grid_rowconfigure(1, weight=1)


        cabecera_contenedor.grid_columnconfigure(3, weight=1)
        cabecera_contenedor.grid_rowconfigure(1, weight=1)

        
        self.estadisticas_contenedor = ctk.CTkFrame(self, fg_color="transparent")
        self.estadisticas_contenedor.pack(fill="both" )

        for i in range(3): 
            caja = ctk.CTkFrame(self.estadisticas_contenedor, height=100 , fg_color=c.DARK_COLOR_SEGUNDARIO)
            caja.grid(row=0, column=i, sticky='nsew', padx=(10,40 if i == 2 else 10))
            self.estadisticas_contenedor.grid_columnconfigure(i, weight=1)
            self.estadisticas_contenedor.grid_rowconfigure(1, weight=1)
            imagen=self.imgEstadisticas[i][0]
            cantidad=self.imgEstadisticas[i][1]
            

            img=cargarImagenes(imagen, imagen, 40, 40)
            ctk.CTkLabel(caja, text=f"  {cantidad}", image=img, compound="left", anchor="w",  font=('yu gothic ui', 26, 'bold')).pack(pady=15)  # Reemplaza 'icono.png' con la ruta de tu imagen
             




        
        #!TODO: FILTROS
        filtros_contenedor = ctk.CTkFrame(self,fg_color="transparent")
        filtros_contenedor.pack(fill="both", pady=(15, 20), padx=(10,40) )
        

        #Input de buscar
        framer_input = ctk.CTkFrame(filtros_contenedor, fg_color=c.DARK_COLOR_SEGUNDARIO)
        framer_input.grid(row=0, column=1, sticky='nsew', ipadx=5, ipady=2)

        Imginput = cargarImagenes("../img/icon/buscar.png", "../img/icon/buscar.png", 17, 17)

        labelInput = ctk.CTkLabel(framer_input, text=" ", image=Imginput, fg_color=c.DARK_COLOR_SEGUNDARIO)
        labelInput.grid(row=0, column=1, sticky='nsew', padx=(3,0), pady=2)

        self.input = ctk.CTkEntry(framer_input, placeholder_text="Buscar", width=125, border_color=c.DARK_COLOR_SEGUNDARIO, font=('yu gothic ui', 16, 'bold'), placeholder_text_color="white", fg_color=c.DARK_COLOR_SEGUNDARIO, corner_radius=0)
        self.input.grid(row=0, column=2, sticky='nsew', pady=2, padx=(0,3))
        ctk.CTkFrame(filtros_contenedor, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=156).place(x=0,y=31)

        framer_input.grid_columnconfigure(2, weight=1)
        framer_input.grid_rowconfigure(0, weight=1) 


        #Input de categorias
        self.comboboxCategoria = ctk.CTkComboBox(filtros_contenedor, values=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"],
                                             width=135, height=28, min_character_width=17, fg_color="#1e293b", button_color=c.DARK_COLOR_SEGUNDARIO, text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", reducir_x=0,  dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0,
                                            command= lambda _: self.controlador.filtros()
                                            )

        # Supongamos que ya tienes un Combobox llamado comboboxCategoria
        self.comboboxCategoria.grid(row=0, column=2, sticky='nsew', padx=8)
        self.comboboxCategoria.set("Categoria")

        ctk.CTkFrame(filtros_contenedor, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=135).place(x=164, y=31)


        
        #Input de Otros Filtros
        self.comboboxMasFiltros = ctk.CTkComboBox(filtros_contenedor, values=["Masculino", "Femenino"],
                                             width=135, min_character_width=15, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), reducir_x=0, border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0,
                                            command= lambda _: self.controlador.filtros()
                                            )

        self.comboboxMasFiltros.grid(row=0, column=3, sticky='nsew', padx=(0,8))
        self.comboboxMasFiltros.set("Sexo")
        ctk.CTkFrame(filtros_contenedor, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=135).place(x=307,y=31)


        #Boton de buscar 
        ImginputDark = cargarImagenes("../img/icon/buscarDark.png", "../img/icon/buscarDark.png", 18, 18)
        boton_buscar=ctk.CTkButton(filtros_contenedor, image=ImginputDark, fg_color=c.DARK_TEXT_COLOR, hover="#FFCA0A", text="", width=8, command= self.controlador.filtros)
        boton_buscar.grid(row=0, column=4, sticky='nsew')




        filtros_contenedor.grid_columnconfigure(4, weight=1)
        filtros_contenedor.grid_rowconfigure(1, weight=1)
        
        self.card_usuario()



    #!TODO: Usuarios   
    def card_usuario(self):    
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="transparent",  corner_radius=0 , height=400)
        self.scrollable_frame.pack(fill="both", padx=(10,40))
        for usuario in self.todos_usuarios:                
            ImgFondo = cargarImagenes("../img/fondoUsuario1.png", "../img/fondoUsuario1.png", 500, 120)
            ImgAvatar = cargarImagenes("../img/avatar.png", "../img/avatar.png" if usuario.sexo == "Masculino" else "../img/avatar_femenina.png",  90 if usuario.sexo == "Masculino" else 105, 122 if usuario.sexo == "Masculino" else 133)
            # Crea un Frame como contenedor principal
            self.frame_principal = ctk.CTkFrame(self.scrollable_frame, fg_color=c.DARK_TEMA, width=500, height=120)
            self.frame_principal.pack(fill="both", pady=(0,10), expand=True)

            # Agrega el Label con la imagen de fondo al Frame
            label_fondo = ctk.CTkLabel(self.frame_principal, image=ImgFondo, text="")
            label_fondo.pack(fill="both")

            # Agrega el Label con la imagen pequeña y el texto al Frame
            label_pequeño = ctk.CTkLabel(self.frame_principal, text="", fg_color="#F1E751", image=ImgAvatar)
            label_pequeño.place(x=32,y=2 if usuario.sexo == "Masculino" else -6)

            activoImg=cargarImagenes("../img/icon/exitoso.png", "../img/icon/exitoso.png" if usuario.activo == "Activo" else "../img/icon/error.png" , 19,19 )        
            ctk.CTkLabel(self.frame_principal, text=f'{usuario.nombre} {usuario.apellido}', font=('yu gothic ui', 17, 'bold'), text_color="white", fg_color="#001938").place(x=160, y=3)
            ctk.CTkLabel(self.frame_principal, image=activoImg,text="", font=('yu gothic ui', 17, 'bold'), text_color="white", fg_color="#001938").place(x=370, y=4)
            ctk.CTkLabel(self.frame_principal, text=usuario.posicion, font=('yu gothic ui', 13, 'bold'), text_color="#d1d5db",  fg_color="#001938").place(x=160, y=28)
            ctk.CTkLabel(self.frame_principal, text="<--->", font=('yu gothic ui', 13, 'bold'), text_color=c.DARK_TEXT_COLOR,  fg_color="#001938").place(x=222 if usuario.rol=="Jugador" else 255, y=28)
            ctk.CTkLabel(self.frame_principal, text=usuario.rol, font=('yu gothic ui', 13, 'bold'), text_color="#d1d5db",  fg_color="#001938").place(x=260 if usuario.rol=="Jugador" else 293, y=28)
            

            ImgActualizar = cargarImagenes("../img/icon/actualizar.png", "../img/icon/actualizar.png", 14, 14)
            boton_editar=ctk.CTkButton(self.frame_principal, image=ImgActualizar, fg_color=c.DARK_TEXT_COLOR, text="", width=10,hover_color="#FFCA0A", command=lambda usuario=usuario:self.master.controlador.cambiar_ventana(2, usuario))
            boton_editar.configure(cursor="hand2")
            
            boton_editar.place(x=435, y=7)


            ImgBorrar = cargarImagenes("../img/icon/borrar.png", "../img/icon/borrar.png", 14, 14)
            boton_eliminar=ctk.CTkButton(self.frame_principal, image=ImgBorrar, fg_color=c.DARK_TEXT_COLOR, text="", width=10,hover_color="red", command= lambda usuario_id=usuario.id, framer_id=self.frame_principal.winfo_id(): self.controlador.eliminar_modal(usuario_id, framer_id))
            boton_eliminar.configure(cursor="hand2")
            boton_eliminar.place(x=400, y=7)

        

            atleta_estadisticas = ctk.CTkFrame(self.frame_principal, fg_color="#001938", width=270, height=40)
            atleta_estadisticas.place(x=160, y=65)

            lista = [
                ("Partidos", 12, usuario.partidos or 0),
                ("Goles", 17, usuario.goles or 0),
                ("Rojas", 17, usuario.targetas_rojas or 0),
                ("Amarillas", 12, usuario.targetas_amarillas or 0),
                ]

            # Configura el framer para tener 4 columnas
            for i in range(4):
                nombre, x, numero = lista[i]  
                container_atleta_estadisticas = ctk.CTkFrame(atleta_estadisticas, fg_color=c.DARK_COLOR_SEGUNDARIO, width=65, height=50)
                container_atleta_estadisticas.grid(row=0, column=i, sticky='nsew', padx=2)  # Cambia 'nsew' a 'ew'

                ctk.CTkLabel(container_atleta_estadisticas, text=nombre, font=('yu gothic ui', 11, 'bold'), text_color="#d1d5db",  fg_color=c.DARK_COLOR_SEGUNDARIO).place(x=x, y=-2)

                ctk.CTkLabel(container_atleta_estadisticas, text=numero, font=('yu gothic ui', 16, 'bold'), text_color="white",  fg_color=c.DARK_COLOR_SEGUNDARIO).place(x=24, y=18)

                atleta_estadisticas.grid_columnconfigure(i, weight=1)

    def recargar(self):
        self.scrollable_frame.pack_forget()
        self.after(1,self.card_usuario())