from sqlalchemy import func
from models.partidoModelo import Partido
from utils.db import ConectarDb
from sqlalchemy.orm import Session
from models.usuarioModelo import Usuario
from utils.db import ConectarDb

ConectarDb().conectar_db()

usuarios = [
    Usuario(nombre="Pocho", apellido="Gómez", direccion="Avenida Los Laureles 987, Caracas", telefono="04128765432", edad=24, sexo="Masculino", rol="Administrador", categoria="Adulto A", contraseña="1234"),
    Usuario(nombre="Carlos", apellido="González", direccion="Calle Los Alamos 123, Caracas", telefono="04123456789", edad=30, sexo="Masculino", rol="Jugador", categoria="Adulto B", targetas_rojas=1, targetas_amarillas=0, goles=20, partidos=4, activo="Activo", posicion="Delantero",),
    Usuario(nombre="David", apellido="Pérez", direccion="Avenida Bolívar 456, Maracaibo", telefono="04149876543", edad=25, sexo="Masculino", rol="Equipo Tecnico", categoria="Juvenil A", activo="Inactivo", posicion="Director tecnico",),
    Usuario(nombre="Maria", apellido="Martínez", direccion="Calle Los Pinos 789, Valencia", telefono="04241234567", edad=30, sexo="Femenino", rol="Jugador", categoria="Juvenil B", targetas_rojas=6, targetas_amarillas=2, goles=6, partidos=1, activo="Activo", posicion="Medio",),
    Usuario(nombre="Ana", apellido="Rodríguez", direccion="Avenida Los Ilustres 321, Barquisimeto", telefono="04167654321", edad=27, sexo="Femenino", rol="Jugador", categoria="Infantil A", targetas_rojas=2, targetas_amarillas=8, goles=1, partidos=10, activo="Activo", posicion="Defensa",),
    Usuario(nombre="Luis", apellido="Hernández", direccion="Calle Las Acacias 654, Mérida", telefono="04262345678", edad=33, sexo="Masculino", rol="Equipo Tecnico", categoria="Infantil B",activo="Inactivo", posicion="Auxiliar tecnico",),
]


# Crear 10 registros de partidos
partidos = [
    Partido(equipo_visitante="Infantil A", equipo_local="Infantil B", fecha_partido="26/06/2024", hora_partido="15:00", goles_visitante=2, goles_local=1, estado_partido="Finalizado"),
    Partido(equipo_visitante="Juvenil A", equipo_local="Juvenil B", fecha_partido="28/05/2024", hora_partido="16:00",  estado_partido="Hoy"),
    Partido(equipo_visitante="Adulto A", equipo_local="Adulto B", fecha_partido="29/05/2024", hora_partido="14:00",  estado_partido="Proximo"),
    Partido(equipo_visitante="Infantil A", equipo_local="Adulto A", fecha_partido="01/06/2024", hora_partido="13:00",  estado_partido="Proximo"),
    Partido(equipo_visitante="Juvenil B", equipo_local="Adulto B", fecha_partido="09/06/2024", hora_partido="12:00",  estado_partido="Proximo"),
    Partido(equipo_visitante="Adulto B", equipo_local="Infantil B", fecha_partido="05/06/2024", hora_partido="11:00",  estado_partido="Proximo"),
]

session = Session(bind=ConectarDb().engine)

total_usuarios = session.query(func.count(Usuario.id)).scalar()
total_partidos = session.query(func.count(Partido.id)).scalar()

# Agregar los usuarios a la sesión
if(total_usuarios == 0):
    for usuario in usuarios:
        session.add(usuario)

# Agregar los partidos a la sesión
if(total_partidos == 0):
    for partido in partidos:
        session.add(partido)
        
# Confirmar la transacción
session.commit()


print("Datos agregados exitosamente")    

# Cerrar la sesión
session.close()
