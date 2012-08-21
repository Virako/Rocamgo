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

from cv import CreateImage, CreateMat, Smooth, AbsDiff, CV_GAUSSIAN, iplimage, cvmat, Add

def difference(img1, img2):
    if isinstance(img1, cvmat):
        aux1 = CreateMat(img1.rows, img1.cols, img1.type)
        aux2 = CreateMat(img1.rows, img1.cols, img1.type)
        res  = CreateMat(img1.rows, img1.cols, img1.type)
    elif isinstance(img1, iplimage):
        aux1 = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
        aux2 = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
        res  = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
    else:
        return -1

    Smooth(img1, aux1, CV_GAUSSIAN, 5, 5)
    Smooth(img2, aux2, CV_GAUSSIAN, 5, 5)
    
    AbsDiff(aux1, aux2, res) 
    return res

def suma(img1, img2):
    if isinstance(img1, cvmat):
        aux1 = CreateMat(img1.rows, img1.cols, img1.type)
        aux2 = CreateMat(img1.rows, img1.cols, img1.type)
        res  = CreateMat(img1.rows, img1.cols, img1.type)
    elif isinstance(img1, iplimage):
        aux1 = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
        aux2 = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
        res  = CreateImage((img1.width, img1.height), img1.depth, img1.nChannels)
    else:
        return -1

    Smooth(img1, aux1, CV_GAUSSIAN, 5, 5)
    Smooth(img2, aux2, CV_GAUSSIAN, 5, 5)
    
    Add(aux1, aux2, res) 
    return res



