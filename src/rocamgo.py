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

from src.cameras import Cameras
from src.search_goban import search_goban
from copy import copy
from check_goban_moved import check_goban_moved
from sys import path
path.append('/usr/lib/pymodules/python2.7')
from cv import ShowImage
from cv import WaitKey
from cv import Circle
from cv import CaptureFromFile
from cv import QueryFrame
from perspective import perspective


def main():
    # Select camera from computer
    cam = Cameras()
    cams_found = cam.check_cameras()
    camera = cam.show_and_select_camera()
    #camera = CaptureFromFile('tests/videos/capture1.avi') # Test videos
    prev_corners = None
    current_corners = None
    good_corners = None

    while camera: 
        # Select image from camera 
        img = camera.get_frame()
        #img = QueryFrame(camera) # Test videos

        # previous corners
        prev_corners = copy(current_corners)

        # Detect goban
        current_corners = search_goban(img)
        if not current_corners:
            current_corners = copy(prev_corners)

        # Check goban moved 
        if check_goban_moved(prev_corners, current_corners):
            good_corners = copy(current_corners)
            print "MOVED"
        
        if good_corners:
            # Paint corners for tested 
            for corner in good_corners:
                Circle(img, corner, 4, (255,0,0), 4, 8, 0)
            # Transform goban to ideal form
            ideal_img = perspective(img, good_corners) # TODO no hallar 2 veces
            ShowImage("Ideal", ideal_img)


        # Show image
        ShowImage("Camera", img)

        
        # Detect stone
        
        # Upload to internet

        # FPS
        key = WaitKey(30)
        if key == 27: # Esc
            break

if __name__ == "__main__":
    main()
