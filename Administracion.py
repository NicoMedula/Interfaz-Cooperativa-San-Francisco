import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ast
from tkinter import ttk
from Pagina2 import *
import mysql.connector


def ventanaAdministracion():
    global App6
    App6=tk.Toplevel()
    App6.geometry("925x500+300+200")
    App6.configure(background="gray14")
    App6.title("Administracion")
    Recuadro()
    

def Recuadro():
    cuadro= CTkFrame(master=App6, fg_color="#8D6F3A", border_color="#FFCC70",border_width=2)
    cuadro.pack(expand=True)
    cuadro.place(rely=0.2,relx=0.5)
    
    CTkButton(master=cuadro, text="Ingreso de productos",fg_color="#FFA500",hover_color="#FF4500").pack(expand=True,padx=30,pady=20)               
    CTkButton(master=cuadro, text="Stock general",fg_color="#FFA500",hover_color="#FF4500").pack(expand=True,padx=30,pady=20)
    CTkButton(master=cuadro, text="Camiones",fg_color="#FFA500",hover_color="#FF4500", command= ventanaCamiones).pack(expand=True,padx=30,pady=20)
    

    
    headtexto=Label(App6,text="Secciones",fg="orange2",bg="gray14",font=("Microsoft Yahei UI Light",23,"bold"))
    headtexto.place(relx=0.55,rely=0.1)
  

def insertarCamiones(marca, carga):
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="camiones")
        cursor = conn.cursor()

        
        query = "INSERT INTO camiones2 (Marca, Carga) VALUES (%s, %s)"
        data = (marca, carga)
        cursor.execute(query, data)

        
        query2 = "SELECT * FROM camiones2"
        cursor.execute(query2)
        records = cursor.fetchall()

        
        ResultadoTexto.delete(1.0, tk.END)

        
        ResultadoTexto.insert(tk.END, "Camiones registrados:\n")
        for record in records:
            ResultadoTexto.insert(tk.END, f"ID: {record[0]}\n")
            ResultadoTexto.insert(tk.END, f"Marca: {record[1]}\n")
            ResultadoTexto.insert(tk.END, f"Carga: {record[2]}\n\n")

        conn.commit()
        

    except Exception as e:
        ResultadoTexto.insert(tk.END, f"Error: {e}\n")

    finally:
       
        cursor.close()
        conn.close()

def on_submit():
    marca = entradamarca.get()
    carga = entradacarga.get()
    insertarCamiones(marca, carga)



def ventanaCamiones():
    set_appearance_mode("System")  
    set_default_color_theme("blue")  

    AppCa = CTk()
    AppCa.title("Registro de Camiones")
    AppCa.geometry("800x600")

    global entradacarga
    global entradamarca
    global ResultadoTexto

    labelMarca = CTkLabel(AppCa, text="Marca del Camión:")
    labelMarca.pack(pady=5)
    entradamarca = CTkEntry(AppCa)
    entradamarca.pack(pady=5)

    labelCarga = CTkLabel(AppCa, text="Carga que lleva:")
    labelCarga.pack(pady=5)
    entradacarga = CTkEntry(AppCa)
    entradacarga.pack(pady=5)


    BotonRegis = CTkButton(AppCa, text="Registrar Camión", command=on_submit)
    BotonRegis.pack(pady=20)


    cuadroTexto = CTkFrame(AppCa)
    cuadroTexto.pack(pady=20, fill='both', expand=True)


    ResultadoTexto = CTkTextbox(cuadroTexto, wrap='word', height=10)
    ResultadoTexto.pack(side='left', fill='both', expand=True, padx=(20, 0))


    scrollbar = CTkScrollbar(cuadroTexto, command=ResultadoTexto.yview)
    scrollbar.pack(side='right', fill='y')


    ResultadoTexto.configure(yscrollcommand=scrollbar.set)


    AppCa.mainloop()