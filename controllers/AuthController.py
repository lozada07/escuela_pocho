
# from models.usuario import Usuario
from constantes import constantes as c
from CTkMessagebox import CTkMessagebox
from sqlalchemy.orm import Session
from models.usuarioModelo import Usuario
from utils.db import ConectarDb

class AuthController:
    def __init__(self, vista):
        self.vista = vista


    def login(self):
        campos= {
            "usuario" : self.vista.usuario.get(),
            "contraseña" : self.vista.contraseña.get()
        }

        errores = [self.validar_campo(campo, valor) for campo, valor in campos.items()]
        errores = [error for error in errores if error is not None]  # Filtra los errores

        if errores:
            # Enviar los errores a la vista
            self.mostrar_errores(errores)
        else:    
            session = Session(bind=ConectarDb().engine)
            # Obtener el usuario a eliminar
            usuario = session.query(Usuario).filter(Usuario.nombre == campos["usuario"]).first()


            # Comprueba si el usuario existe
            if usuario is not None and usuario.rol=="Administrador" and usuario.contraseña == campos["contraseña"]:
                self.vista.master.controller.cambiarVentana()  # Cambia de ventana

            else: 
                CTkMessagebox(title="Error", message="Usuario o contraseña incorrectos", text_color="white", font=('yu gothic ui', 15, 'bold'), border_color="blue", icon="cancel", button_color=c.DARK_TEXT_COLOR, button_hover_color="#FFDB59", button_text_color=c.DARK_TEMA, title_color=c.DARK_TEXT_COLOR)

     #Validar campos del formulario
    def validar_campo(self, campo, valor):
        if not valor or (isinstance(valor, str) and valor.isspace()):
            return {"campo": campo, "error": "Este campo es obligatorio."}

        if (campo == "usuario" and  len(valor)<3):
            return {"campo": campo, "error":  "Este campo debe contener almenos 3 caracteres"}
        if (campo == "contraseña" and  len(valor)<4):
            return {"campo": campo, "error":  "Este campo debe contener almenos 4 caracteres"}


        return None  # No hay errores

    
    #Mostrar los errores en pantalla
    def mostrar_errores(self, errores):
        # Reinicia todos los labels de error y los colores de los frames
        for campo in self.vista.labels_errores.keys():
            self.vista.labels_errores[campo].configure(text="")
            self.vista.frames_campos[campo].configure(fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR))

        # Muestra los mensajes de error y cambia el color de los frames a rojo
        for error in errores:
            campo = error["campo"]
            mensaje = error["error"]
            self.vista.labels_errores[campo].configure(text=mensaje)
            self.vista.frames_campos[campo].configure(fg_color="red")

        # Cancela cualquier temporizador existente
        if self.vista.temporizador is not None:
            self.vista.after_cancel(self.vista.temporizador)

        # Programa la eliminación de los mensajes de error después de 5 segundos (5000 milisegundos)
        self.vista.temporizador = self.vista.after(2000, self.eliminar_errores)
    
    #Eliminar los errores de pantalla
    def eliminar_errores(self):
        # Elimina todos los mensajes de error y restablece los colores de los frames
        for campo in self.vista.labels_errores.keys():
            self.vista.labels_errores[campo].configure(text="")
            self.vista.frames_campos[campo].configure(fg_color=(c.LIGHT_TEXT_COLOR, c.DARK_TEXT_COLOR))


