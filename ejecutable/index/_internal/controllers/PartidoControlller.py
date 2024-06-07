
from datetime import datetime
from sqlalchemy.orm import Session
from utils.db import ConectarDb
from constantes import constantes as c
from CTkMessagebox import CTkMessagebox
from sqlalchemy import func, or_
from models.partidoModelo import Partido

class PartidoController:
    def __init__(self, vista):
        self.vista = vista
       

   
    #Registro de partidos
    def registro_partido(self):
        campos = {
            "equipo_local": self.vista.comboboxEquipoLocal.get(),
            "equipo_visitante": self.vista.comboboxEquipoVisitante.get(),
            "fecha_partido": self.vista.fecha.get(),
            "hora_partido": self.vista.hora.get(),
         

        }
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime('%d/%m/%Y')

        if campos["fecha_partido"] == fecha_formateada:
            campos["estado_partido"] = "Hoy"

        if self.vista.comboboxEquipoLocal.get()==self.vista.comboboxEquipoVisitante.get():
            self.vista.labels_errores["equipo_visitante"].configure(text="Equipos iguales")
            self.vista.frames_campos["equipo_visitante"].configure(fg_color="red")

            # Programa la eliminación de los mensajes de error después de 2 segundos (2000 milisegundos)
            self.vista.temporizador = self.vista.after(2000, self.eliminar_errores)
            return

        errores = [self.validar_campo(campo, valor) for campo, valor in campos.items()]
        errores = [error for error in errores if error is not None]  # Filtra los errores

        if errores:
            # Enviar los errores a la vista
            self.mostrar_errores(errores)
        else:
        
         
            nuevo_partido = Partido(**campos)

            # Crear una nueva sesión
            session = Session(ConectarDb().engine)

            #  Añadir el nuevo partido a la sesión
            session.add(nuevo_partido)

            # Hacer commit de la sesión para guardar los cambios en la base de datos
            session.commit()
            
            if nuevo_partido is not None:
                self.vista.master.mostrar_errores("exitoso","Partido creado exitosamente", "top-center")
                self.vista.master.controlador.cambiar_ventana(1)
            else:
                self.vista.master.mostrar_errores("error","Ocurrio un error", "top-center")


    # Obtener los partidos
    def obtener_partidos(self):
        session = Session(bind=ConectarDb().engine)

     
        # Obtener todos los partidos ordenados por ID en orden descendente
        partidos = session.query(Partido).order_by(Partido.id.desc()).all()

       

        session.close()
        return [*partidos]

    
    
    
    def modificar_partido(self, id):
        campos = {
            "equipo_local": self.vista.comboboxEquipoLocal.get(),
            "equipo_visitante": self.vista.comboboxEquipoVisitante.get(),
            "fecha_partido": self.vista.fecha.get(),
            "hora_partido": self.vista.hora.get(),
        
        }

        if self.vista.comboboxEquipoLocal.get()==self.vista.comboboxEquipoVisitante.get():
            print("SI SON")
            self.vista.labels_errores["equipo_visitante"].configure(text="Equipos iguales")
            self.vista.frames_campos["equipo_visitante"].configure(fg_color="red")

            # Programa la eliminación de los mensajes de error después de 2 segundos (2000 milisegundos)
            self.vista.temporizador = self.vista.after(2000, self.eliminar_errores)
            return

        errores = [self.validar_campo(campo, valor) for campo, valor in campos.items()]
        errores = [error for error in errores if error is not None]  # Filtra los errores

        if errores:
            # Enviar los errores a la vista
            self.mostrar_errores(errores)
        else:



            # Crear una nueva sesión
            session = Session(ConectarDb().engine)

            partido = session.query(Partido).filter(Partido.id == id).update(campos)

            if partido is not None:
                self.vista.master.mostrar_errores("exitoso","Partido modificado exitosamente", "top-center")
                session.commit()
                self.vista.master.controlador.cambiar_ventana(1)

            else:
                self.vista.master.mostrar_errores("error","Ocurrio un error", "top-center")

            



    #Jpanel de confirmación para eliminar partido
    def eliminar_modal(self, id):
        CTkMessagebox(title="Error", message="¿Desea eliminar este partido?", icon="cancel", button_color=("#B3B3B3",c.DARK_TEXT_COLOR), button_hover_color="#FFDB59", button_text_color=c.DARK_TEMA, title_color=c.DARK_TEXT_COLOR, sound=True, fade_in_duration=50, funcion_ejecutar= lambda: self.eliminar_partido(id), option_1="Cancelar", option_2="Si", font=('yu gothic ui', 15, 'bold'))

    #Para eliminar un partido
    def eliminar_partido(self, id):
        

        session = Session(bind=ConectarDb().engine)
        # Obtener el partido a eliminar
        partido = session.query(Partido).filter(Partido.id == id).first()
        
        # Comprueba si el partido existe
        if partido is not None:
            # Eliminar el registro
            session.delete(partido)
            # Confirmar la transacción
            session.commit()
            
         
            #Mostrar mensaje por pantalla
            self.vista.master.mostrar_errores("Exitoso","Partido eliminado exitosamente", "top-center")
            
            #Vuelve a obtener los partidos ya actualizados
            self.vista.todos_partido = self.obtener_partidos()
            self.vista.master.controlador.cambiar_ventana(1)
        
        else: 
            self.vista.master.mostrar_errores("error","Ocurrio un error, vuelve a intentarlo", "top-center")

    
    

    #Obtener la cantidad de registros de la tabla partido
    def cantidad_registros(self):
        session = Session(bind=ConectarDb().engine)

        # Cuenta la cantidad de registros en la tabla 'partidos'
        total_registros = session.query(func.count(Partido.id)).scalar()
        session.close()

        return total_registros





    #Validar campos del formulario
    def validar_campo(self, campo, valor):
        if not valor or (isinstance(valor, str) and valor.isspace()):
            return {"campo": campo, "error": "Este campo es obligatorio."}

        if (campo == "equipo_local" or  campo == "equipo_visitante") and valor not in ["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}
        if campo == "hora_partido" and valor not in [f"{i:02}:00" for i in range(8, 19)]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}


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



    # !TODO: FILTROS
    def filtros(self):
        equipos=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"]
        fecha=["Proximo", "Hoy", "En Juego", "Finalizado"]
        estado_value = self.vista.comboboxFecha.get() if self.vista.comboboxFecha.get() in fecha else None
        equipo_value = self.vista.comboboxCategoria.get() if self.vista.comboboxCategoria.get() in equipos else None
        
        

        session = Session(bind=ConectarDb().engine)

        # Crea una consulta base
        query = session.query(Partido)

              
       
        if equipo_value:
            query = query.filter(or_(Partido.equipo_local == equipo_value, Partido.equipo_visitante == equipo_value))
        if estado_value:
            query = query.filter(Partido.estado_partido == estado_value)
        if equipo_value and estado_value:
            query = query.filter(or_(Partido.equipo_local == equipo_value, Partido.equipo_visitante == equipo_value), Partido.estado_partido==estado_value)
        # Ejecuta la consulta
        resultados = query.all()
        
        #Modifica el array de Partidos
        self.vista.todos_partidos=resultados
        
        #Recarga el widget
        self.vista.recargar()   

   
