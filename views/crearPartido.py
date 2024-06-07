from datetime import datetime
import customtkinter as ctk
from constantes import constantes as c
from controllers.PartidoControlller import PartidoController
from utils.cargarImg import cargarImagenes
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from babel import numbers

class CrearPartidoVentana(ctk.CTkFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent,  partido=None):
        super().__init__(parent)
        
        #Controlador de la vista
        self.controlador = PartidoController(self)
        self.configure(fg_color="transparent" )
        self.partido = partido

        
        self.labels_errores = {
            "equipo_local": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "equipo_visitante": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "fecha_partido": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "hora_partido": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
        }

        # Diccionario para almacenar los framerErrores
        self.frames_campos = {
            "equipo_local": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "equipo_visitante": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "fecha_partido": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "hora_partido": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
        }
 
    def main(self):
        
        partidoImg = cargarImagenes( "../img/editarPartido.png" if self.partido else "../img/crearPartido.png","../img/editarPartido.png" if self.partido else "../img/crearPartido.png" , 550, 140)

        #Imagen de partidos
        ctk.CTkLabel(self,text="", image=partidoImg, anchor="center" ,fg_color="transparent", width=700, height=140).pack(fill="both")
        

        
        # Seleccion de Equipo Local
        equipoLocalImg = cargarImagenes("../img/icon/equipo.png", "../img/icon/equipo.png", 19,19)
        ctk.CTkLabel(self, image=equipoLocalImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30, height=30).place(x=17,y=170)
        self.comboboxEquipoLocal = ctk.CTkComboBox(self, values=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"],
                                             width=200, height=30, min_character_width=46, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0 )
        self.comboboxEquipoLocal.place(x=45, y=170 )
        self.comboboxEquipoLocal.set( self.partido.equipo_local if self.partido else"Equipo Local")
        self.frames_campos["equipo_local"].place(x=17, y=200)
        self.labels_errores["equipo_local"].place(x=17, y=200) 




         # Seleccion de Equipo visitante
        equipoVisitanteImg = cargarImagenes("../img/icon/equipo.png", "../img/icon/equipo.png", 19,17)
        ctk.CTkLabel(self, image=equipoVisitanteImg, text="", fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=264,y=170)
        self.comboboxEquipoVisitante = ctk.CTkComboBox(self, values=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"],
                                             width=200, height=30, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0 )
        self.comboboxEquipoVisitante.place(x=293, y=170 )
        self.comboboxEquipoVisitante.set( self.partido.equipo_visitante if self.partido else "Equipo Visitante")
        self.labels_errores["equipo_visitante"].place(x=264, y=200)
        self.frames_campos["equipo_visitante"].place(x=264, y=200)
        
        #Input y Label de Fecha
        
        styleNuevo = ttk.Style(self)
        styleNuevo.configure('my.DateEntry',  fielbackground=c.DARK_COLOR_SEGUNDARIO, foreground='white')
 


        labelFechaImg = cargarImagenes("../img/icon/edadDark.png", "../img/icon/edadDark.png", 16, 18)
        ctk.CTkLabel(self, image=labelFechaImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30,height=30).place(x=17,y=240)
        
        self.fecha = DateEntry(self, width=22, height=180, background=c.DARK_COLOR_SEGUNDARIO, 
                  borderwidth=2, font=('yu gothic ui', 16, 'bold'), date_pattern="dd/mm/yyyy" ,mindate=datetime.now() )
        
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime('%d/%m/%Y')

        self.fecha.set_date( self.partido.fecha_partido if self.partido else fecha_formateada) 

        self.fecha.place(x=70, y=365)
        self.frames_campos["fecha_partido"].place(x=17, y=270)
        self.labels_errores["fecha_partido"].place(x=17, y=270) 


        


        #Selete y Label de Hora

        labelHoraImg = cargarImagenes("../img/icon/activo.png", "../img/icon/activo.png", 21,21)
        ctk.CTkLabel(self, image=labelHoraImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30,height=30).place(x=264,y=240)
        horas = [f"{i:02}:00" for i in range(8, 19)]
        self.hora= ctk.CTkComboBox(self, values=horas,
                                             width=200, height=30, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0, min_character_width=49 )
        self.hora.place(x=293, y=240)
        self.hora.set( self.partido.hora_partido if self.partido else "Hora")

        self.frames_campos["hora_partido"].place(x=264, y=270)
        self.labels_errores["hora_partido"].place(x=264, y=270) 
       

        #Boton de crear
        ctk.CTkButton(self,  text="Guardar" if self.partido else "Agregar" , fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color="#FFCA0A", height=28, text_color=c.DARK_TEMA, width=140, font=('yu gothic ui', 15, 'bold'),command=self.controlador.registro_partido if self.partido==None else lambda id=self.partido.id: self.controlador.modificar_partido(id)).place(x=355, y=310)

        #Boton de cancelar

        ctk.CTkButton(self, text="Cancelar", fg_color="#B3B3B3", hover_color="#9ca3af", height=28, text_color=c.DARK_TEMA ,width=140, font=('yu gothic ui', 15, 'bold'), command=lambda indice=1: self.master.controlador.cambiar_ventana(indice)).place(x=210, y=310)
        
        #Boton de eliminar
        if self.partido:
            ImgBorrar = cargarImagenes("../img/icon/borrar.png", "../img/icon/borrar.png", 14, 14)
            ctk.CTkButton(self, text="", fg_color="red", image=ImgBorrar, hover_color="red", height=28, text_color=c.DARK_TEMA ,width=10, font=('yu gothic ui', 15, 'bold'), command= lambda id=self.partido.id: self.controlador.eliminar_modal(id) ).place(x=175, y=310)




        #Temporizador
        self.temporizador = None