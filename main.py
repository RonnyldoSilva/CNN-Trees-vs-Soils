# Importando as bibliotecas necessarias
import argparse
import numpy as np 
import cv2

# Construindo o analisador de argumentos e analisar os argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")

args = vars(ap.parse_args())

# Carregando o modelo e classificando
import tflearn 
from tflearn.layers.conv import conv_2d, max_pool_2d 
from tflearn.layers.core import input_data, dropout, fully_connected 
from tflearn.layers.estimator import regression 

IMG_SIZE = 50
LR = 1e-3

import tensorflow as tf 
convnet = input_data(shape =[None, IMG_SIZE, IMG_SIZE, 1], name ='input') 
  
convnet = conv_2d(convnet, 32, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 
  
convnet = conv_2d(convnet, 64, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 
  
convnet = conv_2d(convnet, 128, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 
  
convnet = conv_2d(convnet, 64, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 
  
convnet = conv_2d(convnet, 32, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 
  
convnet = fully_connected(convnet, 1024, activation ='relu') 
convnet = dropout(convnet, 0.8) 
  
convnet = fully_connected(convnet, 2, activation ='softmax') 
convnet = regression(convnet, optimizer ='adam', learning_rate = LR, 
      loss ='categorical_crossentropy', name ='targets') 
  
model = tflearn.DNN(convnet, tensorboard_dir ='log')
model.load('./model.tflearn')

# Carregando a imagem de entrada do disco
img = cv2.imread(args["input"], cv2.IMREAD_GRAYSCALE) 
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
testing_data = []
testing_data.append([np.array(img), 0])
data = testing_data[0][0].reshape(IMG_SIZE, IMG_SIZE, 1) 

# Classificando a imagem
model_out = model.predict([data])[0]

prediction = ''

if np.argmax(model_out) == 1: prediction = 'Soil'
else: prediction = 'Tree'

result = '\nResultado: {}'.format(prediction)

print(result)