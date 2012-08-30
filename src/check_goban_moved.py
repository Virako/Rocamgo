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

from src.cte import *
from cv import *

def search_sum_pixels_in_line_y(x, y, dist, img1, img2): # if x line: values order x, y
    change = 0
    acum = 0
    while acum < NUM_POINTS:
        pixel1 = Get2D(img1, y, x)
        pixel2 = Get2D(img2, y, x)
        change += abs(pixel1[0]-pixel2[0]) + \
         abs(pixel1[1]-pixel2[1]) + abs(pixel1[2]-pixel2[2]) 
        y -= dist 
        acum += 1
    return change

def search_sum_pixels_in_line_x(x, y, dist, img1, img2): # if x line: values order x, y
    change = 0
    acum = 0
    while acum < NUM_POINTS:
        pixel1 = Get2D(img1, y, x)
        pixel2 = Get2D(img2, y, x)
        change += abs(pixel1[0]-pixel2[0]) + \
         abs(pixel1[1]-pixel2[1]) + abs(pixel1[2]-pixel2[2]) 
        x -= dist 
        acum += 1
    return change

def check_goban_moved(img1,img2,corners):

    if not (img1 and img2):
        return True 
 
    change_total = []
    # TODO Comentar que recorremos las 4 lineas externas para buscar cambios
    for c1 in corners[::3] :
        p1_x = c1[0]
        p1_y = c1[1]
        for c2 in corners[1:3]:            
            p2_x = c2[0]
            p2_y = c2[1]
            
            if p1_x == p2_x:
                if p1_y < p2_y:
                    p1_y, p2_y = p2_y, p1_y
                dist = (p1_y - p2_y)/NUM_POINTS
                change = search_sum_pixels_in_line_y(p1_x, p1_y, dist, img1, img2)
            elif p1_y == p2_y:
                if p1_x < p2_x:
                    p1_x,p2_x = p2_x,p1_x
                dist = (p1_x - p2_x)/NUM_POINTS
                change = search_sum_pixels_in_line_x(p1_x, p1_y, dist, img1, img2)
            else:
                if p1_x < p2_x:
                    p1_x,p2_x = p2_x,p1_x
                dist_x = (p1_x - p2_x)/NUM_POINTS
                x = p1_x 
                y = p1_y
                change = 0
                acum = 0
                while acum < NUM_POINTS: 
                    pixel1 = Get2D(img1, y, x)
                    pixel2 = Get2D(img2, y, x)
                    change += abs(pixel1[0]-pixel2[0]) + \
                     abs(pixel1[1]-pixel2[1]) + abs(pixel1[2]-pixel2[2]) 
                    x -= dist_x 
                    y = (((x - p1_x)*(p2_y - p1_y))/(p2_x - p1_x))+p1_y
                    acum += 1
            change /= 20
            change_total.append(change)
            # add to test goban with x1==x2 and y1==y2. No hay pendiente. 

    print change_total, corners
    #return min(change_total) > 30 and max(change_total) > 80
    return sum(change_total) > 40*4

