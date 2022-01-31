from skimage import data, img_as_float, io  # Skimage Para el histograma
import random  # Variables aleatorias
from PIL import Image, ImageFilter  # Edición de imagen
from matplotlib import pyplot as plt  # Generar gráficos
import cv2  # Librería OpenCV
from skimage import exposure
import numpy as np  # Para arrays
import os  # Para trabajar en un SO, creando archivos temporales
os.sys.path
print('done')


img1 = cv2.imread('nieve1.PNG')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray1, 210, 255, cv2.THRESH_BINARY)
cv2.imshow('3', gray1)
cv2.imshow('1', thresh1)
print('done')
cv2.waitKey(0)

cv2.imshow('image1', thresh1)
img2 = cv2.imread('nieve2.PNG')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(gray2, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('image2', thresh2)
print('done')
cv2.waitKey(0)
