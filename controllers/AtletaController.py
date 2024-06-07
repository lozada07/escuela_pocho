
from sqlalchemy.orm import Session
from models.usuarioModelo import Usuario
from utils.db import ConectarDb
from constantes import constantes as c
from CTkMessagebox import CTkMessagebox
from sqlalchemy import func

class AtletaController:
    def __init__(self, vista):
        self.vista = vista
        self.permitido = False
        self.valor_edad = -1
    #Registro de usuarios
    def registro(self):
        campos = {
            "nombre": self.vista.nombre.get(),
            "apellido": self.vista.apellido.get(),
            "direccion": self.vista.direccion.get(),
            "telefono": self.vista.telefono.get(),
            "rol": self.vista.comboboxRol.get(),
            "categoria": self.vista.comboboxCategoria.get(),
            "edad": self.vista.edad.get(),
            "sexo": self.vista.comboboxGenero.get(),
            "posicion": self.vista.comboboxPosicion.get(),
            "activo": self.vista.comboboxActivo.get(),
        }

        if ((campos["edad"] != self.valor_edad ) or (campos["edad"] == self.valor_edad and self.permitido == False)) and campos["edad"] != None and campos["edad"] < 18 :

        # if campos["edad"] != None and campos["edad"] < 18 and ((self.permitido == False and campos["edad"] != self.valor_edad) or ( campos["edad"] == self.valor_edad and self.permitido == False)):
            ms = CTkMessagebox(title="Error", message="Usuario meno de Edad, ¿Su representante esta de acuerdo?", icon="warning", button_color=("#B3B3B3",c.DARK_TEXT_COLOR), button_hover_color="#FFDB59", button_text_color=c.DARK_TEMA, title_color=c.DARK_TEXT_COLOR, sound=True, fade_in_duration=50, option_1="Cancelar", option_2="Si", font=('yu gothic ui', 15, 'bold'))
            if ms.get() == "Si":

                self.permitido = True
            else:
                self.permitido = False

            self.valor_edad = campos["edad"]    

        errores = [self.validar_campo(campos, campo, valor) for campo, valor in campos.items()]
        errores = [error for error in errores if error is not None]  # Filtra los errores

        if errores:
            # Enviar los errores a la vista
            self.mostrar_errores(errores)
        else:


            #Convertir valores
            campos["edad"]=int(self.vista.edad.get())
            if campos["rol"] == "Jugador":
                campos["targetas_rojas"]=int(self.vista.targetas_rojas.get()) if self.vista.targetas_rojas.get() else 0 
                campos["targetas_amarillas"]=int(self.vista.targetas_amarillas.get()) if self.vista.targetas_amarillas.get() else 0 
                campos["goles"]=int(self.vista.goles.get()) if self.vista.goles.get() else 0 
                campos["partidos"]=int(self.vista.partidos.get()) if self.vista.partidos.get() else 0 

         
            nuevo_usuario = Usuario(**campos)

            # Crear una nueva sesión
            session = Session(ConectarDb().engine)

            # # Añadir el nuevo usuario a la sesión
            session.add(nuevo_usuario)

            # # Hacer commit de la sesión para guardar los cambios en la base de datos
            session.commit()
            
            if nuevo_usuario.id is not None:
                self.vista.master.mostrar_errores("exitoso","Usuario creado exitosamente", "top-right")
                self.vista.master.controlador.cambiar_ventana(0)
            else:
                self.vista.master.mostrar_errores("error","Ocurrio un error", "top-center")

    # Obtener los usuarios
    def obtener_usuarios(self):
        session = Session(bind=ConectarDb().engine)

     
        # Obtener todos los usuarios ordenados por ID en orden descendente
        usuarios = session.query(Usuario).filter(Usuario.rol != "Administrador").order_by(Usuario.id.desc()).all()

        # Modificar la variable en la vista
        self.vista.todos_usuarios = usuarios

        session.close()
        return [*usuarios]

    
    
    
    def modificar(self, id):
        campos = {
            "nombre": self.vista.nombre.get(),
            "apellido": self.vista.apellido.get(),
            "direccion": self.vista.direccion.get(),
            "telefono": self.vista.telefono.get(),
            "rol": self.vista.comboboxRol.get(),
            "categoria": self.vista.comboboxCategoria.get(),
            "edad": self.vista.edad.get(),
            "sexo": self.vista.comboboxGenero.get(),
            "posicion": self.vista.comboboxPosicion.get(),
            "activo": self.vista.comboboxActivo.get(),
        }


        errores = [self.validar_campo(campos, campo, valor) for campo, valor in campos.items()]
        errores = [error for error in errores if error is not None]  # Filtra los errores

        if errores:
            # Enviar los errores a la vista
            self.mostrar_errores(errores)
        else:

            #Convertir valores
            if campos["rol"] == "Jugador":
                campos["targetas_rojas"]=int(self.vista.targetas_rojas.get() or 0 ) 
                campos["targetas_amarillas"]=int(self.vista.targetas_amarillas.get() or 0) 
                campos["goles"]=int(self.vista.goles.get() or 0) 
                campos["partidos"]=int(self.vista.partidos.get() or 0) 
            else:          
                campos["targetas_rojas"]=0 
                campos["targetas_amarillas"]=0 
                campos["goles"]=0 
                campos["partidos"]=0 

            # Crear una nueva sesión
            session = Session(ConectarDb().engine)

            usuario = session.query(Usuario).filter(Usuario.id == id).update(campos)

            if usuario is not None:
                self.vista.master.mostrar_errores("exitoso","Usuario modificado exitosamente", "top-center")
                session.commit()
                self.vista.master.controlador.cambiar_ventana(0)

            else:
                self.vista.master.mostrar_errores("error","Ocurrio un error", "top-center")

            



    #Jpanel de confirmación para eliminar usuario
    def eliminar_modal(self, id, framerId):
        CTkMessagebox(title="Error", message="¿Desea eliminar este atleta?", icon="cancel", button_color=("#B3B3B3",c.DARK_TEXT_COLOR), button_hover_color="#FFDB59", button_text_color=c.DARK_TEMA, title_color=c.DARK_TEXT_COLOR, sound=True, fade_in_duration=50, funcion_ejecutar= lambda: self.eliminar(id,framerId), option_1="Cancelar", option_2="Si", font=('yu gothic ui', 15, 'bold'))

    #Para eliminar un usuario
    def eliminar(self, id, framerId):
        

        session = Session(bind=ConectarDb().engine)
        # Obtener el usuario a eliminar
        usuario = session.query(Usuario).filter(Usuario.id == id).first()
        
        # Comprueba si el usuario existe
        if usuario is not None:
            # Eliminar el registro
            session.delete(usuario)
            # Confirmar la transacción
            session.commit()
            
            #Eliminar el framer de la ventana
            for framer in self.vista.scrollable_frame.winfo_children():
                if(framer.winfo_id()==framerId):
                    framer.destroy() 
         
            #Actualizar en la ventana la cantidad de usuarios
            for campo in self.vista.estadisticas_contenedor.winfo_children():
                for label in campo.winfo_children():
                    if int(label.cget("text")) == self.vista.total_usuarios:
                        self.vista.total_usuarios -=1
                        label.configure(text=f"  {self.vista.total_usuarios}")
                      
            #Mostrar mensaje por pantalla
            self.vista.mostrar_errores("Exitoso","Usuario eliminado exitosamente", "top-center")
            
            #Vuelve a obtener los usuarios ya actualizados
            self.vista.todos_usuarios = self.obtener_usuarios()
        
        else: 
            self.vista.mostrar_errores("error","Ocurrio un error, vuelve a intentarlo", "top-center")

    
    

    #Obtener la cantidad de registors de las tablas
    def cantidad_registros(self):
        session = Session(bind=ConectarDb().engine)

        # Cuenta la cantidad de registros en la tabla 'usuarios'
        total_registros = session.query(func.count(Usuario.id)).scalar()
        session.close()

        return total_registros





    #Validar campos del formulario
    def validar_campo(self,campos, campo, valor):
        if not valor or (isinstance(valor, str) and valor.isspace()):
            return {"campo": campo, "error": "Este campo es obligatorio."}

        if campo in ["nombre", "apellido", "direccion"] and len(valor) < 2:
            return {"campo": campo, 
                    "error": "Este campo debe tener al menos 2 caracteres."}

        if campo == "telefono" and not valor.isdigit():
            return {"campo": campo, "error": "Este campo solo puede contener números."}

        if campo == "edad" and valor > 35:
            return {"campo": campo, "error": "Edad no permitida"}

        if campo == "rol" and valor not in ["Jugador", "Equipo Tecnico"]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}

        if campo == "categoria" and valor not in ["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}

        if campo == "sexo" and valor not in ["Masculino", "Femenino"]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}

        if campo == "posicion" and campos["rol"] == "Jugador" and valor not in ["Delantero", "Medio", "Portero" ]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}

        if campo == "posicion" and campos["rol"] == "Equipo Tecnico" and valor not in ["Defensa", "Director tecnico", "Auxiliar tecnico", "Preparador fisico", "Psicólogo deportivo", "Médico"]:
            return {"campo": campo, "error":  "Este campo es obligatorio."}

        
        # if campo == "posicion"  and valor not in ["Defensa", "Director tecnico", "Auxiliar tecnico", "Preparador fisico", "Psicólogo deportivo", "Médico"]:
        #     return {"campo": campo, "error":  "Este campo es obligatorio."}


        if campo == "activo" and valor not in ["Inactivo", "Activo"]:
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
        categorias=["Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Adulto A", "Adulto B"]
        sexo=["Masculino", "Femenino"]
        input_value = self.vista.input.get()
        categoria_value = self.vista.comboboxCategoria.get() if self.vista.comboboxCategoria.get() in categorias else None
        sexo_value = self.vista.comboboxMasFiltros.get()  if self.vista.comboboxMasFiltros.get() in sexo else ""
        
        

        session = Session(bind=ConectarDb().engine)

        # Crea una consulta base
        query = session.query(Usuario)

        if input_value and categoria_value and sexo_value:  
            query = query.filter(Usuario.nombre.ilike(f"%{input_value}%"), Usuario.categoria == categoria_value,  Usuario.sexo == sexo_value )
        elif input_value and categoria_value:  
            query = query.filter(Usuario.nombre.ilike(f"%{input_value}%"), Usuario.categoria == categoria_value )
        elif input_value and sexo_value:
            query = query.filter(Usuario.nombre.ilike(f"%{input_value}%"), Usuario.sexo == sexo_value )
        elif categoria_value and sexo_value:
            query = query.filter( Usuario.categoria == categoria_value , Usuario.sexo == sexo_value )
        elif input_value:
            query = query.filter(Usuario.nombre.ilike(f"%{input_value}%"))
        elif categoria_value:
            query = query.filter(Usuario.categoria == categoria_value )
        elif sexo_value:    
            query = query.filter(Usuario.sexo == sexo_value )
      
                 
        # Ejecuta la consulta
        resultados = query.all()
        
        #Modifica el array de usuarios
        self.vista.todos_usuarios=resultados
        
        #Recarga el widget
        self.vista.recargar()   

    def mas_campos(self, choice):
        if (choice == "Jugador"):
            self.vista.isAtleta=True
            self.vista.comboboxPosicion.configure(values=["Delantero", "Medio", "Portero", "Defensa"])
        else:
            self.vista.isAtleta=False
            self.vista.comboboxPosicion.configure(values=["Director tecnico", "Auxiliar tecnico", "Preparador fisico", "Psicólogo deportivo", "Médico"])


            self.vista.labelTargetasRojas.place_forget()
            self.vista.targetas_rojas.place_forget()
            self.vista.frames_campos["targetas_rojas"].place_forget()
            
            self.vista.labelTargetasAmarillas.place_forget()
            self.vista.targetas_amarillas.place_forget()
            self.vista.frames_campos["targetas_amarillas"].place_forget()
            
            self.vista.labelGoles.place_forget()
            self.vista.goles.place_forget()
            self.vista.frames_campos["goles"].place_forget()

            self.vista.labelPartidos.place_forget()
            self.vista.partidos.place_forget()
            self.vista.frames_campos["partidos"].place_forget()


      
            

 
        self.vista.campos_atletas()
        print("combobox dropdown clicked:", choice)
   
    def verificar_edad(self):
       print("Hello")