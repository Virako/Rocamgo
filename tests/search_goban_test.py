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
from src.perspective import *
from cv import LoadImage
from math import sqrt
import unittest
from nose.tools import *
import os
import operator
try:
    import cPickle as pickle
except ImportError:
    import pickle

class Test_camera(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def distancia(self, p1, p2):
        return sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)

    def get_corners_and_image(self, n):
        path = 'tests/images/'
        name_images = os.listdir(path)
        png = lambda x: x[-4:] == ".png"
        name_images = filter(png, name_images)
        name_images.sort()
        print name_images
        filename = name_images[n]
        name_txt = filename.replace('.png', '.txt')
        with open(path + name_txt) as f:
            return pickle.load(f), LoadImageM(path + filename, CV_LOAD_IMAGE_COLOR)

    def get_max_edge(self, corners):
        edges = []
        for c in xrange(4):
            edges.append(sqrt((corners[c][0]-corners[(c+1)%4][0])**2 + \
                        (corners[c][1]-corners[(c+1)%4][1])**2))
        return max(edges)


    def test_detect_goban1(self):
        corners, image = self.get_corners_and_image(0)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban2(self):
        corners, image = self.get_corners_and_image(1)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban3(self):
        corners, image = self.get_corners_and_image(2)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban4(self):
        corners, image = self.get_corners_and_image(3)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban5(self):
        corners, image = self.get_corners_and_image(4)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban6(self):
        corners, image = self.get_corners_and_image(5)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban7(self):
        corners, image = self.get_corners_and_image(6)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban8(self):
        corners, image = self.get_corners_and_image(7)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban9(self):
        corners, image = self.get_corners_and_image(8)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban10(self):
        corners, image = self.get_corners_and_image(9)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban11(self):
        corners, image = self.get_corners_and_image(10)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


    def test_detect_goban12(self):
        corners, image = self.get_corners_and_image(11)
        find_corners = search_goban(image)
        if not find_corners:
            assert_true(False)
        boolean = []
        for i in xrange(4):
            d1 = self.distancia(find_corners[i], corners[i])
            dist_max = get_max_edge(corners)/19
            boolean.append(d1 < dist_max)
        assert_true(reduce(operator.mul, boolean))


if __name__ == '__main__':
    print "Run test with nosetest"
