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
 
from src.search_goban import *
from cv import LoadImage
from math import sqrt
import unittest
from nose.tools import *

class Test_camera(unittest.TestCase):
    
    def setUp(self):
        self.images = []
        self.corners = []
        name_images = os.listdir("images")
        png = lambda x: x[-4:] == "png"
        name_images = filter(png, name_images)
        img = os.path.join(os.path.dirname(__file__), "images")
        for image in images:
            img.append()
            self.images.append(os.path.join(img, image))
            txt = image.replace(".png", ".txt")
            with open(txt) as f:
                self.corners.append(f.readlines())
    
    def tearDown(self):
        pass

    def distancia(self, p1, p2):
        return sqrt(abs(p1[0]-p1[1])**2, abs(p2[0]-p2[1])**2)

    def test_detect_goban(self):
        for i in xrange(len(self.images)):
            # open image
            image = LoadImageM(self.image[i], CV_LOAD_IMAGE_COLOR)
            find_corner = search_goban(image)
            good_corner = self.corner[i]
            check_corner = 0
            for find_point in find_corner:
                for good_point in good_corner:
                    if self.distancia(find_point, good_point) < \
                        self.distancia(good_point[0], good_point[1])/19:
                        check_corner += 1
                        break
            assert_equals(check_corner, 4)


if __name__ == '__main__':
    print "Run test with nosetest"
