import cv2
# referencia a la hardcase
face_cascade = cv2.CascadeClassifier(' _frontalface_default.xml')
#obtener referencia a la camara de la maquina
cap = cv2.VideoCapture(0)

while True:
    img = cap.read()
    #conversion a escala de grices 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #almacenara todas las caras detectadas por red neuronal de opencv
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
     # creamos la estructura de un cuadrado que detecte el restro 
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 2)
    # se muetra el fotograma con la cara detectada 
    cv2.imshow('img', img)
    # detectar se se preciono la tecla escape para salir del programa 
    #k = cv2.waitKey(1)
    #if k == 27: # 27 es el scall para Esc
    #    break
    if cv2.waitKey(1) == ord('q'): # Wait for the user to press 'q' key to stop the recording
      break
cap.release()


