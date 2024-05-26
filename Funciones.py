import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ast
from tkintermapview import TkinterMapView

def Abrirnueva ():
    App2=tk.Toplevel()
    App2.geometry("925x500+300+200")
    App2.configure(background="gray14")
    App2.title("Pagina 2")
    BotonMosMapa = CTkButton(master=App2, text="Mostrar Ubi en el Mapa", corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500",command=abrirMapa)# Boton de "Inicio de sesion"
    BotonMosMapa.place(relx=0.5,rely=0.5, anchor="center")

def abrirMapa():
    Mapa=tk.Toplevel()
    Mapa.geometry("925x500+300+200")
    Mapa.title("Mapa")

    map_widget= TkinterMapView(Mapa,width=100,height=100)
    map_widget.pack(fill="both",expand=True)
    
    map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
    map_widget.set_position(-32.97148, -60.62084)  
    map_widget.set_zoom(12) 