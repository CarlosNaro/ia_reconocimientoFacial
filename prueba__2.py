from cProfile import label
from tkinter import *

#global pantalla
pantalla = Tk()
pantalla.geometry("300x250")  #Asignamos el tamaño de la ventana 
pantalla.title("Registro de Alumno")    #Asignamos el titulo de la pantalla
Label(text = "Registrar Nombre", bg = "gray", width = "300", height = "2", font = ("Verdana", 13)).pack() #Asignamos caracteristicas de la ventana

#creacionde botones
username = Label(text = "Usuario * ").pack()
username = StringVar()
username_entry = Entry(textvariable=username)
username_entry.pack()

def send_data():
    username_data = username.get()
    print(f"Alumno : {username_data} / Registrado")
#usuario_entrada2.pack()
submit = Button(pantalla, text = "Registrar", width = 20, height = 1, bg="#00CD63", command = send_data).pack()

pantalla.mainloop()

