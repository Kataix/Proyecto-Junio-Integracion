from sympy.parsing.sympy_parser import parse_expr		## importamos todas las librerias que usaremos
from sympy import *
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

myWindow = Tk() #Se instancia tkinter frame.
myWindow.title('Calculo integrales') #Titulo de la ventanta.
myWindow.geometry("1080x720") #Tamaño de la ventana.

f = Label(myWindow, text='Ingrese funcion a evaluar: ', font='times' ,) #Cuadro para ingresar funcion.
f.pack()
txto = Text(myWindow, width=50, height=2) #Tamaño cuadro.
txto.pack()
symb = Label(myWindow, text='Ingrese simbolo de la integracion: ', font='times') #Cuadro para ingresar simbolo.
symb.pack()
my_symbol = Text(myWindow, width=10, height=2) #Tamaño cuadro simbolo.
my_symbol.pack()

def calcular():
	funcion = txto.get(1.0, END) #Funcion a ingresar.
	simbolo = my_symbol.get(1.0, END) #Simbolo(x) a ingresar.
	f = parse_expr(funcion) #Parsing a la funcion.
	x = symbols(f'{simbolo}') #Se convierte el string a simbolo.
	fun = Integral(f, (x)) #Datos a integrar.
	resultado = integrate(f, (x)) #Calculo de la integral.
		
	valor.config(text=f'Value: {resultado}')#Mostramos resultado.
	graficar(resultado)

btn = Frame(myWindow)
btn.pack()
calcula = Button(btn, text='Calcular', command=calcular) #Boton para realizar cálculo.
calcula.grid() 
valor = Label(myWindow)
valor.pack()
#Se define tamaño grafica y se muestra.
fig = matplotlib.figure.Figure(figsize=(24, 12), dpi=50)
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig, master=valor)
canvas.get_tk_widget().pack()
canvas._tkcanvas.pack()
#Elimina visibilidad gráfica canvas.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


#Función que representa el resultado como latex.
def graficar(text):
	tmptext = latex(text) #Resultado convertido a latex.
	tmptext = "$"+tmptext+"$"
	ax.clear()  #Se borra cualquier resultado anterior mostrado.
	ax.text(0.1, 0.5, tmptext, fontsize = 50)  
	canvas.draw() #Se genera la representacion.

myWindow.bind('<Return>', graficar)
myWindow.mainloop()