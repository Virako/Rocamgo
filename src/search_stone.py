#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Rocamgo is recogniter of the go games by processing digital images with opencv.
# Copyright (C) 2012 Víctor Ramirez de la Corte <virako.9 at gmail dot com>
# Copyright (C) 2012 David Medina Velasco <cuidadoconeltecho at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from cv import *
from src.difference import *
from cte import GOBAN_SIZE
class Search_stone:
    """clase encargada de la deteccion de piedras, todas las funciones de esta clase
    se encargar de pasar de una imagen de un tablero con piedras donde el tablero
    esta detectado a un archivo .sfg"""
    def __init__(self):
        self.ultimaimagenbuena=None 
        

    def search_ston(self,previusimg,imgcurrent):
        """esta funcion se encarga de ver si las imagenes que nos llegan son claras
        y en caso de serlo busca piedras en ella. Devuelve las piedras en caso de 
        encontrarlas"""
        stones=None
        diff = difference(previusimg,imgcurrent)
        if not self.true_img(diff):
            stones = self.search_circle(imgcurrent)
        return stones
        

    def true_img(self,diff):
        """Analiza las diferencias de las dos imagenes, asi 
        podemos saber si la imagen es clara o no, pues puede que la imagen tenga 
        manos por medio. Devuelve si una imagen es valida o no """

        while 1:
            ShowImage("Camera", diff)
            key = WaitKey(30)
            if key == 27: # Esc
                break
        nx = diff.height/30     #valor salto x
        ny = diff.width/30      #valor salto y
        px,py = 0,0             # posicion actual de x e y
        cont_pix_change = 0
        n_samples = 0          #numero de muestras
           
        while px<diff.height:
            while py<diff.width:
                pixel=Get2D(diff,px,py)
                cambio=pixel[0]+pixel[1]+pixel[2]
                if cambio>60:
                   cont_pix_change += 1
                py+=ny
                n_samples+=1
            py=0
            px+=nx
            
        print  cont_pix_change>(n_samples/8)
        return cont_pix_change>(n_samples/8)


    #dp estaba a 1.6
    def search_circle(self, image, dp = 1.6):
        """Función que trata la imagen luminosa con los filtros Canny y Smooth y 
           busca cincunferencias. Devuelve los centros de las cincunferencias 
           encontradas """ 
        
        stones = []

        gray = CreateImage((image.width, image.height), IPL_DEPTH_8U, 1)
        CvtColor(image, gray, CV_BGR2GRAY)
        
        # creamos dos imagenes auxiliares para aplicar los filtros
        gray_aux = CreateImage((gray.width, gray.height), gray.depth, \
         gray.nChannels)
        gray_aux_2 = CreateImage((gray.width, gray.height), gray.depth, \
         gray.nChannels)
        
        Canny(gray, gray_aux_2, 50,55,3)
        Smooth(gray_aux_2, gray_aux, CV_GAUSSIAN, 5, 5)
        
        # creo una matriz de para guardar los circulos encontrados
        storage = CreateMat(1, gray_aux.height*gray_aux.width, CV_32FC3)

        # Buscamos circunferencias en la imagen con la transformada de Hough, 
        # el tamaño de las circunferencias estarán entre los radios dados
                
        tamcelda = image.width/GOBAN_SIZE
        tamcelda2 = image.height/GOBAN_SIZE
        border = tamcelda/4
        
        circles = HoughCircles( gray_aux, storage, CV_HOUGH_GRADIENT, dp, \
         tamcelda/2+border, 50, 55, tamcelda/4+border,  tamcelda/2+border ) 
         
        try:
            for n in range(0, storage.cols):
                p = Get1D(storage, n)
                pt = (Round(p[0]), Round(p[1]))
                stones.append(pt)
                Circle(gray, pt, Round(p[2]), CV_RGB(255, 255, 255), 2) # pinta el circulo encontrado
            print "Hay ", len(stones), " circulos en la imagen"
        except:
            print "No hemos podido recorrer el storage de cvHoughCircles.\
             No se han encontrado circunferencias"
        
        while 1:
            ShowImage("pepito",gray)
            key = WaitKey(30)
            if key == 27: # Esc
                break
        
        
            
        #try: cvSaveImage("images/circunferencias.png", gray)
        #except: print "Error al guardar la imagen con cincunferencias. " # para chequeo
        
        #if storage.cols == 0 and dp <= 2 and len(stones) == 0:
        #    dp += 0.2
        #    print "variando profundidad para buscar mejor:", dp
           
        #    return search_circle(image, tablero, size, dp = dp+0.2) # TODO problema al hacer la recursividad y al variar el dp
        
            
        return stones
        
    def check_color(self,stone,img):
        """Nos encargamos de saber el color de una piedra.Devuelve si es blanco o
        negro en forma binaria."""
        tamcelda = img.width/20
        colorn=0
        colorb=0
        for x in range(stone[0]-tamcelda,stone[0]+tamcelda):
            pixel=Get2D(img,x,stone[1])
            if pixel[0]>200 and pixel[1]>200 and pixel[2]>200:
                colorb += 1
            if pixel[0]<50 and pixel[1]<50 and pixel[2]<50:
                colorn += 1
        for y in range(stone[1]-tamcelda,stone[0]+tamcelda):
            pixel=Get2D(img,stone[0],y)
            if pixel[0]>200 and pixel[1]>200 and pixel[2]>200:
                colorb += 1
            if pixel[0]<50 and pixel[1]<50 and pixel[2]<50:
                colorn += 1
        if colorb > colorn:
            return 1
        return 0 
   
    def position_img_goban(self,stone,img):
        """Devuelve la posicion de la interseccion, a partir de una posicion en 
        pixeles"""
        distx = img.width/19
        disty = img.height/19
        posx = stone[0]/distx
        posy = stone[1]/disty
        return [posx,posy]
        
        
        
        
        
        
        
        
        
        
        
        
                  
