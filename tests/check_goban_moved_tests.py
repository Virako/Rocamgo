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
 
from src.check_goban_moved import check_goban_moved
from cv import LoadImageM
from cv import CV_LOAD_IMAGE_COLOR

import unittest
from nose.tools import *
import os
try:
    import cPickle as pickle
except:
    import pickle


class Test_camera(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def images_true(self):
        return (('img0013.png', 'img0014.png'), ('img0001.png', 'img0004.png'), 
                ('img0014.png', 'img0013.png'), ('img0004.png', 'img0001.png'))


    def images_false(self):
        return (('img0001.png'), ('img0004.png'), ('img0007.png'), ('img0010.png'))


    def select_corners_false(self, n):
        path = 'tests/images/'
        image1 = self.images_false()[n]
        txt1 = image1.replace('.png', '.txt')
        with open(path + txt1) as f:
            corners_img1 = pickle.load(f)
        return corners_img1, corners_img1


    def select_corners_true(self, n):
        path = 'tests/images/'
        image1, image2 = self.images_true()[n]
        txt1 = image1.replace('.png', '.txt')
        txt2 = image2.replace('.png', '.txt')
        with open(path + txt1) as f:
            corners_img1 = pickle.load(f)
        with open(path + txt2) as f:
            corners_img2 = pickle.load(f)
        return corners_img1, corners_img2
        

    def test_check_goban_moved_true1(self):
        corners_img1, corners_img2 = self.select_corners_true(1)
        assert_true(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_true2(self):
        corners_img1, corners_img2 = self.select_corners_true(2)
        assert_true(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_true3(self):
        corners_img1, corners_img2 = self.select_corners_true(3)
        assert_true(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_true0(self):
        corners_img1, corners_img2 = self.select_corners_true(0)
        assert_true(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_false1(self):
        corners_img1, corners_img2 = self.select_corners_false(1)
        assert_false(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_false2(self):
        corners_img1, corners_img2 = self.select_corners_false(2)
        assert_false(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_false3(self):
        corners_img1, corners_img2 = self.select_corners_false(3)
        assert_false(check_goban_moved(corners_img1, corners_img2))


    def test_check_goban_moved_false0(self):
        corners_img1, corners_img2 = self.select_corners_false(0)
        assert_false(check_goban_moved(corners_img1, corners_img2))


if __name__ == '__main__':
    print "Run test with nosetest"
