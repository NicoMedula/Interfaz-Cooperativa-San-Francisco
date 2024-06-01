import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ast
from tkinter import ttk
from Pagina2 import *
import openpyxl as xl

##############################################--------------------------------------

def Limpiar():
    nombreprod.delete(0,END)
    cantprod.delete(0,END)

##############################################--------------------------------------

def cargarPedido():
    archivo=xl.load_workbook("Data.xlsx")
    hoja1=archivo["Hoja1"]
    valorProd=nombreprod.get()
    valorCat=categorias.get()
    valorCantidad=cantprod.get()
    hoja1.cell(column=1,row=hoja1.max_row+1,value=valorProd)
    hoja1.cell(column=2,row=hoja1.max_row,value=valorCantidad)
    hoja1.cell(column=3,row=hoja1.max_row,value=valorCat)
    archivo.save("Data.xlsx")
    messagebox.showinfo(title="Cargado",message="Se cargo el pedido!")
#######################################################################---------------------------------------
def mostrarPedidos():
    App = tk.Toplevel()
    App.geometry("925x500+300+200")
    App.configure(background="gray14")
    App.title("Mis Pedidos")

    Arbol = ttk.Treeview(App, columns=("Producto", "Cantidad", "Categoría","Precio"), show='headings')
    Arbol.heading("Producto", text="Producto")
    Arbol.heading("Cantidad", text="Cantidad")
    Arbol.heading("Categoría", text="Categoría")
    Arbol.heading("Precio", text="Precio")
    Arbol.pack(expand=True, fill='both')

    archivo = xl.load_workbook("Data.xlsx")
    hoja = archivo["Hoja1"]
    
    for row in hoja.iter_rows(min_row=2, values_only=True):  
        Arbol.insert("", tk.END, values=row)

##############################################--------------------------------------
def realizarpedido():
    App=tk.Toplevel()
    App.geometry("925x500+300+200")
    App.configure(background="gray14")
    App.title("Exportaciones")

    global nombreprod
    global categorias
    global cantprod

    categorias=CTkComboBox(App,values=["Aceite","Frutas","Jugos"],fg_color="#FFA500",corner_radius=32,dropdown_fg_color="#FFA500")
    categorias.place(relx=0.6,rely=0.5, anchor="center")

    nombreprod=CTkEntry(master=App, placeholder_text="Ingrese el producto", width=200,font=("bold",12)) 
    nombreprod.place(relx=0.6,rely=0.3, anchor="center")

    cantprod=CTkEntry(master=App, placeholder_text="Ingrese cantidad", width=200,font=("bold",12)) 
    cantprod.place(relx=0.6,rely=0.4, anchor="center")

    Botonrealizar=(CTkButton(master=App, text="Realizar pedido", corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500",command=cargarPedido))
    Botonrealizar.place(relx=0.6,rely=0.8, anchor="center")

    BotonLimpiar=CTkButton(master=App, text="Limpiar", corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500",command=Limpiar)
    BotonLimpiar.place(relx=0.6,rely=0.9, anchor="center")


def cuadroScroll():
    cuadro= CTkFrame(master=App4, fg_color="#8D6F3A", border_color="#FFCC70",border_width=2)
    cuadro.pack(expand=True)
    cuadro.place(rely=0.2,relx=0.5)
    
    CTkButton(master=cuadro, text="Mis pedidos",fg_color="#FFA500",hover_color="#FF4500",command=mostrarPedidos).pack(expand=True,padx=30,pady=20)               
    CTkButton(master=cuadro, text="Realizar pedido",fg_color="#FFA500",hover_color="#FF4500",command=realizarpedido).pack(expand=True,padx=30,pady=20)
    CTkButton(master=cuadro, text="Seguir mi pedido",fg_color="#FFA500",hover_color="#FF4500").pack(expand=True,padx=30,pady=20)
    
    headtexto=Label(App4,text="Secciones",fg="orange2",bg="gray14",font=("Microsoft Yahei UI Light",23,"bold"))
    headtexto.place(relx=0.55,rely=0.1)

def VentanaExport():
    global App4
    App4=tk.Toplevel()
    App4.geometry("925x500+300+200")
    App4.configure(background="gray14")
    App4.title("Exportaciones")
    cuadroScroll()




