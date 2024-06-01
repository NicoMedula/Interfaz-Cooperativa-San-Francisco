import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ast
from Pagina2 import *
from ProcesosProd import *
from customtkinter import CTk

#############----------------------------------------------------------------------------------------
def Validar():

    with open("registro.txt", "r") as Archivo:
            lines = Archivo.readlines()

            for i in range(0, len(lines), 2):
                guardar_usuario = lines[i].strip()
                guardar_contra = lines[i+1].strip()
                if usuario.get() == guardar_usuario and contra.get() == guardar_contra:
                    abrirventana2()
                    return
                else:
                     messagebox.showerror("cuidado","Contraseña o mail incorrecto")

#############----------------------------------------------------------------------------------------


def abrirventana2():
    App.withdraw()
    Abrirnueva()

#############----------------------------------------------------------------------------------------

def GuardarArchivo():
    Archivo=open("registro.txt", "w")
    Archivo.write(usuario2.get() + "\n")
    Archivo.write(contra2.get() + "\n")
    Archivo.close()

###############################################----------------------------------------------------
def registrarUser():
    App5=CTk()
    App5.geometry("300x300")#Tamaño de la ventana de Tkinter
    App5.configure(bg="#fff")
    App5.title("Register")
    global usuario2
    global contra2

    usuario2=CTkEntry(master=App5, placeholder_text="Ingrese su usuario", width=200,font=("bold",12)) #Ingresa el mail
    usuario2.place(relx=0.5,rely=0.3, anchor="center")

    contra2=CTkEntry(master=App5, placeholder_text="Ingrese su contraseña", width=200,font=("bold",12),show="*") #Ingresa la contraseña
    contra2.place(relx=0.5,rely=0.4, anchor="center")

    BotonSumbit = CTkButton(master=App5, text="Registrarse",command=GuardarArchivo, corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500")
    BotonSumbit.place(relx=0.5,rely=0.5, anchor="center")

    App5.mainloop()


    


###############################################----------------------------------------------------

App=CTk()
App.geometry("925x500+300+200")#Tamaño de la ventana de Tkinter
App.configure(bg="#fff")
App.title("Sign Up")

#############----------------------------------------------------------------------------------------

img = PhotoImage(file="C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/logo.png") #se importa la foto de la cooperativa
Label(App,image=img,border=0,bg="gray14").place(relx=0.22,rely=0.5,anchor="center")#formato y ubicacion de la foto


#############----------------------------------------------------------------------------------------

frame=Frame(App,width=350,height=390,bg="gray14") #recuadro de inicio de sesion
frame.place(relx=0.6,rely=0.5,anchor="center")


#########-------------------------------------------------------------------------------------------------------
img2 = Image.open("C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/visible.png")
img2 = img2.resize((40, 40), Image.LANCZOS)  
img2 = ImageTk.PhotoImage(img2)
Labelimg2=Label(master=App, image=img2, border=0, bg="gray14")
Labelimg2.place(relx=0.73, rely=0.4, anchor="center")

#########-------------------------------------------------------------------------------------------------------

img3 = Image.open("C:/Users/nicol/OneDrive/Escritorio/TPI Interfaz/Imagen/user.png")
img3 = img3.resize((40, 40), Image.LANCZOS)  
img3 = ImageTk.PhotoImage(img3)
Labelimg3=Label(master=App, image=img3, border=0, bg="gray14")
Labelimg3.place(relx=0.73, rely=0.3, anchor="center")

#########-------------------------------------------------------------------------------------------------------

headtexto=Label(frame,text="Sign Up",fg="orange2",bg="gray14",font=("Microsoft Yahei UI Light",23,"bold"))
headtexto.place(x=100,y=0)


#############----------------------------------------------------------------------------------------


BotonIS = CTkButton(master=App, text="Iniciar sesion", corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500",command=Validar)# Boton de "Inicio de sesion"
BotonIS.place(relx=0.6,rely=0.7, anchor="center")#Posicion de boton "Inicio de sesion"

BotonRG = CTkButton(master=App, text="Registrarse",command=registrarUser, corner_radius=32,fg_color="#FFA500",
                   hover_color="#FF4500")
BotonRG.place(relx=0.6,rely=0.8, anchor="center")

CajaOpcion= CTkComboBox(master=App, values=["AMERICA","EU","ASIA"],fg_color="#FFA500",corner_radius=32,dropdown_fg_color="#FFA500")#Caja de opciones
CajaOpcion.place(relx=0.6,rely=0.5, anchor="center")#Posicion de la caja de opciones

CajaCheck= CTkCheckBox(master=App,text="No soy robot",fg_color="#FFA500",checkbox_height=30,corner_radius=36,checkbox_width=30) #check de robot
CajaCheck.place(relx=0.6,rely=0.6, anchor="center")

usuario=CTkEntry(master=App, placeholder_text="Ingrese su usuario", width=200,font=("bold",12)) #Ingresa el mail
usuario.place(relx=0.6,rely=0.3, anchor="center")

contra=CTkEntry(master=App, placeholder_text="Ingrese su contraseña", width=200,font=("bold",12),show="*") #Ingresa la contraseña
contra.place(relx=0.6,rely=0.4, anchor="center")



#############----------------------------------------------------------------------------------------













App.mainloop()