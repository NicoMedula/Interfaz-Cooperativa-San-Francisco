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

    img_path = "C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/logo.png"
    img3 = Image.open(img_path)
    img3 = img3.resize((250, 250), Image.LANCZOS)
    photo_img3 = ImageTk.PhotoImage(img3)

    Labelimg3 = tk.Label(App6, image=photo_img3, border=0,bg="gray14")
    Labelimg3.image = photo_img3  
    Labelimg3.place(relx=0.2, rely=0.73, anchor="center")
    

def Recuadro():
    cuadro= CTkFrame(master=App6, fg_color="#8D6F3A", border_color="#FFCC70",border_width=2)
    cuadro.pack(expand=True)
    cuadro.place(rely=0.2,relx=0.5)
    
    CTkButton(master=cuadro, text="Ingreso de productos",fg_color="#FFA500",hover_color="#FF4500",command=ventanaProveedores).pack(expand=True,padx=30,pady=20)               
    CTkButton(master=cuadro, text="Stock general",fg_color="#FFA500",hover_color="#FF4500",command=mostrarFrutaCantidad).pack(expand=True,padx=30,pady=20)
    CTkButton(master=cuadro, text="Camiones",fg_color="#FFA500",hover_color="#FF4500", command= ventanaCamiones).pack(expand=True,padx=30,pady=20)
    

    
    headtexto=Label(App6,text="Secciones",fg="orange2",bg="gray14",font=("Microsoft Yahei UI Light",23,"bold"))
    headtexto.place(relx=0.55,rely=0.1)

  #BASE DE DATOS PARA LOS CAMIONES
###################################################################################################################
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
            ResultadoTexto.insert(tk.END, f"Marca: {record[1]}\n")
            ResultadoTexto.insert(tk.END, f"Carga: {record[2]}\n\n")

        conn.commit()
        

    except Exception as e:
        ResultadoTexto.insert(tk.END, f"Error: {e}\n")

    finally:
       
        cursor.close()
        conn.close()

def CargarCamion():
    marca = entradamarca.get()
    carga = entradacarga.get()
    insertarCamiones(marca, carga)



def ventanaCamiones():
    set_appearance_mode("System")  
    

    AppCa = CTk()
    AppCa.title("Registro de Camiones")
    AppCa.geometry("800x600")


    global entradacarga
    global entradamarca
    global ResultadoTexto

    labelMarca = CTkLabel(AppCa,text="Ingrese la marca del camion")
    labelMarca.pack(pady=5)
    entradamarca = CTkEntry(AppCa)
    entradamarca.pack(pady=5)

    labelCarga = CTkLabel(AppCa,text="Ingrese la carga del camion")
    labelCarga.pack(pady=5)
    entradacarga = CTkEntry(AppCa)
    entradacarga.pack(pady=5)


    BotonRegis = CTkButton(master=AppCa, text="Registrar", corner_radius=32,fg_color="#FFA500",
                             hover_color="#FF4500", command=CargarCamion)
    
    BotonRegis.pack(pady=20)


    cuadroTexto = CTkFrame(AppCa)
    cuadroTexto.pack(pady=20, fill='both', expand=True)


    ResultadoTexto = CTkTextbox(cuadroTexto, wrap='word', height=10)
    ResultadoTexto.pack(side='left', fill='both', expand=True, padx=(20, 0))


    scrollbar = CTkScrollbar(cuadroTexto, command=ResultadoTexto.yview)
    scrollbar.pack(side='right', fill='y')

    ResultadoTexto.configure(yscrollcommand=scrollbar.set)
    AppCa.mainloop()
    ##################################################################################################################




    #BASE DE DATOS PARA PRVEEDORES
    ##################################################################################################################

def insertarProveedor(nombre, fruta, cantidad, precio):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="camiones")
        cursor = conn.cursor()

        query = "INSERT INTO proveedores (Proveedor, Fruta, Cantidad, Precio) VALUES (%s, %s, %s, %s)"
        data = (nombre, fruta, cantidad, precio)
        cursor.execute(query, data)

        query2 = "SELECT * FROM proveedores"
        cursor.execute(query2)
        records = cursor.fetchall()

        ResultadoTexto.delete(1.0, tk.END)
        ResultadoTexto.insert(tk.END, "Proveedores registrados:\n")
        for record in records:
            ResultadoTexto.insert(tk.END, f"Proveedor: {record[1]}\n")
            ResultadoTexto.insert(tk.END, f"Fruta: {record[2]}\n")
            ResultadoTexto.insert(tk.END, f"Cantidad: {record[3]}\n")
            ResultadoTexto.insert(tk.END, f"Precio: {record[4]}\n\n")

        conn.commit()

    except Exception as e:
        ResultadoTexto.insert(tk.END, f"Error: {e}\n")

    finally:
        cursor.close()
        conn.close()

def CargarProvee():
    nombre = entradaNombre.get()
    fruta = entradaFruta.get()
    cantidad= entradaCantidad.get()
    precio= entradaPrecio.get()

    insertarProveedor(nombre, fruta, cantidad, precio)

def ventanaProveedores():

    root = CTk()
    root.title("Registro de Proveedores")
    root.geometry("800x600")

    global entradaCantidad
    global entradaFruta
    global entradaNombre
    global entradaPrecio
    global ResultadoTexto

    labelNombre = CTkLabel(root, text="Nombre de proovedor")
    labelNombre.pack(pady=5)
    entradaNombre = CTkEntry(root)
    entradaNombre.pack(pady=5)

    labelFruta = CTkLabel(root, text="Ingrese la fruta")
    labelFruta.pack(pady=5)
    entradaFruta = CTkEntry(root)
    entradaFruta.pack(pady=5)

    labelCantidad= CTkLabel(root, text="Cantidad de frutas")
    labelCantidad.pack(pady=5)
    entradaCantidad = CTkEntry(root)
    entradaCantidad.pack(pady=5)

    labelPrecio= CTkLabel(root, text="Ingrese el precio")
    labelPrecio.pack(pady=5)
    entradaPrecio = CTkEntry(root)
    entradaPrecio.pack(pady=5)

    BotonRegistrar = CTkButton(root, text="Registrar Proveedor",corner_radius=32,fg_color="#FFA500",
                             hover_color="#FF4500", command=CargarProvee)
    BotonRegistrar.pack(pady=20)


    CuadroTexto = CTkFrame(root)
    CuadroTexto.pack(pady=20, fill='both', expand=True)


    ResultadoTexto = CTkTextbox(CuadroTexto, wrap='word', height=10)
    ResultadoTexto.pack(side='left', fill='both', expand=True, padx=(20, 0))


    scrollbar = CTkScrollbar(CuadroTexto, command=ResultadoTexto.yview)
    scrollbar.pack(side='right', fill='y')


    ResultadoTexto.configure(yscrollcommand=scrollbar.set)


    root.mainloop()
    ##################################################################################################################

#STOCK DE FRUTAS
##################################################################################################################
def mostrarFrutaCantidad():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="camiones")
        cursor = conn.cursor()

        query = "SELECT Proveedor, Fruta, Cantidad FROM proveedores"
        cursor.execute(query)
        records = cursor.fetchall()

        ventana = tk.Tk()
        ventana.title("Stock")

        
        ResultadoTexto = tk.Text(ventana, height=10, width=50)
        ResultadoTexto.pack()

        ResultadoTexto.insert(tk.END, "Proveedor\t\t\tFruta\t\tCantidad\n")
        ResultadoTexto.insert(tk.END, "--------------------------------------------------\n")
        for record in records:
            ResultadoTexto.insert(tk.END, f"{record[0]}\t\t\t{record[1]}\t\t{record[2]}\n")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()