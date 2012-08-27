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

def check_goban_moved(img1,img2,corners):

    if not (img1 and img2):
        return True 
 
    change_final = []
    for c in corners[::3] :
        p1_x = c[0]
        p1_y = c[1]
        for c2 in corners[1:3]:            
            p2_x = c2[0]
            p2_y = c2[1]
            
            dist_x = abs(p1_x - p2_x) / NUM_POINTS
                                
            if p1_x < p2_x:
                p1_x,p2_x = p2_x,p1_x
                p1_y,p2_y = p2_y,p1_y
                
            x = p1_x 
            y = p1_y
            change_t = 0
            while x > p2_x: 
                pixel = Get2D(img1,y,x)
                pixel1 = Get2D(img2,y,x)
                change = abs(pixel[0]-pixel1[0]) + abs(pixel[1]-pixel1[1]) +\
                    abs(pixel[2]-pixel1[2])
                change_sum += change
                x = x-dist_x    
                y = ((x - p1_x)*(p2_y - p1_y) / (p2_x - p1_x))+p1_y
            change_sum = change_s / 20
            change_t.append(changet)
    
    return min(change_t) > 40     
                        
      
      
      
      
      
