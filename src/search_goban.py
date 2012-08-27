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
from math import sqrt
from src.difference import difference
from src.cte import *

def count_perimeter(seq):
    """ Count perimeter from sequence (contour). """
    ant = False
    for (a,b) in seq:
        if ant:
            perimeter += sqrt((ant[0]-a)**2 + (ant[1]-b)**2)
        else:
            perimeter = sqrt((seq[-1][0]-a)**2 + (seq[-1][1]-b)**2)
        ant = (a,b)
    return perimeter

def get_corners(contour):
    """ Get corner sorted: ul, dl, ur, dr """
    corners = []
    for (x,y) in contour:
        corners.append((x,y))
    corners.sort()
    c1 = corners[:2]
    c2 = corners[2:]
    if corners[0][1] >= corners[1][1]:
        c1.reverse()
    if corners[2][1] >= corners[3][1]:
        c2.reverse()
    return c1 + c2


def filter_image(img):
    aux_1 = CreateMat(img.rows, img.cols, img.type)
    aux_2 = CreateMat(img.rows, img.cols, img.type)
    Canny(img, aux_2, 50, 200, 3)
    Smooth(aux_2, aux_1, CV_GAUSSIAN, 3, 3)
    return aux_1


def detect_contour(img, img2):
    """ From a image filtered previously, detect contours. """ 
    storage = CreateMemStorage()
    seq = FindContours(img, storage, CV_RETR_TREE, CV_CHAIN_APPROX_NONE, 
      offset=(0, 0))
    sequence = []
    
    aprox = True
    while seq:
        if len(seq) >= 4 and (img.cols*img.rows) > ContourArea(seq) > \
            ((img.cols/2)*(img.rows/2)):
            perimeter = count_perimeter(seq)
            seq_app = ApproxPoly(seq, storage, CV_POLY_APPROX_DP, perimeter*0.02, 1)
            if len(seq_app) == 4:
                return seq_app
            else:
                return None
        else:
            if seq.h_next() == None:
                break
            else:
                seq = seq.h_next()
    return None


def search_goban(img): 
    aux_gray = CreateImage((img.width, img.height), IPL_DEPTH_8U, 1)
    CvtColor(img, aux_gray, CV_RGB2GRAY)
    img_gray = GetMat(aux_gray, 0)
    img_filtered = filter_image(img_gray)
    contour = detect_contour(img_filtered, img)
    if contour: 
        return get_corners(contour)
    else:
        return None

