def up(master, elemento, callback, limite):
    # obtener la posición actual
    y = float(elemento.place_info()['y'])
    # establecer la nueva posición
    if y > limite:
        elemento.place_configure(y=y-30)
        # repetir después de 1000ms
        master.after(5, callback)

def right(master, elemento, callback, limite):
    # obtener la posición actual
    x = float(elemento.place_info()['x'])
    # establecer la nueva posición
    if x >=limite :  # cambiar esto según tus necesidades
        elemento.place_configure(x=x-30)  # cambiar esto según tus necesidades
        # repetir después de 1000ms
        master.after(4, callback)
