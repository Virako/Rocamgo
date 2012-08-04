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

from sys import path
path.append('/usr/lib/pymodules/python2.7')
from cv import CreateFileCapture
from cv import DestroyAllWindows
from cv import ShowImage
from cv import WaitKey
from cv import SetMouseCallback
from cv import CV_EVENT_LBUTTONDBLCLK
from cv import CV_EVENT_LBUTTONDOWN
from src.camera import Camera

class Cameras:
    """ Class for open cameras in the computer. """

    def __init__(self):
        #cam = Camera()
        #cam.index = 100
        #cam.capture = CreateFileCapture("http://192.168.1.2:5143/mjpeg")
        self.cameras = []
        self.camera = None

    def on_mouse(self, event, x, y, flags, camera):
        """ Event for clicks of mouse. """
        if event == CV_EVENT_LBUTTONDOWN:
            print "SIMPLE CLICK"
        elif event == CV_EVENT_LBUTTONDBLCLK: 
            self.camera = camera
            print "DOBLE CLICK"

    def check_cameras(self, num=99):
        """ Check cameras. """
        n = 0
        while len(self.cameras) < num and n < 100: 
            camera = Camera() 
            camera.open_camera(n)
            if camera.get_frame(): 
                self.cameras.append(camera)
            n += 1
        return len(self.cameras)

    def show_and_select_camera(self):
        """ Show cameras in different windows for select one camera. """
        if not self.cameras:
            return self.camera
        elif len(self.cameras) == 1:
            return self.cameras[0]
        else:
            while not self.camera:
                for camera in self.cameras:
                    name_windows = str(camera.index)
                    img = camera.get_frame()
                    ShowImage(name_windows, img)
                    key = WaitKey(60)
                    # TODO select camera push the key
                    SetMouseCallback(name_windows, self.on_mouse, camera) 
            DestroyAllWindows()

        return self.camera

