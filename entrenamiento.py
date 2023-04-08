import cv2
import os
import numpy as np 

# dataPath = 'C:/Users/Developer/Desktop/Proyecto/Data'
dataPath = 'E:\Desarrollo_Software\Python-IA\ia_reconocimientoFacial\Data'
#procedemos alistar las carpetas 
peopleList = os.listdir(dataPath)
print('Lista de personas ', peopleList)

# creacion de array para el entrenamiento 
labels = []
facesData = []
label = 0

#prcedemos a leer cada uno de las imagenes en las carpetas 
for nameDir in peopleList:
    personPath = dataPath + '/' +nameDir
    print('Leyendo las Imagenes')
    # el segundop for es para leer cada imagen 
    for fileName in os.listdir(personPath):
        print('Rostro: ', nameDir + '/' + fileName) # muestra los rostro que se leen 
        #almacenaremos los rostros y las etiquetas que les corresponderan a cada uno 
        labels.append(label)
        facesData.append(cv2.imread(personPath + '/' + fileName, 0)) #se almacena las imagenes en escala de grices
        image = cv2.imread(personPath + '/' + fileName, 0)
       
        # :::: podemos ver el proceso de leer las imagenes 
        cv2.imshow('iamge', image)
        cv2.waitKey(10)
        #::::::::::::

    label = label + 1

print('Labels = ', labels)
print('Numero de Etiquetas 0 =', np.count_nonzero(np.array(labels) == 0))
print('Numero de Etiquetas 1 =', np.count_nonzero(np.array(labels) == 1))


# Métodos para entrenar el reconocedor
#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido
#face_recognizer.write('modeloEigenFace.xml')
#face_recognizer.write('modeloFisherFace.xml')

# face_recognizer.write('modeloLBPHFace.xml')
face_recognizer.write('E:\Desarrollo_Software\Python-IA\ia_reconocimientoFacial\modeloLBPHFace.xml')
print("Modelo almacenado...")