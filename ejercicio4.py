from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import dda
import bresenham

class App:
  def __init__(self, master) -> None:
  
    # Instantiating master 
    self.master = master

    self.fila = 1
    self.listaDDA = []

    self.lOpcion = Label(self.master, text="Seleccione el tamaño del espacio ordenado (2D o 3D): ", font=("Arial", 18)).grid(column = 0, row = 1, columnspan = 3, sticky = W)

    self.radio1 = Radiobutton(self.master, text="2D", font=("Arial", 18), value = "2D", variable = opcion, command = self.seleccionado).grid(column = 3, row = 1)
    self.radio2 = Radiobutton(self.master, text="3D", font=("Arial", 18), value = "3D", variable = opcion, command = self.seleccionado).grid(column = 4, row = 1)
    
    self.algoritmoAEscoger = Label(self.master, text="Seleccione el algoritmo: ", font=("Arial", 18)).grid(column = 0, row = 2, columnspan = 2, sticky = W)    
    self.algoritmoDDA = Radiobutton(self.master, text="DDA", font=("Arial", 18), value = "DDA", variable = algoritmo, command = self.seleccionado).grid(column = 2, row = 2)
    self.algoritmoBre = Radiobutton(self.master, text="Bresenham Líneas", font=("Arial", 18), value = "Bresenham Líneas", variable = algoritmo, command = self.seleccionado).grid(column = 3, row = 2)
    self.algoritmoMid = Radiobutton(self.master, text="Mid-Point Círculo", font=("Arial", 18), value = "Mid-Point Círculo", variable = algoritmo, command = self.seleccionado).grid(column = 4, row = 2)

    self.lIngreso = Label(self.master, text="Ingrese los puntos del espacio: ", font=("Arial", 18)).grid(column = 0, row = 4, columnspan = 8, sticky = W)


  def nuevasFilas(self) -> None:
    seleccionada = opcion.get()
    algoritmoEscogido = algoritmo.get()
    
    if((seleccionada == "2D" and algoritmoEscogido == "DDA") and self.fila < 2):
      self.fila = 2
      self.X2 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 7)
      self.X2E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X2E.grid(column = 1, row = 7)
      self.Y2 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 7)
      self.Y2E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y2E.grid(column = 3, row = 7)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 4, row = 7)
      self.bMas.grid_forget()
      
    if((seleccionada == "2D" and algoritmoEscogido == "Bresenham Líneas") and self.fila < 2):
      self.fila = 2
      self.X2 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 7)
      self.X2E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X2E.grid(column = 1, row = 7)
      self.Y2 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 7)
      self.Y2E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y2E.grid(column = 3, row = 7)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 4, row = 7)
      self.bMas.grid_forget()
      
    if((seleccionada == "3D" and algoritmoEscogido == "DDA") and self.fila < 2):
      self.fila = 2
      self.X4 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 7)
      self.X4E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X4E.grid(column = 1, row = 7)
      self.Y4 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 7)
      self.Y4E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y4E.grid(column = 3, row = 7)
      self.Z4 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 4, row = 7)
      self.Z4E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Z4E.grid(column = 5, row = 7)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 7)
      self.bMas.grid_forget()
      
    if((seleccionada == "3D" and algoritmoEscogido == "Bresenham Líneas") and self.fila < 2):
      self.X4 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 7)
      self.X4E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X4E.grid(column = 1, row = 7)
      self.Y4 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 7)
      self.Y4E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y4E.grid(column = 3, row = 7)
      self.Z4 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 4, row = 7)
      self.Z4E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Z4E.grid(column = 5, row = 7)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 7)
      self.bMas.grid_forget()

  def graficarDDA(self) -> None:
    self.bListo['state'] = DISABLED
    listaX = []
    listaY = []
    listaDDA = dda.dda(int(self.X1E.get()), int(self.Y1E.get()), int(self.X2E.get()), int(self.Y2E.get()))
    listaX = listaDDA.pop(0)
    listaY = listaDDA.pop(0)
    x = listaX
    y = listaY
    
    
    fig = plt.figure(figsize=(3, 4))
    plt.plot(x, y, linestyle = 'solid')
    plt.title("Gráfica DDA")
    plt.plot([int(self.X1E.get()), int(self.X2E.get())], [int(self.Y1E.get()), int(self.Y2E.get())])

    # Especificar nuestra ventana (master) como master
    canvas = FigureCanvasTkAgg(fig, master=self.master)
    canvas.draw()
    Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 0, row = 8, columnspan = 9)
    canvas.get_tk_widget().grid(row = 9, column = 3)

    #Barra de navegación
    toolbarFrame = Frame(master=self.master)
    toolbarFrame.grid(row = 10, column = 3)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) 
    
  def graficarBresenham(self) -> None:
    self.bListo['state'] = DISABLED
    listaX = []
    listaY = []
    listaBre = bresenham.bresenham(int(self.X1E.get()), int(self.Y1E.get()), int(self.X2E.get()), int(self.Y2E.get()))
    listaX = listaBre.pop(0)
    listaY = listaBre.pop(0)
    x = listaX
    y = listaY
    
    
    fig = plt.figure(figsize=(3, 4))
    plt.plot(x, y, linestyle = 'solid')
    plt.title("Gráfica Bresenham")
    plt.plot([int(self.X1E.get()), int(self.X2E.get())], [int(self.Y1E.get()), int(self.Y2E.get())])

    # Especificar nuestra ventana (master) como master
    canvas = FigureCanvasTkAgg(fig, master=self.master)
    canvas.draw()
    Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 0, row = 8, columnspan = 9)
    canvas.get_tk_widget().grid(row = 9, column = 3)

    #Barra de navegación
    toolbarFrame = Frame(master=self.master)
    toolbarFrame.grid(row = 10, column = 3)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) 
    
  def graficarMid(self) -> None:
    self.bListo['state'] = DISABLED
    listaX = []
    listaY = []
    listaDDA = dda.dda(int(self.X1E.get()), int(self.Y1E.get()), int(self.X2E.get()), int(self.Y2E.get()))
    listaX = listaDDA.pop(0)
    listaY = listaDDA.pop(0)
    x = listaX
    y = listaY
    
    
    fig = plt.figure(figsize=(3, 4))
    plt.plot(x, y, linestyle = 'solid')
    plt.title("Gráfica Mid-Point Circle")
    plt.plot([int(self.X1E.get()), int(self.X2E.get())], [int(self.Y1E.get()), int(self.Y2E.get())])

    # Especificar nuestra ventana (master) como master
    canvas = FigureCanvasTkAgg(fig, master=self.master)
    canvas.draw()
    Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 0, row = 8, columnspan = 9)
    canvas.get_tk_widget().grid(row = 9, column = 3)

    #Barra de navegación
    toolbarFrame = Frame(master=self.master)
    toolbarFrame.grid(row = 10, column = 3)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) 

  def deshabilitarbMas3D(self) -> None:
    self.bListo['state'] = DISABLED
    fig = plt.figure(figsize=(3, 4))
    ax = plt.axes(projection ='3d')
    
    # Especificar nuestra ventana (master) como master
    canvas = FigureCanvasTkAgg(fig, master=self.master)
    canvas.draw()
    
    canvas.get_tk_widget().grid(row = 9, column = 3)
    
    #Barra de navegación
    toolbarFrame = Frame(master=self.master)
    toolbarFrame.grid(row = 10, column = 3)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) 

  def seleccionado(self) -> None:
    seleccionada = opcion.get()
    algoritmoEscogido = algoritmo.get()
    
    if(seleccionada == "2D" and algoritmoEscogido == "DDA"):
      self.X1 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 6)
      self.X1E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X1E.grid(column = 1, row = 6)
      self.Y1 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 6)
      self.Y1E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y1E.grid(column = 3, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.bMas = Button(self.master, text = " + ", font=("Arial", 18), state = NORMAL, command = self.nuevasFilas)
      self.bMas.grid(column = 7, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.graficarDDA)
      self.bListo.grid(column = 8, row = 6)
      
    if(seleccionada == "2D" and algoritmoEscogido == "Bresenham Líneas"):
      self.X1 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 6)
      self.X1E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X1E.grid(column = 1, row = 6)
      self.Y1 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 6)
      self.Y1E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y1E.grid(column = 3, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.bMas = Button(self.master, text = " + ", font=("Arial", 18), state = NORMAL, command = self.nuevasFilas)
      self.bMas.grid(column = 7, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.graficarBresenham)
      self.bListo.grid(column = 8, row = 6)
      
    if(seleccionada == "2D" and algoritmoEscogido == "Mid-Point Círculo"):
      self.X1 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 6)
      self.X1E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X1E.grid(column = 1, row = 6)
      self.Y1 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 6)
      self.Y1E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y1E.grid(column = 3, row = 6)
      self.r = Label(self.master, text="r: ", width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.rE = Entry(self.master, width = 5, font=("Arial", 18))
      self.rE.grid(column = 5, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 7)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.graficarMid)
      self.bListo.grid(column = 8, row = 6)

    if(seleccionada == "3D" and algoritmoEscogido == "DDA"):
      self.X3 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 6)
      self.X3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X3E.grid(column = 1, row = 6)
      self.Y3 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 2, row = 6)
      self.Y3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y3E.grid(column = 3, row = 6)
      self.Z3 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.Z3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Z3E.grid(column = 5, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 6)
      self.bMas = Button(self.master, text = " + ", font=("Arial", 18), state = NORMAL, command = self.nuevasFilas)
      self.bMas.grid(column = 8, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.deshabilitarbMas3D)
      self.bListo.grid(column = 9, row = 6)
      
    if(seleccionada == "3D" and algoritmoEscogido == "Bresenham Líneas"):
      self.X3 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 0, row = 6)
      self.X3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X3E.grid(column = 1, row = 6)
      self.Y3 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 6)
      self.Y3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y3E.grid(column = 3, row = 6)
      self.Z3 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.Z3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Z3E.grid(column = 5, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 6)
      self.bMas = Button(self.master, text = " + ", font=("Arial", 18), state = NORMAL, command = self.nuevasFilas)
      self.bMas.grid(column = 8, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.deshabilitarbMas3D)
      self.bListo.grid(column = 9, row = 6)
      
    if(seleccionada == "3D" and algoritmoEscogido == "Mid-Point Círculo"):
      self.X3 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 1, row = 6)
      self.X3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.X3E.grid(column = 2, row = 6)
      self.Y3 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 6)
      self.Y3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Y3E.grid(column = 4, row = 6)
      self.Z3 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 5, row = 6)
      self.Z3E = Entry(self.master, width = 5, font=("Arial", 18))
      self.Z3E.grid(column = 6, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 7, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.deshabilitarbMas3D)
      self.bListo.grid(column = 9, row = 6)

    return seleccionada


if __name__ == "__main__":
  
    
    root = Tk()
    opcion = StringVar()
    opcion.set(value = None)
    algoritmo = StringVar()
    algoritmo.set(value = None)
    #Título
    root.title("Ejercicio 04")
  
    #Tamaños
    root.geometry("1400x800")
    root.resizable(True, True)
    root.grid()
  
    #Llamar App
    app = App(root)
  
    #Mainloop
    root.mainloop()