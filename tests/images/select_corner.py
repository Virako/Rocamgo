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

from cv import SetMouseCallback
from cv import ShowImage
from cv import LoadImage
from cv import WaitKey
from cv import DestroyWindow
from cv import CV_EVENT_LBUTTONDOWN
from cv import CV_LOAD_IMAGE_COLOR
import os
try:
    import cPickle as pickle
except ImportError:
    import pickle

global corners 
corners = []

def on_mouse(event, x, y, flags, filename):
    """ Event for clicks of mouse. """
    global corners
    if event == CV_EVENT_LBUTTONDOWN:
        corners.append((x,y))
        print corners

def sort_corners(): 
    """ Get corner sorted: ul, dl, ur, dr """
    global corners
    corners.sort()
    c1 = corners[:2]
    c2 = corners[2:]
    if corners[0][1] >= corners[1][1]:
        c1.reverse()
    if corners[2][1] >= corners[3][1]:
        c2.reverse()
    return c1 + c2


def load_images(path):
    global corners
    names_images = os.listdir(path)
    png = lambda x: x[-3:] == "png"
    names_images = filter(png, names_images)
    for name in names_images:
        print name
        img = LoadImage(os.path.join(path, name), CV_LOAD_IMAGE_COLOR)
        filename = name.replace(".png", ".txt")
        corners = []
        while 1:
            ShowImage(filename, img)
            SetMouseCallback(filename, on_mouse, os.path.join(path, filename))
            key = WaitKey()
            if key == 10 and len(corners) == 4: # Enter for next
                with open(os.path.join(path, filename), 'w') as f:
                    corners = sort_corners()
                    pickle.dump(corners, f)
                DestroyWindow(filename)
                break
            elif key == 10:
                print "Not 4 corners"
            elif key == 110: # n next image
                DestroyWindow(filename)
                break
            elif key == 114: # r for start and remove point
                corners = []
            elif key == 27: # ESC
                exit()
            else:
                print key

load_images('.')
