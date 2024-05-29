import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ast
from Pagina2 import *
from tkinter import ttk

def tablaAceitesEsenciales():
    global ventanaAceites
    ventanaAceites=tk.Toplevel()
    ventanaAceites.geometry("925x500+300+200")
    ventanaAceites.configure(background="gray14")
    ventanaAceites.title("Aceites")

    arbol=ttk.Treeview(ventanaAceites, columns=( "Precio", "Cantidad") )
    arbol.insert("",END,text=" Aceite Naranja",values=( "2000", "1"))
    arbol.insert("",END,text="Aceite Limon",values=( "2350", "1"))
    arbol.insert("",END,text="Aceite Mandarina",values=( "2100", "1"))
    arbol.insert("",END,text="Aceite Pomelo",values=( "2500", "1"))

    arbol.place(relx=0.5,rely=0.5,anchor="center")

    arbol.heading("#0",text="Aceites")
    arbol.heading("#1",text="Precio")
    arbol.heading("#2",text="Cantidad")


def tablaJugos():
    global ventanaJugos
    ventanaJugos=tk.Toplevel()
    ventanaJugos.geometry("925x500+300+200")
    ventanaJugos.configure(background="gray14")
    ventanaJugos.title("Jugos")

    arbol=ttk.Treeview(ventanaJugos, columns=( "Precio", "Cantidad") )
    arbol.insert("",END,text=" Jugo Naranja",values=( "1500", "1"))
    arbol.insert("",END,text="Jugo Limon",values=( "1800", "1"))
    arbol.insert("",END,text="Jugo Mandarina",values=( "1650", "1"))
    arbol.insert("",END,text="Jugo Pomelo",values=( "2100", "1"))

    arbol.place(relx=0.5,rely=0.5,anchor="center")

    arbol.heading("#0",text="Jugos")
    arbol.heading("#1",text="Precio")
    arbol.heading("#2",text="Cantidad")


def tablaFrutas():
    global ventanaFruta
    ventanaFruta=tk.Toplevel()
    ventanaFruta.geometry("925x500+300+200")
    ventanaFruta.configure(background="gray14")
    ventanaFruta.title("Frutas")

    arbol=ttk.Treeview(ventanaFruta, columns=( "Precio", "Cantidad") )
    arbol.insert("",END,text="Naranja",values=( "300", "1"))
    arbol.insert("",END,text="Limon",values=( "250", "1"))
    arbol.insert("",END,text="Mandarina",values=( "200", "1"))
    arbol.insert("",END,text="Pomelo",values=( "400", "1"))

    arbol.place(relx=0.5,rely=0.5,anchor="center")

    arbol.heading("#0",text="Fruta")
    arbol.heading("#1",text="Precio")
    arbol.heading("#2",text="Cantidad")


def VentanaNuevaP():
    global App3
    App3=tk.Toplevel()
    App3.geometry("925x500+300+200")
    App3.configure(background="gray14")
    App3.title("Procesos Productivos")

    
    cuadro= CTkFrame(master=App3, fg_color="#8D6F3A", border_color="#FFCC70",border_width=2)
    cuadro.pack(expand=True)
    cuadro.place(rely=0.075,relx=0.5)
    
    CTkButton(master=cuadro, text="Frutas",fg_color="#FFA500",hover_color="#FF4500",command=tablaFrutas).pack(expand=True,padx=30,pady=20)               
    CTkButton(master=cuadro, text="Jugos",fg_color="#FFA500",hover_color="#FF4500",command=tablaJugos).pack(expand=True,padx=30,pady=20)
    CTkButton(master=cuadro, text="Aceites Esenciales",fg_color="#FFA500",command=tablaAceitesEsenciales,hover_color="#FF4500").pack(expand=True,padx=30,pady=20)

