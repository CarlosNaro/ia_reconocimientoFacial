import cv2
import os

# dataPath = 'C:/Users/Developer/Desktop/Proyecto/Data' #Cambia a la ruta donde hayas almacenado Data
dataPath = 'E:\Desarrollo_Software\Python-IA\ia_reconocimientoFacial\Data' #Cambia a la ruta donde hayas almacenado Data

imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
#face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
#-----
# face_recognizer.read('modeloLBPHFace.xml')
face_recognizer.read('E:\Desarrollo_Software\Python-IA\ia_reconocimientoFacial\modeloLBPHFace.xml')


#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('Video.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
	ret,img = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	auxImg = gray.copy()

	faces = faceClassif.detectMultiScale(gray,1.1,4)

	for (x,y,w,h) in faces:
		rostro = auxImg[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)

		cv2.putText(img,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		'''
		# EigenFaces
		if result[1] < 5700:
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		
		# FisherFace
		if result[1] < 500:
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		'''
		# LBPHFace
		if result[1] < 50:
			cv2.putText(img,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)	
			print('::::')
			print(' ',imagePaths[result[0]] , ' Asistencia Registrada')
			print('::::')
		else:
			cv2.putText(img,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
		
	#cv2.imshow('img',img)
	#k = cv2.waitKey(1)
	#if k == 27 or result[1] < 50:
	#	print('::::')
	#	print(' ',imagePaths[result[0]] , ' Asistencia Registrada')
	#	break
		
	cv2.imshow('img',img)
	k = cv2.waitKey(1)
	if k == 27:	
		break
print(':::::::::')
print('Fin del Reconocimiento')
cap.release()
cv2.destroyAllWindows()
