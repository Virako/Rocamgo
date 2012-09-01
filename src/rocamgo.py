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
from sys import path
path.append('/usr/lib/pymodules/python2.7')
from cv import ShowImage
from cv import WaitKey
from cv import Circle


def main():
    # Select camera from computer
    cam = Cameras()
    cams_found = cam.check_cameras()
    camera = cam.show_and_select_camera()
    corners = None
    
    while camera: 
        
        # Show current camera
        img = camera.get_frame()

        # TODO Check goban moved 
        goban_moved = True

        # Detect goban
        if goban_moved:
            corners = search_goban(img)
        if corners:
            for corner in corners:
                Circle(img, corner, 4, (255,0,0), 4, 8, 0)
        ShowImage("Camera", img)

        # Transform goban to ideal form
        
        # Detect stone
        
        # Upload to internet

        # FPS
        key = WaitKey(30)
        if key == 27: # Esc
            break

    
if __name__ == "__main__":
    main()
