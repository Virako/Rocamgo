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

"""
:var cameras: lista de cámaras 
:type cameras: list
:var camera: cámara seleccionada
:type camera: Capture
"""

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
from src.cte import *

class Cameras:
    """ Clase para abrir las cámaras disponibles en el ordenador. """

    def __init__(self):
        #cam = Camera()
        #cam.index = 100
        #cam.capture = CreateFileCapture("http://192.168.1.2:5143/mjpeg")
        self.cameras = []
        self.camera = None

    def on_mouse(self, event, x, y, flags, camera):
        """ Capturador de eventos de click de ratón. 
        :param event: Evento capturado.  
        :type event: int
        :param x: posición x del ratón. 
        :type x: int
        :param y: posición y del ratón. 
        :type y: int
        :param camera: objeto Camera. 
        :type camera: Camera
        """
        if event == CV_EVENT_LBUTTONDBLCLK: 
            self.camera = camera

    def check_cameras(self, num=MAX_CAMERAS):
        """ Comprueba las cámaras disponibles. 
        :param num: máximo número de cámaras a comprobar
        :keyword num: el valor por defecto es 99, ya que en Linux es lo
        permitido
        :param num: int
        :return: lista de cámaras disponibles
        :rtype: list of Camera
        """
        n = 0
        while len(self.cameras) < num and n <= MAX_CAMERAS: 
            camera = Camera() 
            camera.open_camera(n)
            if camera.get_frame(): 
                self.cameras.append(camera)
            n += 1
        return len(self.cameras)

    def show_and_select_camera(self):
        """ Muestra las cámaras disponibles en ventanas y da la opción de
        seleccionar una de ellas pulsando doble click.
        :return: cámara seleccionada
        :rtype: Camera """
        if not self.cameras:
            return self.camera
        elif len(self.cameras) == 1:
            return self.cameras[0]
        elif len(self.cameras) > 1:
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

