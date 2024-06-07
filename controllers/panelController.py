from utils.animaciones import right, up
from views.atletasVentana import AtletasVentana
from views.crearPartido import CrearPartidoVentana
from views.listaAtletasVentana import ListaAtletasVentana
from views.partidosVentana import PartidosVentana



class PanelController:
    def __init__(self, vista):
        self.vista = vista
        


    def cambiar_ventana(self, indice, query=None):
        ventanas = [ListaAtletasVentana, PartidosVentana, AtletasVentana, CrearPartidoVentana ]
        
        self.vista.contenedor_contenido.place_forget()
        if indice == len(ventanas):
            self.vista.master.destroy()
        

        for index, Ventana in enumerate(ventanas):
            if index == indice:

                y=self.vista.alto_ventana
                x=self.vista.ancho_navbar
                
                if index == 2 or index==3:
                    y=0
                    x=self.vista.ancho_navbar+self.vista.ancho_ventana 

                # Crea la nueva ventana
                if query:
                    print("Query", query)
                    self.vista.contenedor_contenido = Ventana(self.vista, query)
                else:
                    self.vista.contenedor_contenido = Ventana(self.vista)

      


                    
                self.vista.contenedor_contenido.place(x=x, y=y, relwidth=1 - self.vista.ancho_navbar/self.vista.ancho_ventana, relheight=1)
                self.vista.contenedor_contenido.main()

                if index == 2 or index==3:
                    self.animacion_right()
                else:
                    self.animacion_up()
    
    def animacion_up(self):
        up(self.vista, self.vista.contenedor_contenido, self.animacion_up, 0)

    def animacion_right(self):
        right(self.vista, self.vista.contenedor_contenido, self.animacion_right, 300)    