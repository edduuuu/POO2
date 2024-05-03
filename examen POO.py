from tkinter import * 
from tkinter import #mporta todos los símbolos (clases, funciones, etc.) del módulo
window = Tk()  #Crea una instancia de la clase Tk(), que representa una ventana principal de la aplicación.
window.title("Welcome to Movie selector") #Establece el título de la ventana como "Welcome to movie selector"
window.geometry('800x800') #Establece las dimensiones de la ventana a 800 píxeles de ancho por 800 píxeles de alto.
window.configure(background = "grey"); #Establece el color de fondo de la ventana en grey.
a = Label(window ,text = "movie name").grid(row = 0,column = 0) 
b = Label(window ,text = "year of release").grid(row = 1,column = 0)
c = Label(window ,text = "director").grid(row = 2,column = 0)
d = Label(window ,text = "platform to see it").grid(row = 3,column = 0) #Crea cuatro etiquetas de texto para etiquetar las entradas de datos. Esta crea filas y columnas en la ventana creada
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1) #Crea cuatro campos de entrada de texto para que el usuario ingrese datos.la diferencia con las de arriba es que se almacenan los datos
def clicked(): #Define una función llamada clicked(), que se ejecutará cuando se haga clic en el botón "Submit". 
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0) #Crea un botón de la biblioteca ttk con el texto "Submit".
window.mainloop() #Esta funcion sirve para que la ventana se mantenga abierta
