
import pandas as pd
from customtkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from utils.buscarImg import buscarImg

def exportar_jugadores_pdf(datos):


    # Crea un DataFrame con los datos
    df = pd.DataFrame()
    columnas = ['nombre', 'apellido', 'edad', 'sexo', 'rol', 'categoria', 'posicion', 'activo']

    jugadores = []
    for jugador in datos:
        if jugador.rol != "Equipo Tecnico": 
            jugadores.append(jugador)


    for columna in columnas:
        df[columna] = [getattr(jugador, columna) for jugador in jugadores]

    # Modal de descarga
    # Modal de descarga
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")], initialfile="Listado_de_Jugadores.pdf", title="Listado de Jugadores")


    # Crea un archivo PDF con márgenes ajustados
    doc = SimpleDocTemplate(ruta_archivo, pagesize=letter, topMargin=-2)
    
    # Agrega el logotipo 
    logo_path = buscarImg("../img/Logo.png")  
    logo = Image(logo_path, width=120, height=110, hAlign="CENTER")
    styles = getSampleStyleSheet()

    # Agrega el texto "Listado de Jugadores" a la derecha con estilo personalizado
    estilo_titulo_personalizado = ParagraphStyle(
        name="TituloPersonalizado",
        parent=styles["Title"],  # Utiliza el estilo existente como base
        textColor="#ffd43b", 
        alignment=1,  # 0: izquierda, 1: centro, 2: derecha
        fontName="Helvetica-Bold",  # Fuente en negrita 
        fontSize=39
    )
    texto = Paragraph("<b>Listado de Usuarios</b>", estilo_titulo_personalizado)

    # Crea una tabla con dos celdas para logotipo y texto
    tabla_cabecera = Table([[logo, texto]], rowHeights=130, colWidths=[100, 500], hAlign="CENTER", vAlign="MIDDLE", cornerRadii=(10, 10, 0, 0))

    # Establecer el estilo de la tabla
    tabla_cabecera.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), '#0f172a'),  # Aplicar fondo a todas las celdas
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, 0), 12),
        ('RIGHTPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

    ]))

    # Crea la tabla con los datos 
    table_data = [columnas] + df.values.tolist()
    table = Table(table_data, colWidths=75)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#1e293b'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), '#f7f7f7')
    ]))

    # Crea una lista de elementos para la página
    elementos = [tabla_cabecera, table]

    # Construye el PDF
    doc.build(elementos)


def exportar_partidos_pdf(datos):

    # Crea un DataFrame con los datos
    df = pd.DataFrame()

    columnas = ['equipo_local', 'equipo_visitante', 'fecha_partido', 'hora_partido', 'goles_local', 'goles_visitante', 'estado_partido']


    partidos=[]
    for partido in datos:
        if partido.estado_partido == "Proximo" or  partido.estado_partido == "Hoy":
            partido.goles_local = ""
            partido.goles_visitante = ""
        
        partidos.append(partido)
    
    for columna in columnas:
        df[columna] = [getattr(partido, columna) for partido in partidos]

    # Modal de descarga
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")], initialfile="Listado_de_Partidos.pdf", title="Listado de Jugadores")


    # Crea un archivo PDF con márgenes ajustados
    doc = SimpleDocTemplate(ruta_archivo, pagesize=letter, topMargin=-2)
    
    # Agrega el logotipo 
    logo_path = buscarImg("../img/Logo.png")  
    logo = Image(logo_path, width=120, height=110, hAlign="CENTER")
    styles = getSampleStyleSheet()

    # Agrega el texto "Listado de Partidos" a la derecha con estilo personalizado
    estilo_titulo_personalizado = ParagraphStyle(
        name="TituloPersonalizado",
        parent=styles["Title"],  # Utiliza el estilo existente como base
        textColor="#ffd43b", 
        alignment=1,  # 0: izquierda, 1: centro, 2: derecha
        fontName="Helvetica-Bold",  # Fuente en negrita 
        fontSize=39
    )
    texto = Paragraph("<b>Listado de Partidos</b>", estilo_titulo_personalizado)

    # Crea una tabla con dos celdas para logotipo y texto
    tabla_cabecera = Table([[logo, texto]], rowHeights=130, colWidths=[100, 500], hAlign="CENTER", vAlign="MIDDLE", cornerRadii=(10, 10, 0, 0))

    # Establecer el estilo de la tabla
    tabla_cabecera.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), '#0f172a'),  # Aplicar fondo a todas las celdas
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, 0), 12),
        ('RIGHTPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

    ]))

    # Crea la tabla con los datos 
    table_data = [columnas] + df.values.tolist()
    table = Table(table_data, colWidths=85.7)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#1e293b'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), '#f7f7f7')
    ]))

    # Crea una lista de elementos para la página
    elementos = [tabla_cabecera, table]

    # Construye el PDF
    doc.build(elementos)


