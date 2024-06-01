import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ast
from tkintermapview import TkinterMapView
from ProcesosProd import VentanaNuevaP
from Exportacion import VentanaExport

App2=None
App3=None

def abrirExport():
    global App2
    VentanaExport()



def abrirPprod():
    global App2
    VentanaNuevaP()
    
def Abrirnueva():
    global App2
    App2=tk.Toplevel()
    App2.geometry("925x500+300+200")
    App2.configure(background="gray14")
    App2.title("Pagina 2")

    cuadroScroll(App2)


    BotonMosMapaPR = CTkButton(master=App2, text="Mostrar ubicacin del puerto de Rosario", corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500",command=abrirMapaPuerto)# Boton de la ubi del puerto
    BotonMosMapaPR.place(relx=0.17,rely=0.4, anchor="center")

    BotonMosMapaCoop = CTkButton(master=App2, text="Mostrar Ubicacin da la Cooperativa", corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500",command=AbrirMapaCoop)# Boton de la ubi de la coop
    BotonMosMapaCoop.place(relx=0.17,rely=0.3, anchor="center")

   ##############################--------------------------------------------------------------
    img_path = "C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/location-pin.png"
    img3 = Image.open(img_path)
    img3 = img3.resize((40, 40), Image.LANCZOS)
    photo_img3 = ImageTk.PhotoImage(img3)

    Labelimg3 = tk.Label(App2, image=photo_img3, border=0,bg="gray14")
    Labelimg3.image = photo_img3  
    Labelimg3.place(relx=0.35, rely=0.3, anchor="center")
   ##############################--------------------------------------------------------------
    img_path = "C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/location-pin.png"
    img3 = Image.open(img_path)
    img3 = img3.resize((40, 40), Image.LANCZOS)
    photo_img3 = ImageTk.PhotoImage(img3)

    Labelimg3 = tk.Label(App2, image=photo_img3, border=0,bg="gray14")
    Labelimg3.image = photo_img3  
    Labelimg3.place(relx=0.36, rely=0.4, anchor="center")
    
    ##############################--------------------------------------------------------------

    img_path = "C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/project-management.png"
    img3 = Image.open(img_path)
    img3 = img3.resize((40, 40), Image.LANCZOS)
    photo_img3 = ImageTk.PhotoImage(img3)

    Labelimg3 = tk.Label(App2, image=photo_img3, border=0,bg="gray14")
    Labelimg3.image = photo_img3  
    Labelimg3.place(relx=0.80, rely=0.25, anchor="center")

    #############################################33-------------------------------------------------------

    img_path = "C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/logo.png"
    img3 = Image.open(img_path)
    img3 = img3.resize((250, 250), Image.LANCZOS)
    photo_img3 = ImageTk.PhotoImage(img3)

    Labelimg3 = tk.Label(App2, image=photo_img3, border=0,bg="gray14")
    Labelimg3.image = photo_img3  
    Labelimg3.place(relx=0.2, rely=0.73, anchor="center")

    #############################################3----------------------------------------------------------

    

def abrirMapaPuerto():
    Mapa=tk.Toplevel()
    Mapa.geometry("925x500+300+200")
    Mapa.title("Mapa")

    mapa_widget= TkinterMapView(Mapa,width=100,height=100)
    mapa_widget.pack(fill="both",expand=True)
    
    mapa_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
    mapa_widget.set_position(-32.97148, -60.62084)  
    mapa_widget.set_address("Puerto Rosario",marker=True)
    mapa_widget.set_zoom(16) 
    
def AbrirMapaCoop():

    Mapa=tk.Toplevel()
    Mapa.geometry("925x500+300+200")
    Mapa.title("Mapa")

    mapa_widget= TkinterMapView(Mapa,width=100,height=100)
    mapa_widget.pack(fill="both",expand=True)
    
    mapa_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
    mapa_widget.set_position(-30.3305999, -57.8003410)  
    mapa_widget.set_address("Cooperativa San Francisco, Monte Caseros, Corrientes",marker=True)
    mapa_widget.set_zoom(16)


def cuadroScroll(App2):
    cuadro= CTkFrame(master=App2, fg_color="#8D6F3A", border_color="#FFCC70",border_width=2)
    cuadro.pack(expand=True)
    cuadro.place(rely=0.2,relx=0.5)
    
    CTkButton(master=cuadro, text="Proc. Produc.",fg_color="#FFA500",hover_color="#FF4500",command=abrirPprod).pack(expand=True,padx=30,pady=20)               
    CTkButton(master=cuadro, text="Exportaciones",fg_color="#FFA500",hover_color="#FF4500",command=VentanaExport()).pack(expand=True,padx=30,pady=20)
    CTkButton(master=cuadro, text="Texto 3",fg_color="#FFA500",hover_color="#FF4500").pack(expand=True,padx=30,pady=20)
    
    headtexto=Label(App2,text="Secciones",fg="orange2",bg="gray14",font=("Microsoft Yahei UI Light",23,"bold"))
    headtexto.place(relx=0.55,rely=0.1)