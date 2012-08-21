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

from cv import * # TODO


def on_mouse(event, x, y, flags, camera):
    """ Event for clicks of mouse. """
    if event == CV_EVENT_LBUTTONDOWN:
        with open(filename, 'a') as f:
            f.writeline(x + ' ' + y))
            print "SIMPLE CLICK"

    self.images = []
    self.corners = []
    name_images = os.listdir("images")
    png = lambda x: x[-4:] == "png"
    name_images = filter(png, name_images)
    img = os.path.join(os.path.dirname(__file__), "images")
    for image in images:
        img.append()
        self.images.append(CreateImage(os.path.join(img, image)))
        txt = image.replace(".png", ".txt")
        with open(txt) as f:
            self.corners.append(f.readlines())


def check_cameras(num=MAX_CAMERAS):
    """ Check cameras. """
    n = 0
    while len(cameras) < num and n <= MAX_CAMERAS: 
        camera = Camera() 
        camera.open_camera(n)
        if camera.get_frame(): 
            cameras.append(camera)
        n += 1
    return len(cameras)

def show_and_select_camera():
    """ Show cameras in different windows for select one camera. """
    if not cameras:
        return camera
    elif len(cameras) == 1:
        return cameras[0]
    elif len(cameras) > 1:
        while not camera:
            for camera in cameras:
                name_windows = str(camera.index)
                img = camera.get_frame()
                ShowImage(name_windows, img)
                key = WaitKey(60)
                # TODO select camera push the key
                SetMouseCallback(name_windows, on_mouse, camera) 
        DestroyAllWindows()

    return camera

