# -*- coding: utf-8 -*-
#
# Rocamgo is recogniter of the go games by processing digital images with opencv.
# Copyright (C) 2012 Víctor Ramirez de la Corte <virako.9@gmail.com>
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
    
from src.Camera import Camera
import unittest
from nose.tools import *

class Test_camera(unittest.TestCase):
    
    def setUp(self):
        self.camera = Camera()
        self.camera.capture = "Capture1"
    
    def tearDown(self):
        self.camera.close_camera()
    
    def test_get_frame_from_camera_close(self):
        self.camera.close_camera()
        assert_equals(self.camera.capture, None)
    
if __name__ == '__main__':
    print "Run test with nosetest"
