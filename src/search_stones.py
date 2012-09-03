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
from src.cte import GOBAN_SIZE
from src.cte import BLACK
from src.cte import WHITE


def search_stones(img, corners, dp=1.7):
    """ Devuelve las circunferencias encontradas en una imagen. """
    gray = CreateMat(img.width, img.height,CV_8UC1)
    CvtColor(img, gray, CV_BGR2GRAY)
    
    gray_aux = CloneMat(gray)
    gray_aux_2 = CloneMat(gray)
    Canny(gray, gray_aux_2, 50,55,3)
    Smooth(gray_aux_2, gray_aux, CV_GAUSSIAN, 3, 5)
    
    # creo una matriz de para guardar los circulos encontrados
    circles = CreateMat(1, gray_aux.height*gray_aux.width, CV_32FC3)
    # r es el la mitad del tamaño de un cuadrado, el radio deseado 
    r = img.width/(GOBAN_SIZE*2)
    
    # HoughCircles(image, storage, method, dp, min_dist, param1, param2, 
    # min_radius, max_radius)
    HoughCircles(gray_aux, circles, CV_HOUGH_GRADIENT, dp, int(r*0.5), 50, 55,\
     int(r*0.7), int(r*1.2)) 
     
    return circles



def check_color_stone(pt, radious, img, threshold=190):
    """ Devuelve el color de la piedra dado el centro y el radio de la piedra y
    una imagen. También desechamos las piedras que no sean negras o blancas. """
    
    black_total = 0
    white_total = 0
    no_color = 0
    for x in range(pt[0] - radious/2, pt[0] + radious/2):
        try: 
            pixel = Get2D(img, pt[1], x)[:-1]
        except:
            continue
        if all(p > threshold for p in pixel):
            white_total += 1
        elif all(p < 50 for p in pixel):
            black_total += 1
        else:
            no_color += 1
    for y in range(pt[1] - radious/2, pt[1] + radious/2):
        try:
            pixel = Get2D(img, y, pt[0])
        except:
            continue
        if all(p > threshold for p in pixel):
            white_total += 1
        elif all(p < 50 for p in pixel):
            black_total += 1
        else:
            no_color += 1
    
    if white_total >= black_total and white_total >= no_color:
        return WHITE
    elif no_color >= black_total and no_color >= white_total:
        return -1
    elif black_total >= white_total and black_total >= no_color:
        return BLACK

