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
 

from src.camera import Camera
from src.cameras import Cameras
import unittest
from nose.tools import *
from random import choice

class Test_camera(unittest.TestCase):
    
    def setUp(self):
        self.cameras = Cameras()
        self.camera_1 = Camera()
        self.camera_2 = Camera()
    
    def tearDown(self):
        self.cameras = None
    
    def test_select_zero_cameras(self):
        result = self.cameras.show_and_select_camera()
        assert_equals(result, None)
    
    def test_select_one_cameras(self):
        self.cameras.cameras = [self.camera_1]
        result = self.cameras.show_and_select_camera()
        assert_equals(result, self.camera_1)

    def test_select_two_or_more_cameras(self):
        self.cameras.cameras = [self.camera_1, self.camera_2]
        self.cameras.camera = choice(self.cameras.cameras)
        result = self.cameras.show_and_select_camera()
        assert_true(result in self.cameras.cameras)


if __name__ == '__main__':
    print "Run test with nosetest"
