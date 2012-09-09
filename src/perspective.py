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


from cv import GetPerspectiveTransform
from cv import WarpPerspective
#from cv import Canny
#from cv import Smooth
from cv import CreateMat
from cv import CV_32FC1
#from cv import CV_RGB2GRAY
from cv import CreateImage
#from cv import IPL_DEPTH_8U
#from cv import CvtColor
#from cv import GetMat
from functions import get_max_edge
from functions import distance_between_two_points
from functions import get_external_corners


def perspective(img, corners): 
    """ Crea una imagen en modelo ideal del tablero dado en perspectiva.
    :param img: imagen con el tablero en perspectiva
    :todo comprobar de que tipo es la imagen TODO
    :type img: IplImage or CvMat
    :param corners: lista de las esquinas del tablero
    :type corners: list
    :return: imagen en modelo ideal
    :rtype: IplImage
    """

    max_edge = get_max_edge(corners)
    corners = get_external_corners(corners)
    # The goban have a relation 15/14 height/width
    relation = 14/15.0
    # In the sequence, the orden of corners are ul, dl, dr, ur
    corners_transf = ((0,0),(0,max_edge),(max_edge,0),(max_edge,max_edge))
    mat = CreateMat(3, 3, CV_32FC1)
    GetPerspectiveTransform( corners, corners_transf, mat)
    src = CreateImage((max_edge, max_edge), img.depth, img.nChannels)
    WarpPerspective(img, src, mat)
    return src

