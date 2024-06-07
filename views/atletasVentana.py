import customtkinter as ctk
from constantes import constantes as c
from utils.FloatSpinbox import FloatSpinbox
from utils.cargarImg import cargarImagenes

from controllers.AtletaController import AtletaController

class AtletasVentana(ctk.CTkFrame):  # Usa ctk.CTkFrame en lugar de ttk.Frame
    def __init__(self, parent, user=None):
        super().__init__(parent)
        self.user = user
        #Controlador de la vista
        self.controlador = AtletaController(self)
        self.configure(fg_color="transparent" )
        
        # Diccionario para almacenar los labels de los errores
        self.labels_errores = {
            "nombre": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "apellido": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "direccion": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "telefono": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "rol": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "categoria": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "edad": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "sexo": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "posicion": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "activo": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "targetas_rojas": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "targetas_amarillas": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "goles": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),
            "partidos": ctk.CTkLabel(self, text="" , font=('yu gothic ui', 12, 'bold'), text_color="red"),



        }
        # Diccionario para almacenar los framerErrores
        self.frames_campos = {
            "nombre": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "apellido": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "direccion": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "telefono": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "rol": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=228),
            "categoria": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),
            "edad": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),
            "sexo": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),        
            "posicion": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),        
            "activo": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),    
            "targetas_rojas": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),    
            "targetas_amarillas": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),        
            "goles": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),        
            "partidos": ctk.CTkFrame(self, height=3, fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), width=230),          
        }

        self.isAtleta=False
        if self.user:
            if self.user.rol == "Jugador":
                self.isAtleta=True

    def main(self):
        
        # !TODO: MENU

        registroImg = cargarImagenes("../img/actualizar.png" if self.user else "../img/registro.png", "../img/actualizar.png" if self.user else "../img/registro.png"    , 550, 120)

        #Imagen de registro
        ctk.CTkLabel(self,text="", image=registroImg, anchor="center" ,fg_color="transparent", width=700, height=120).pack(fill="both")
        
        #Input y Label de nombre
        labelNombreImg = cargarImagenes("../img/icon/nombreLight.png", "../img/icon/nombreDark.png", 19, 19)

        ctk.CTkLabel(self, image=labelNombreImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30, corner_radius=0).place(x=17,y=130)
        self.nombre=ctk.CTkEntry(self, border_width=0, placeholder_text="Nombre",   textvariable=ctk.StringVar(value=self.user.nombre if self.user else "") if self.user else "", font=('yu gothic ui', 16, 'bold'), height=28, corner_radius=0, fg_color=("#cbd5e1","#1e293b" )  , placeholder_text_color=("black","white"),width=200)
        self.nombre.place(x=45, y=130) #-40
        self.frames_campos["nombre"].place(x=17, y=158) #-40
        self.labels_errores["nombre"].place(x=17, y=158) 
        

        #Input y Label de Apellido
        labelApellidoImg = cargarImagenes("../img/icon/apellidoLight.png", "../img/icon/apellidoDark.png", 19, 19)

        ctk.CTkLabel(self, image=labelApellidoImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=265,y=130 )
        self.apellido=ctk.CTkEntry(self, border_width=0, placeholder_text="Apellido", textvariable=ctk.StringVar(value=self.user.apellido if self.user else "") if self.user else "" , font=('yu gothic ui', 16, 'bold'), corner_radius=0, fg_color=("#cbd5e1","#1e293b" ), placeholder_text_color=("black","white"), height=28, width=200)
        self.apellido.place(x=293, y=130)
        self.frames_campos["apellido"].place(x=266, y=158)
        self.labels_errores["apellido"].place(x=266, y=158)
        
         
        #Input y Label de dirección
        
        labelDireccionImg = cargarImagenes("../img/icon/direccionLight.png", "../img/icon/direccionDark.png", 16, 18)
        
        ctk.CTkLabel(self, image=labelDireccionImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=17,y=185)
        self.direccion=ctk.CTkEntry(self, border_width=0, placeholder_text="Direccion", textvariable=ctk.StringVar(value=self.user.direccion if self.user else "") if self.user else "", height=28, font=('yu gothic ui', 16, 'bold'), corner_radius=0, fg_color=("#cbd5e1","#1e293b" ), placeholder_text_color=("black","white"), width=200)
        self.direccion.place(x=45, y=185)
        self.frames_campos["direccion"].place(x=17, y=213)
        self.labels_errores["direccion"].place(x=17, y=213) 
        

        #Input y Label de telefono
        labelTelefonoImg = cargarImagenes("../img/icon/telefonoLight.png", "../img/icon/telefonoDark.png", 17, 17)

        ctk.CTkLabel(self, image=labelTelefonoImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=265,y=185 )
        self.telefono=ctk.CTkEntry(self, border_width=0, placeholder_text="Telefono", textvariable=ctk.StringVar(value=self.user.telefono if self.user else "") if self.user else "",height=28, font=('yu gothic ui', 16, 'bold'), corner_radius=0, fg_color=("#cbd5e1","#1e293b" ), placeholder_text_color=("black","white"), width=200 )
        self.telefono.place(x=293, y=185)
        self.frames_campos["telefono"].place(x=265, y=213)
        self.labels_errores["telefono"].place(x=265, y=213) 

        # Seleccion de Rol
        RolImg = cargarImagenes("../img/icon/rol.png", "../img/icon/rol.png", 18,19)
        ctk.CTkLabel(self, image=RolImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=17,y=240)
        self.comboboxRol = ctk.CTkComboBox(self, values=["Jugador", "Equipo Tecnico"],
                                             width=200, height=28, min_character_width=42, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0, command= lambda e: self.controlador.mas_campos(e) )
        self.comboboxRol.place(x=45, y=240 )
        self.comboboxRol.set(self.user.rol if self.user else "Rol")
        self.frames_campos["rol"].place(x=17, y=268)
        self.labels_errores["rol"].place(x=17, y=268) 
       
       
        # Seleccion de Categoria
        RolImg = cargarImagenes("../img/icon/categoria.png", "../img/icon/categoria.png", 19,19)
        ctk.CTkLabel(self, image=RolImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=264,y=240)
        self.comboboxCategoria = ctk.CTkComboBox(self, values=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"],
                                             width=200, height=28, min_character_width=47, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0 )
        self.comboboxCategoria.place(x=293, y=240 )
        self.comboboxCategoria.set(self.user.categoria if self.user else "Categoria")
        self.frames_campos["categoria"].place(x=264, y=268)
        self.labels_errores["categoria"].place(x=264, y=268) 
       

        #Input y Label de Edad
        labelEdadImg = cargarImagenes("../img/icon/edadLight.png", "../img/icon/edadDark.png", 17, 17)

        ctk.CTkLabel(self, image=labelEdadImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=28).place(x=17,y=295)
        self.edad = FloatSpinbox(self, width=200, step_size=1, value=self.user.edad if self.user else 0, name="Edad", command=self.controlador.verificar_edad)
        self.edad.place(x=45, y=295 )
        self.frames_campos["edad"].place(x=17, y=324)
        self.labels_errores["edad"].place(x=17, y=324) 
       

        
        # Seleccion de Genero
        generoImg = cargarImagenes("../img/icon/genero.png", "../img/icon/genero.png", 19,17)
        ctk.CTkLabel(self, image=generoImg, text="", fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=264,y=295)
        self.comboboxGenero = ctk.CTkComboBox(self, values=["Masculino", "Femenino"],
                                             width=200, fg_color="#1e293b", button_color="#1e293b", text_color="white",
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0 )
        self.comboboxGenero.place(x=293, y=295 )
        self.comboboxGenero.set(self.user.sexo if self.user else "Genero")
        
        self.frames_campos["sexo"].place(x=264, y=324)
        self.labels_errores["sexo"].place(x=264, y=324)

       

        
        # Seleccion de Posicion
        posicionImg = cargarImagenes("../img/icon/posicion.png", "../img/icon/posicion.png", 21,21)
        ctk.CTkLabel(self, image=posicionImg, text="", fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=17,y=350)
        self.comboboxPosicion = ctk.CTkComboBox(self, values= (["Delantero", "Medio", "Portero", "Defensa"] if self.user.rol == "Jugador" else ["Director tecnico", "Auxiliar tecnico", "Preparador fisico", "Psicólogo deportivo", "Médico"])  if self.user else [],
                                             width=200, fg_color="#1e293b", button_color="#1e293b", text_color="white", min_character_width=46,
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0, state="readonly" )
        self.comboboxPosicion.place(x=45, y=350 )
        self.comboboxPosicion.set(self.user.posicion if self.user else "Posicion")
        self.frames_campos["posicion"].place(x=17, y=378)
        self.labels_errores["posicion"].place(x=17, y=378) 

        # Seleccion de activo
        activoImg = cargarImagenes("../img/icon/activo.png", "../img/icon/activo.png", 21,21)
        ctk.CTkLabel(self, image=activoImg, text="", fg_color=("#cbd5e1","#1e293b" ), width=30).place(x=264,y=350)
        self.comboboxActivo = ctk.CTkComboBox(self, values=["Activo", "Inactivo"],
                                             width=200, fg_color="#1e293b", button_color="#1e293b", text_color="white", min_character_width=49,
                                            hover=False,  font=('yu gothic ui', 16, 'bold'), border_color="#1e293b", dropdown_fg_color="#1e293b",  dropdown_hover_color=c.DARK_TEMA, corner_radius=0 )
        self.comboboxActivo.place(x=293, y=350 )      
        self.comboboxActivo.set( ("Inactivo" if self.user.activo=='Inactivo' else "Activo") if self.user else "Estado")
        self.frames_campos["activo"].place(x=264, y=378)
        self.labels_errores["activo"].place(x=264, y=378) 
    

        #Campos atletas
    
        self.campos_atletas()


         
        #Boton de registro
        ctk.CTkButton(self, text="Guardar" if self.user else "Agregar", fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR), hover_color="#FFCA0A", height=28, text_color=c.DARK_TEMA, width=100, font=('yu gothic ui', 15, 'bold'), command=self.controlador.registro if self.user==None else lambda id=self.user.id: self.controlador.modificar(id) ).place(x=395, y=515)

        #Boton de cancelar
        ctk.CTkButton(self, text="Cancelar", fg_color="#B3B3B3", hover_color="#9ca3af", height=28, text_color=c.DARK_TEMA ,width=100, font=('yu gothic ui', 15, 'bold'), command=lambda indice=0: self.master.controlador.cambiar_ventana(indice)).place(x=290, y=515)

        self.temporizador = None
    

    def campos_atletas(self):
        if(self.isAtleta):
            
            #Input y Label de Targetas rojas
            labelETargetasRoajasImg = cargarImagenes("../img/icon/targetasRojas.png", "../img/icon/targetasRojas.png", 21, 21)

            self.labelTargetasRojas = ctk.CTkFrame(self, fg_color="transparent" )
            self.labelTargetasRojas.place(x=17, y=405)
            ctk.CTkLabel(master=self.labelTargetasRojas, image=labelETargetasRoajasImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=28).pack()
            self.targetas_rojas = FloatSpinbox(self, width=200, step_size=1, value=self.user.targetas_rojas or 0 if self.user else 0, name="Targetas Rojas")
            self.targetas_rojas.place(x=45, y=405 )
            self.frames_campos["targetas_rojas"].place(x=17, y=434)
            self.labels_errores["targetas_rojas"].place(x=17, y=434) 

            #Input y Label de Targetas amarillas
            labelETargetasAmarillasImg = cargarImagenes("../img/icon/targetasAmarillas.png", "../img/icon/targetasAmarillas.png", 21, 21)
            
            self.labelTargetasAmarillas = ctk.CTkFrame(self, fg_color="transparent" )
            self.labelTargetasAmarillas.place(x=264,y=405)


            ctk.CTkLabel(self.labelTargetasAmarillas, image=labelETargetasAmarillasImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).pack()
            self.targetas_amarillas = FloatSpinbox(self, width=200, step_size=1, value=self.user.targetas_amarillas or 0  if self.user else 0, name="Targetas Amarrilas")
            self.targetas_amarillas.place(x=293, y=405 )
            self.frames_campos["targetas_amarillas"].place(x=264, y=434)
            self.labels_errores["targetas_amarillas"].place(x=264, y=434) 


            #Input y Label de Goles
            labelGolesImg = cargarImagenes("../img/icon/goles.png", "../img/icon/goles.png", 21, 21)

            self.labelGoles = ctk.CTkFrame(self, fg_color="transparent" )
            self.labelGoles.place(x=17,y=460)
            
            ctk.CTkLabel(self.labelGoles, image=labelGolesImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=28).pack()
            self.goles = FloatSpinbox(self, width=200, step_size=1, value=self.user.goles or 0  if self.user else 0, name="Goles")
            self.goles.place(x=45, y=460 )
            self.frames_campos["goles"].place(x=17, y=487)
            self.labels_errores["goles"].place(x=17, y=487) 

            #Input y Label de Partidos
            labelPartidosImg = cargarImagenes("../img/icon/partido.png", "../img/icon/partido.png", 21, 21)

            self.labelPartidos = ctk.CTkFrame(self, fg_color="transparent" )
            self.labelPartidos.place(x=264,y=460)

            ctk.CTkLabel(self.labelPartidos, image=labelPartidosImg, text="" , fg_color=("#cbd5e1","#1e293b" ), width=30).pack()
            self.partidos = FloatSpinbox(self, width=200, step_size=1, value=self.user.partidos or 0  if self.user else 0,name="Partidos")
            self.partidos.place(x=293, y=460 )
            self.frames_campos["partidos"].place(x=264, y=487)
            self.labels_errores["partidos"].place(x=264, y=487)
       


