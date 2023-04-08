#importaciones de las librerias necesarias 
import cv2 
import os
import imutils

from cProfile import label
from tkinter import *
#:::::::::::::::::::::::::

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

#:::::::::::::::::::::::::

def send_data():
    username_data = username.get()
    print(f"Alumno : {username_data} / Registrado")
    
    #asignamos nombre a la carpeta donde se almacenara los datos

    namePerson =  username_data

    #namePerson  = input("¿Cómo se llama? ")

    # dataPath = 'C:/Users/Developer/Desktop/Proyecto/data'
    dataPath = 'E:\Desarrollo_Software\Python-IA\ia_reconocimientoFacial\Data' # la ruta donde se almacenara la data del usario registrado

    personPath = dataPath + '/' + namePerson

    #en caso no existir la carpeta con ese nombre la crearemos automatiucamente 
    if not os.path.exists(personPath):
        print('Carpeta Creada: ', personPath)
        os.makedirs(personPath)

    print('carpeta creada : ', namePerson)

    #obtener referencia a la camara de la maquina
    #cap = cv2.VideoCapture('alonso.mp4')
    cap = cv2.VideoCapture(0)

    # referencia al haarcascade para poder trabajar con el detector de rostro
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    print('Detectado')
    count = 0

    # algoritmo encargado de leer cada fotograma de la imagen  

    while True: 
        ret,img = cap.read()
        if ret == False: break
        img = imutils.resize(img, width=640)
        #conversion a escala de grices 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        auxImg = img.copy()


        #almacenara todas las caras detectadas por el programa 
        faces = faceClassif.detectMultiScale(gray, 1.1,4)
        #dibijando la forma cuadrada que captura el rostro 
        for (x,y,w,h) in faces: 
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxImg[y:y+h,x:x+w]

            rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
            count = count + 1
        # mostramos el fotograma con la cara detectada 
        cv2.imshow('img',img)

        k = cv2.waitKey(1)
        if k == 27 or count >= 20:
            break

    print('FIN..')
    cap.release()
    cv2.destroyAllWindows()


submit = Button(pantalla, text = "Registrar", width = 20, height = 1, bg="#00CD63", command = send_data).pack()

pantalla.mainloop()






