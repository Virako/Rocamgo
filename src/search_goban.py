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
from math import sqrt, pi
from src.difference import difference
from src.difference import suma
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

def max_edge(corners):
    edges = []
    for c in xrange(NUM_EDGES):
        edges.append(sqrt((corners[c][0]-corners[(c+1)%4][0])**2 + \
                    (corners[c][1]-corners[(c+1)%4][1])**2))
    return int(max(edges))

def perspective(img, corners): 
    """ Create a transform in perspective from img in corners. """
    # save original corner 
    max_edge = max_edge(corners)
    # The goban have a relation 15:14 height:width
    relation = 14/15.0
    # In the sequence, the orden of corners are ul, dl, dr, ur
    corners_transf = ((0,0),(0,max_edge),(max_edge,0),(max_edge,max_edge))
    mat = CreateMat(3, 3, CV_32FC1)
    GetPerspectiveTransform( corners, corners_transf, mat)
    src = CreateMat( max_edge, max_edge, img.type )
    WarpPerspective(img, src, mat)
    return src

def filter_image(img):
    aux_1 = CreateMat(img.rows, img.cols, img.type)
    aux_2 = CreateMat(img.rows, img.cols, img.type)
    #Canny(img, aux_2, 10, 50)
    Canny(img, aux_2, 50, 200, 3)
    Smooth(aux_2, aux_1, CV_GAUSSIAN, 5, 5)
    return aux_1

def detect_contour(img, img2):
    """ From a image filtered previously, detect contours. """ # TODO rellenar doc
    storage = CreateMemStorage()
    seq = FindContours(img, storage, CV_RETR_TREE, CV_CHAIN_APPROX_NONE, 
      offset=(0, 0))
    sequence = []
    
    img_color = CloneImage(img2)
    aprox = True
    while seq:
        if len(seq) >= 4 and (img.cols*img.rows)*0.95 > ContourArea(seq) > ((img.cols/2)*(img.rows/2)):
            perimeter = count_perimeter(seq)
            seq_app = ApproxPoly(seq, storage, CV_POLY_APPROX_DP, perimeter*0.02, 1)
            if len(seq_app) == 4:
                print "BIEN"
                return seq_app
            else:
                print "MAL."
                return None
        else:
            if seq.h_next() == None:
                break
            else:
                seq = seq.h_next()
    
def search_goban(img):
    # ShowImage("ORIGINAL", img)
    contour = -1
    img_for_diff = None
    ant_diff = None
    diff_ant = None

    aux_gray = CreateImage((img.width, img.height), IPL_DEPTH_8U, 1)
    CvtColor(img, aux_gray, CV_RGB2GRAY)
    img_gray = GetMat(aux_gray, 0)
    img_filtered = filter_image(img_gray)
    if img_for_diff:
        diff = difference(img_for_diff, img)
        # ShowImage("DIFF", diff)
    
    if not contour or contour == -1: # TODO comprobar que hay movimiento
        contour = detect_contour(img_filtered, img)
        img_for_diff = CloneImage(img)

    if contour:
        corners = get_corners(contour)
        perspec = perspective(img_gray, corners)
        #print "buscando CIRCLES"
        #storage = CreateMat(perspec.width, 1, CV_32FC3)
        #HoughCircles(perspec, storage, CV_HOUGH_GRADIENT, 2, perspec.height/19.0, 200, 100)
        #for x in xrange(storage.height-1):
        #    circle = storage[x,0]
        #    Circle(perspec, (int(circle[0]), int(circle[1])), int(circle[2]), CV_RGB(255,0,0), 1, 8, 0) 
        # ShowImage("PERSPEC", perspec)


capture = CreateCameraCapture(1)
#capture = CaptureFromFile("videos/moviendo_tablero_tras_juagada.ogv")
#capture = CaptureFromFile("/home/virako/ROCAMGO/prueba2.avi")


while 1:
    img = QueryFrame(capture)
    print type(img)
    print search_goban(img)

    key = WaitKey(30)
    if key == 27:
        break
    elif key == 10:
        print "searchCircle"


    #seq = FindDominantPoints(seq, storage, CV_DOMINANT_IPAN, 0,0,0,0)
    #seq = ApproxPoly(seq, seq.header_size, storage, CV_POLY_APPROX_DP, 6, 1)


# def distancia_recta_punto(rp1, rp2, p):
#     return distancia_entre_dos_puntos(rp1, p) + distancia_entre_dos_puntos(rp2, p) 

# def centro(seq):
#     size = len(seq)
#     xs = 0
#     ys = 0
#     for (x,y) in seq:
#         xs += x
#         ys += y
#     return (xs/size, ys/size)


# def crea_recta(p1,p2):
#     pendiente =  (p2[1]-p1[1])/(p2[0]-p1[0])
#     return y = pendiente*x + (p1[1]-pendiente*p1[0])

# def detect_lines(img):
#     storage = CreateMemStorage()
#     #lines = HoughLines2( img, storage, CV_HOUGH_PROBABILISTIC, 1, pi/180, 30, img.cols/2, 10 )
#     lines = HoughLines2(img, storage, CV_HOUGH_STANDARD, 1, pi/180, 100, 0, 0)
#     return lines

