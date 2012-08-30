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

from cv import CreateImage
from cv import CreateMat
from cv import Smooth
from cv import AbsDiff
from cv import CV_GAUSSIAN
from cv import iplimage
from cv import cvmat
from cv import Add


def difference(img1, img2):
    # TODO """ """ 
    if isinstance(img1, cvmat) and isinstance(img2, cvmat) and \
      img1.rows == img2.rows and img1.cols == img2.cols: # same type and size
        aux1 = res = CreateMat(img1.rows, img1.cols, img1.type)
        aux2 = res = CreateMat(img2.rows, img2.cols, img2.type)
    elif isinstance(img1, iplimage) and isinstance(img2, iplimage) and \
     img1.width == img2.width and img1.height == img2.height: # same type and size
        aux1 = res = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
        aux2 = CreateImage((img2.width, img2.height), img2.depth, img2.nChannels)
    else:
        return -1

    Smooth(img1, aux1, CV_GAUSSIAN, 5, 5)
    Smooth(img2, aux2, CV_GAUSSIAN, 5, 5)
    AbsDiff(aux1, aux2, res) 
    return res


def add(img1, img2):
    # TODO """ """ 
    if isinstance(img1, cvmat) and isinstance(img2, cvmat) and \
      img1.rows == img2.rows and img1.cols == img2.cols: # same type and size
        aux1 = aux2 = res = CreateMat(img1.rows, img1.cols, img1.type)
    elif isinstance(img1, iplimage) and isinstance(img2, iplimage) and \
     img1.width == img2.width and img1.height == img2.height: # same type and size
        aux1 = aux2 = res = CreateImage((img1.width, img1.height),\
         img1.depth, img1.nChannels)
    else:
        return -1

    Smooth(img1, aux1, CV_GAUSSIAN, 5, 5)
    Smooth(img2, aux2, CV_GAUSSIAN, 5, 5)
    
    Add(aux1, aux2, res) 
    return res

