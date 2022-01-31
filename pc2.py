from skimage import data, img_as_float, io  # Skimage Para el histograma
import random  # Variables aleatorias
from PIL import Image, ImageFilter  # Edición de imagen
from matplotlib import pyplot as plt  # Generar gráficos
import cv2  # Librería OpenCV
from skimage import exposure
import numpy as np  # Para arrays
import os  # Para trabajar en un SO, creando archivos temporales
os.sys.path

# Umbralización

gray1 = cv2.imread('nieve1.PNG', 0)
ret, thresh1 = cv2.threshold(gray1, 210, 255, cv2.THRESH_BINARY)
# cv2.imshow('1', thresh1)
# cv2.waitKey(0)

gray2 = cv2.imread('nieve2.PNG', 0)
ret, thresh2 = cv2.threshold(gray2, 210, 255, cv2.THRESH_BINARY)
# cv2.imshow('2', thresh2)
# cv2.waitKey(0)
gray3 = cv2.imread('columbia1.jpeg', 0)
ret, thresh3 = cv2.threshold(gray3, 210, 255, cv2.THRESH_BINARY)
# cv2.imshow('1', thresh1)
# cv2.waitKey(0)

gray4 = cv2.imread('columbia2.jpeg', 0)
ret, thresh4 = cv2.threshold(gray4, 210, 255, cv2.THRESH_BINARY)
# cv2.imshow('2', thresh2)
# cv2.waitKey(0)

# Apertura

# Erosión


kernel = np.array(
    [[0, 0, 1, 0, 0],
     [1, 1, 0, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 0, 1, 1],
     [0, 0, 1, 0, 0]], np.uint8)

kernelpequeno = np.array(
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ], np.uint8
)


eroded1 = cv2.erode(thresh1, kernelpequeno, iterations=2)
#cv2.imshow('4', eroded)
# cv2.waitKey(0)
eroded2 = cv2.erode(thresh2, kernelpequeno, iterations=2)
#cv2.imshow('4', eroded)
# cv2.waitKey(0)

eroded3 = cv2.erode(thresh3, kernelpequeno, iterations=2)
#cv2.imshow('4', eroded)
# cv2.waitKey(0)
eroded4 = cv2.erode(thresh4, kernelpequeno, iterations=2)
#cv2.imshow('4', eroded)
# cv2.waitKey(0)


# Dilatación

# kernel = np.ones((3, 3))

dilatado1 = cv2.dilate(eroded1, kernelpequeno, iterations=1)
cv2.imshow('4', eroded1)
cv2.waitKey(0)
dilatado2 = cv2.dilate(eroded2, kernelpequeno, iterations=1)
cv2.imshow('4', eroded2)
cv2.waitKey(0)
dilatado3 = cv2.dilate(eroded3, kernelpequeno, iterations=1)
cv2.imshow('4', eroded3)
cv2.waitKey(0)
dilatado4 = cv2.dilate(eroded4, kernelpequeno, iterations=1)
cv2.imshow('4', eroded4)
cv2.waitKey(0)


alaska1rows = len(gray1)
print(alaska1rows)
alaska1cols = len(gray1[0])
print(alaska1cols)

columbia1rows = len(gray3)
columbia1cols = len(gray3[0])

alaska2rows = len(gray2)
alaska2cols = len(gray2[0])

columbia2rows = len(gray4)
columbia2cols = len(gray4[0])


nieveAlaska1 = np.sum(dilatado1 == 255)
print(nieveAlaska1)
nieveAlaska2 = np.sum(dilatado2 == 255)

nieveColumbia1 = np.sum(dilatado3 == 255)
nieveColumbia2 = np.sum(dilatado4 == 255)


porcentajeAlaska1 = nieveAlaska1/(alaska1cols * alaska1rows)*100
porcentajeAlaska2 = nieveAlaska2/(alaska2cols * alaska2rows)*100


porcentajeColumbia1 = nieveColumbia1/(columbia1cols * columbia1rows)*100
porcentajeColumbia2 = nieveColumbia2/(columbia2cols * columbia2rows)*100

print("La cantidad de nieve en Alaska 1980 es: "+str(porcentajeAlaska1))
print("La cantidad de nieve en Alaska 2020 es: "+str(porcentajeAlaska2))
print("La cantidad de nieve en Columbia 1980 es: "+str(porcentajeColumbia1))
print("La cantidad de nieve en Columbia 2020 es: "+str(porcentajeColumbia2))
