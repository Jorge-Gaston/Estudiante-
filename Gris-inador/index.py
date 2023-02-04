import tkinter as tk
from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog


print ("Arrancando")

#Configuracion de la ventana
ventana = tk.Tk() 
ventana.title("Vuelvelo gris-inador") #Titulo de la ventana
ventana.geometry("800x607") #Dimensiones de la ventana
ventana.config(bg="green")
ventana.resizable(1,1)

#funcion para añadir una imagen
def openimage():
    #agregado el selecionador de archivos// para comodidad, cambiar la linea de direccion a donde quiera que abra para las imagenes
    filepath = filedialog.askopenfilename(initialdir= "C:\\Users\\Gaston\\Desktop\\Gris-inador\\img", # <<< esta linea
                                            filetypes=(("JPG", "*.jpg"), ("all files", "*.*")))
    file = open(filepath, "r")                                    
    print (file.read)
    
    print(file.name)
    #Aqui abre la imagen y cambiando el tamaño
    img = Image.open(file.name)
    #Cambia el tamaño
    newimg = img.resize((358, 256))
    reader = ImageTk.PhotoImage(newimg)
    img1 = Label(ventana, image=reader)
    img1.image = reader
    #Cambia la Posicion de la imagen
    img1.place(x=20, y=10)
    file.close() #cerrando el seleccionador de archivos

    #copiando imagen para aplicar escala de grises    
    #aplicando la escala de grises
    
    
    #>>>>>>>>>>>>Primer metodo Average<<<<<<<<<<<<<<<
    
    arrImage = np.array(img)
    arrz =np.zeros((arrImage.shape[0], arrImage.shape[1]))
    #FOR para recorrer la imagen
    for i in (range(arrImage.shape[0])):
        for n in (range(arrImage.shape[1])):
            R = 0
            G = 0
            B= 0

            for j in (range (arrImage.shape[2])):
                if j == 0:
                    R=arrImage[i,n,j] / 3
                elif j == 1:
                    G = arrImage[i,n,j] / 3
                else:
                    B = arrImage[i,n,j] / 3
            arrz[i,n] = R + G + B
    cv2.imwrite("Escala.jpg", arrz)
    cv2.waitKey(0)
    #Mostrando la segunda imagen
    img2 = Image.open("Escala.jpg")
    #Cambiando dimensiones
    newimg = img2.resize((358, 256))
    reader = ImageTk.PhotoImage(newimg)
    img2 = Label(ventana, image= reader)
    img2.image = reader
    #Posicion de la imagen
    img2.place(x=415, y=10)

    #>>>>>>>>>>>>Segundo metodo "MidGray"<<<<<<<<< 
    segImage = np.array(img)
    arrz =np.zeros((segImage.shape[0], segImage.shape[1]))
    #FOR para recorrer la imagen
    for i in (range(segImage.shape[0])):
        for n in (range(segImage.shape[1])):
            R = 0
            G = 0
            B= 0
            suma = 0
            for j in (range (segImage.shape[2])):
                if j == 0:
                    R=segImage[i,n,j] *.03
                    suma = suma + R
                elif j == 1:
                    G = segImage[i,n,j] *0.59
                    suma = suma + G
                else:
                    B = segImage[i,n,j] *0.11
                    suma = suma + B
            arrz[i,n] = suma
    cv2.imwrite("Escala2.jpg", arrz)
    cv2.waitKey(0)
    #Mostrando la segunda image
    segimg = Image.open("Escala2.jpg")
    #Cambiando dimensiones le tamaño
    newimg = segimg.resize((358, 256))
    reader = ImageTk.PhotoImage(newimg)
    segimg = Label(ventana, image=reader)
    segimg.image = reader
    #Posicion de la imagen
    segimg.place(x=20, y=337)

    #>>>>>>>>>>>>Tercer metodo "HSL"<<<<<<<<<<<
    
    segImage = np.array(img)
    arrz =np.zeros((segImage.shape[0], segImage.shape[1]))
    #FOR para recorrer la imagen
    
    for i in (range(segImage.shape[0])):
        for n in (range(segImage.shape[1])):
            R = 0
            G = 0
            B= 0
            for j in (range (segImage.shape[2])):
                if j == 0:
                    
                    R = segImage[i,n,j] * 0.299
                    
                elif j == 1:
                    G = segImage[i,n,j] * 0.587
                    
                else:
                    B = segImage[i,n,j] *0.114
                    
            arrz[i,n] = R + G + B
    cv2.imwrite("Escala3.jpg", arrz)
    cv2.waitKey(0)
    #Mostrando la tercer imagen
    terimg = Image.open("Escala3.jpg")
    #Cambiando dimensiones le tamaño
    newimg = terimg.resize((358, 256))
    reader = ImageTk.PhotoImage(newimg)
    terimg = Label(ventana, image=reader)
    terimg.image = reader
    #Posicion de la imagen
    terimg.place(x=415, y=337)


#------Widgets------
#Boton
B1 = tk.Button(ventana,command=openimage, text="Seleccionar imagen", width=17, height=2, bg=("gray"))

#Labels
tl = tk.Label(text="Imagen seleccionada ^", width=22, height=1)
tl1 = tk.Label(text="Escala de grises 'Average'^", width=22, height=1)
tl2 = tk.Label(text="Escala de grises 'HSL' ", width=22, height=1)
tl3 = tk.Label(text="Escala de grises 'Midgray'", width=22, height=1)

#Posicion para los widgets
B1.place(x=334, y=286)
tl.place(x=65, y=286)
tl1.place(x=560, y=286)
tl2.place(x=560, y=310)
tl3.place(x=65, y=310)


#Intento para ocultar los labels
#tl1.place_forget()
#tl2.place_forget()
#tl3.place_forget()

#Arranca ventana
ventana.mainloop()