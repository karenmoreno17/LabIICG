from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class App:
  def __init__(self, master) -> None:
  
    # Instantiating master 
    self.master = master


    self.click = 0

    self.lOpcion = Label(self.master, text="Seleccione el tamaño del espacio ordenado (2D o 3D): ", font=("Arial", 18)).grid(column = 1, row = 1, columnspan = 4)

    self.radio1 = Radiobutton(self.master, text="2D", font=("Arial", 18), value = "2D", variable = opcion, command = self.seleccionado).grid(column = 5, row = 1)
    self.radio2 = Radiobutton(self.master, text="3D", font=("Arial", 18), value = "3D", variable = opcion, command = self.seleccionado).grid(column = 6, row = 1)
    self.lIngreso = Label(self.master, text="Ingrese los puntos del espacio: ", font=("Arial", 18)).grid(column = 1, row = 4, columnspan = 8, sticky = W)


  def nuevasFilas(self) -> None:
    self.click += 1
    seleccionada = opcion.get()
    if(seleccionada == "2D"):
      self.X2 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 1, row = 6 + self.click)
      self.X2 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 2, row = 6 + self.click)
      self.Y2 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 6 + self.click)
      self.Y2 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 4, row = 6 + self.click)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 5, row = 6 + self.click)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 6 + self.click)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 7, row = 6 + self.click)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 1, row = 7 + self.click) 

    if(seleccionada == "3D"):
      self.X3 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 1, row = 6 + self.click)
      self.X3 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 2, row = 6 + self.click)
      self.Y3 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 6 + self.click)
      self.Y3 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 4, row = 6 + self.click)
      self.Z3 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 5, row = 6 + self.click)
      self.Z3 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 6, row = 6 + self.click)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 7, row = 6 + self.click)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 1, row = 7 + self.click)

  def deshabilitarbMas2D(self) -> None:
    self.bMas.grid_forget()
    self.bListo['state'] = DISABLED
    x = ['Col A', 'Col B', 'Col C']

    y = [30, 20, 15]
    fig = plt.figure(figsize=(3, 4))
    plt.bar(x=x, height=y)

    # Especificar nuestra ventana (master) como master
    canvas = FigureCanvasTkAgg(fig, master=self.master)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 9 + self.click, column = 4)

    #Barra de navegación
    toolbarFrame = Frame(master=self.master)
    toolbarFrame.grid(row = 10 + self.click, column = 4)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) 

  def deshabilitarbMas3D(self) -> None:
    self.bMas.grid_forget()
    self.bListo['state'] = DISABLED
    fig = plt.figure(figsize=(3, 4))
    ax = plt.axes(projection ='3d')
    
    # Especificar nuestra ventana (master) como master
    canvas = FigureCanvasTkAgg(fig, master=self.master)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 9 + self.click, column = 4)
    
    #Barra de navegación
    toolbarFrame = Frame(master=self.master)
    toolbarFrame.grid(row = 10 + self.click, column = 4)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) 

  def seleccionado(self) -> None:
    seleccionada = opcion.get()
    
    if(seleccionada == "2D"):
      self.X2 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 1, row = 6)
      self.X2 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 2, row = 6)
      self.Y2 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 6)
      self.Y2 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 5, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 6, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 7, row = 6)
      self.bMas = Button(self.master, text = " + ", font=("Arial", 18), state = NORMAL, command = self.nuevasFilas)
      self.bMas.grid(column = 8, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.deshabilitarbMas2D)
      self.bListo.grid(column = 9, row = 6)

    if(seleccionada == "3D"):
      self.X3 = Label(self.master, text="X: ", width = 5, font=("Arial", 18)).grid(column = 1, row = 6)
      self.X3 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 2, row = 6)
      self.Y3 = Label(self.master, text="Y: ", width = 5, font=("Arial", 18)).grid(column = 3, row = 6)
      self.Y3 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 4, row = 6)
      self.Z3 = Label(self.master, text="Z: ", width = 5, font=("Arial", 18)).grid(column = 5, row = 6)
      self.Z3 = Entry(self.master, width = 5, font=("Arial", 18)).grid(column = 6, row = 6)
      self.lAux = Label(self.master, text=" ", width = 5, font=("Arial", 18)).grid(column = 7, row = 6)
      self.bMas = Button(self.master, text = " + ", font=("Arial", 18), state = NORMAL, command = self.nuevasFilas)
      self.bMas.grid(column = 8, row = 6)
      self.bListo = Button(self.master, text = " ✓", font=("Arial", 18), command = self.deshabilitarbMas3D)
      self.bListo.grid(column = 9, row = 6)

    return seleccionada


if __name__ == "__main__":
  
    
    root = Tk()
    opcion = StringVar()
    opcion.set(value = None)
    #Título
    root.title("Ejercicio 04")
  
    #Tamaños
    root.geometry("1000x800")
    root.resizable(True, True)
    root.grid()
  
    #Llamar App
    app = App(root)
  
    #Mainloop
    root.mainloop()