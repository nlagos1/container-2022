import histograma as ht
import transport as tr
import calculator as clt

from tkinter import *
from tkinter import font
from PIL import ImageTk, Image


def ventana():
    new = Tk()
    new.title('Container y metodos de transporte')
    new.geometry("800x500")
    new.resizable(0, 0)
    new.config(bg='light cyan')

    defaultFont = font.nametofont('TkDefaultFont')
    defaultFont.config(family="console", weight=font.BOLD, size=8)

    titulo = Label(new, text="Tu mejor opcion para trasporte!")

    title = Label(new, text="Vehiculos totales:", bg='light steel blue')
    title3 = Label(new, text="Tipo de vehiculo:", bg='light steel blue')
    title2 = Label(new, text="Tonelaje Total:", bg='cadet blue')
    title4 = Label(new, text="Coste total:", bg='cyan')
    title5 = Label(new, text="Tonelaje T. Masa:", bg='cadet blue')
    title7 = Label(new, text="Coste vehiculo:", bg="cyan")

    respuesta = Label(new, text=tr.option[0], bg='light gray')  # Vehiculo
    respuesta2 = Label(new, text=clt.cal_tonelaje_total(), bg='light gray')  # Tonelaje total
    respuesta3 = Label(new, text=tr.option[2], bg='light gray')  # Vehiculo cantidad
    respuesta4 = Label(new, text=tr.option[1], bg='light gray')  # Coste Vehiculo
    respuesta5 = Label(new, text=('Solida:', clt.calcular_tonelaje_masa()[0]), bg='mint cream')  # Tonelaje per masa
    respuesta6 = Label(new, text=('Liquida:', clt.calcular_tonelaje_masa()[1]), bg='mint cream')  # Tonelaje per masa
    respuesta7 = Label(new, text=('Gas:', clt.calcular_tonelaje_masa()[2]), bg='mint cream')  # Tonelaje per masa
    respuesta8 = Label(new, text="sss", bg='light gray')  # Tonelaje per carga
    respuesta9 = Label(new, text=tr.Avion.cost, bg='light gray')  # coste vehiculo

    title.place(x=10, y=90, width=100, height=30)
    title2.place(x=220, y=50, width=100, height=30)
    title3.place(x=10, y=50, width=100, height=30)
    title4.place(x=430, y=50, width=100, height=30)
    title5.place(x=220, y=90, width=100, height=30)
    title7.place(x=430, y=90, width=100, height=30)

    titulo.config(bg='light cyan', fg='black', font=('Segoe Script', 23))
    titulo.place(x=10, y=3)

    respuesta.place(x=115, y=50, width=100, height=30)
    respuesta2.place(x=325, y=50, width=100, height=30)
    respuesta3.place(x=115, y=90, width=100, height=30)
    respuesta4.place(x=535, y=50, width=100, height=30)
    respuesta5.place(x=325, y=90, width=100, height=30)
    respuesta6.place(x=325, y=130, width=100, height=30)
    respuesta7.place(x=325, y=170, width=100, height=30)
    respuesta9.place(x=535, y=90, width=100, height=30)

    mensaje = Label(new, text="Imagen de referencia \n del vehiculo.")

    mensaje.place(x=540, y=420)
    mensaje.config(font=('Segoe Script', 12))

    x = Button(text=" Histograma Contenedores", bg="DeepSkyBlue3", borderwidth=0, command=ht.histograma_1)
    y = Button(text="Histograma Tonelaje", bg="DeepSkyBlue3", borderwidth=0, command=ht.histograma_2)

    x.place(x=640, y=90, width=150, height=30)
    y.place(x=640, y=50, width=150, height=30)

    foto = ImageTk.PhotoImage(Image.open(tr.option[3]).resize((300, 200)))
    foton = Label(new, image=foto, borderwidth=0).place(x=490, y=200)
    new.mainloop()


vergil = ventana()
