import customtkinter as ctk
from constantes import constantes as c
from controllers.PartidoControlller import PartidoController
from utils.cargarImg import cargarImagenes
from utils.exportar import exportar_partidos_pdf



class PartidosVentana(ctk.CTkFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent):
        super().__init__(parent)
        
        self.controlador= PartidoController(self)    
        self.configure(fg_color="transparent" )
        
        self.todos_partidos= self.controlador.obtener_partidos()

    def main(self):
        
        
        partidoImg = cargarImagenes(  "../img/partidos.png", "../img/partidos.png" , 550, 140)

        #Imagen de partidos
        ctk.CTkLabel(self,text="", image=partidoImg, anchor="center" ,fg_color="transparent", width=700, height=140).pack(fill="both")
        


        #!TODO: Filtros

        cabecera_contenedor = ctk.CTkFrame(self, fg_color="transparent")
        cabecera_contenedor.pack(fill="both", pady=(20, 10),  padx=(10,33) )
        
        #Input de categorias
        self.comboboxCategoria = ctk.CTkComboBox(cabecera_contenedor, values=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"],
                                             width=135, height=28, min_character_width=17, fg_color="#1e293b", button_color=c.DARK_COLOR_SEGUNDARIO, text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", reducir_x=0,  dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0,
                                            command= lambda _: self.controlador.filtros()
                                            )
        self.comboboxCategoria.grid(row=0, column=1, sticky='nsew', padx=(0,5))
        self.comboboxCategoria.set("Categoria")

        ctk.CTkFrame(cabecera_contenedor, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=135).place(x=0, y=30)


      

        
        #Input de Fecha del Juego
        self.comboboxFecha = ctk.CTkComboBox(cabecera_contenedor, values=["Proximo", "Hoy", "En Juego", "Finalizado" ],
                                             width=135, min_character_width=15, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), reducir_x=0, border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0,
                                            command= lambda _: self.controlador.filtros()
                                            )

        self.comboboxFecha.grid(row=0, column=2, sticky='nsew', padx=(0,8))
        self.comboboxFecha.set("Fecha")
        ctk.CTkFrame(cabecera_contenedor, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=135).place(x=140,y=30)


        container_botones=ctk.CTkFrame(cabecera_contenedor,fg_color="transparent")
        container_botones.grid(row=0, column=4, sticky='e', padx=(40, 0), ipadx=10)

        boton_descargar=ctk.CTkButton(container_botones, text="Descargar", width=12, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color="#FFCA0A", height=10, text_color=c.DARK_TEMA , font=('yu gothic ui', 14, 'bold'), command=lambda: exportar_partidos_pdf(self.todos_partidos))
        boton_descargar.configure(cursor="hand2")
        boton_descargar.grid(row=0, column=1, sticky='nsew', padx=(0, 5), ipady=5, ipadx=10)
            
        boton_agregar=ctk.CTkButton(container_botones, text="Agregar", width=12, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color="#FFCA0A", height=10, text_color=c.DARK_TEMA , font=('yu gothic ui', 14, 'bold'), command=lambda:self.master.controlador.cambiar_ventana(3))
        boton_agregar.configure(cursor="hand2")
        boton_agregar.grid(row=0, column=2, sticky='nsew', ipady=5, ipadx=10)
        
    
 

        # !TODO: TARGETA DE PARTIDOS

        #Contenedor    
        self.campos = ctk.CTkFrame(self, fg_color=c.DARK_COLOR_SEGUNDARIO,  corner_radius=10 , height=500)
        self.campos.pack(fill="both", padx=(10,33), pady=(10,0) )
        
        

        #Labels
        ctk.CTkLabel(self.campos, text="FECHA", fg_color=c.DARK_COLOR_SEGUNDARIO, font=('yu gothic ui', 16, 'bold'), text_color="white").place(x=25,y=4)
        ctk.CTkLabel(self.campos, text="EQUIPO", fg_color=c.DARK_COLOR_SEGUNDARIO, font=('yu gothic ui', 16, 'bold'), text_color="white").place(x=210,y=4)
        ctk.CTkLabel(self.campos, text="HORARIO", fg_color=c.DARK_COLOR_SEGUNDARIO, font=('yu gothic ui', 16, 'bold'), text_color="white").place(x=400,y=4)
        
    
        self.cargar_partidos()
      

       

    def cargar_partidos(self):
        self.scrollable_frame = ctk.CTkScrollableFrame(self.campos, fg_color="transparent",  corner_radius=0 , height=400)
        self.scrollable_frame.pack(fill="both", pady=(25,0))
         
        logos={
            "Adulto A": "../img/AdultoA.png",
            "Adulto B": "../img/AdultoB.png",
            "Juvenil A": "../img/JuvenilA.png",
            "Juvenil B": "../img/JuvenilB.png",
            "Infantil A": "../img/InfantilA.png",
            "Infantil B": "../img/InfantilB.png",

        }

        for index, partido in enumerate(self.todos_partidos):                
            
            ImgFondo = cargarImagenes("../img/fondoPartidos.png", "../img/fondoPartidos.png", 500, 80)
            
            # Crea un Canvas como contenedor principal
            self.frame_principal = ctk.CTkCanvas(self.scrollable_frame, width=500, height=80, bg=c.DARK_COLOR_SEGUNDARIO, cursor="hand2")
            self.frame_principal.pack(fill="both", pady=(10 if index==0 else 15,0), expand=True)
            


            # Agrega el Label con la imagen de fondo al Frame
            label_fondo = ctk.CTkLabel(self.frame_principal, image=ImgFondo, text="", corner_radius=10)
            label_fondo.pack(fill="both")

            #Eventos:
            label_fondo.bind("<Button-1>", lambda  event, partido=partido: self.master.controlador.cambiar_ventana(3, partido))


            ctk.CTkLabel(self.frame_principal, text=partido.fecha_partido, fg_color="#001938", font=('yu gothic ui', 14, 'bold'), text_color="#e2e8f0").place(x=23, y=25)

            # Equipo Local
            ImgEquipoLocal = cargarImagenes(logos[partido.equipo_local], logos[partido.equipo_local], 45, 45)
            ctk.CTkLabel(self.frame_principal, text="", fg_color="#001938", image=ImgEquipoLocal).place(x=172,y=20)
            ctk.CTkLabel(self.frame_principal, text=partido.equipo_local, fg_color="#001938", font=('yu gothic ui', 15, 'bold'), text_color="white").place(x=105, y=25)


            #Label VS
            if partido.goles_local or partido.goles_visitante:
                
                ganador=partido.goles_local if partido.goles_local > partido.goles_visitante else partido.goles_visitante

                ctk.CTkLabel(self.frame_principal, text=partido.goles_local ,  fg_color="#001938", font=('yu gothic ui', 15, 'bold'), text_color="white" if ganador != partido.goles_local else c.DARK_TEXT_COLOR).place(x=220, y=25)
                ctk.CTkLabel(self.frame_principal, text=partido.goles_visitante, fg_color="#001938", font=('yu gothic ui', 15, 'bold'), text_color="white"if ganador != partido.goles_visitante else c.DARK_TEXT_COLOR).place(x=252, y=25)

            ctk.CTkLabel(self.frame_principal, text="VS", fg_color="#001938", font=('yu gothic ui', 13, 'bold'), text_color="#e2e8f0").place(x=230, y=25)
            
            # Equipo Visitante
            ImgEquipoVisitante = cargarImagenes(logos[partido.equipo_visitante], logos[partido.equipo_visitante], 50, 50)
            ctk.CTkLabel(self.frame_principal, text="", fg_color="#001938", image=ImgEquipoVisitante).place(x=267,y=15)
            ctk.CTkLabel(self.frame_principal, text=partido.equipo_visitante, fg_color="#001938", font=('yu gothic ui', 15, 'bold'), text_color="white").place(x=322, y=25)




            ctk.CTkLabel(self.frame_principal, text=f"{partido.hora_partido} VZ", fg_color="#001938", font=('yu gothic ui', 14, 'bold'), text_color="#e2e8f0").place(x=402, y=25)
           
    def recargar(self):
        self.scrollable_frame.pack_forget()
        self.after(1, self.cargar_partidos())