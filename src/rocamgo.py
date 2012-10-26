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

""":var cam: Objeto Cameras 
:Type cam: Cameras
:var cams_found: número de cámaras encontradas en el ordenador
:Type cams_found: int
:var camera: cámara que estamos usando
:Type camera: Camera
:var prev_corners: esquinas del tablero anteriores encontradas
:Type prev_corners: list
:var current_corners: esquinas actuales del tablero encontradas
:Type current_corners: list
:var good_corners: últimas esquinas buenas encontradas
:Type good_corners: list
:var img: imagen actual sacada de la cámara o video
:Type img: IplImage 
:var ideal_img: tablero en formato ideal
:Type ideal_img: IplImage 
:var goban: Objeto tablero
:Type goban: Goban
:var circles: circulos encontrado en la imagen
:Type circles: CvMat
:var false_stones: contador para piedras falsas, no son negras o blancas
:Type false_stones: int
:var stones: piedras detectadas como negras o blancas
:Type stones: list
:var pt: centro de la piedra
:Type pt: tuple
:var radious: radio de la piedra
:Type radious: float
:var color: color de la piedra
:Type color: int
:var key: tecla pulsada       
:Type key: int
"""

from src.cameras import Cameras
from src.search_goban import search_goban
from src.check_goban_moved import check_goban_moved
from src.perspective import perspective
from src.search_stones import search_stones
from src.search_stones import check_color_stone
from src.stone import Stone
from src.goban import Goban
from src.cte import BLACK
from src.cte import WHITE
from src.cte import GOBAN_SIZE
from copy import copy
from sys import path
from record import Record
from cv import ShowImage
from cv import WaitKey
from cv import Circle
from cv import CaptureFromFile
from cv import QueryFrame
from cv import Get1D
from cv import Round
from cv import CV_RGB
import argparse



def main(parser):

    print "Camer, video, record"
    print parser.camera
    print parser.video
    print parser.record

    if parser.camera:
        cam = Cameras()
        cams_found = cam.check_cameras(int(parser.camera))
        camera = cam.show_and_select_camera()
        # TODO
        threshold=190
    elif parser.video:
        camera = CaptureFromFile(parser.video)
        threshold=150 
    if parser.record:
        record = Record(parser.record, QueryFrame(camera))

    prev_corners = None
    current_corners = None
    good_corners = None
    ideal_img = None
    goban = Goban(GOBAN_SIZE)

    while camera: 
        # Select image from camera 
        # TODO
        #img = camera.get_frame()
        img = QueryFrame(camera) # Test videos
        if parser.record:
            record.add_frame(img)

        # previous corners
        prev_corners = copy(current_corners)

        # Detect goban
        current_corners = search_goban(img)
        if not current_corners:
            current_corners = copy(prev_corners)

        # Check goban moved 
        if check_goban_moved(prev_corners, current_corners):
            good_corners = copy(current_corners)
            #print "MOVED"
        
        if good_corners:
            # Paint corners for tested 
            for corner in good_corners:
                Circle(img, corner, 4, (255,0,0), 4, 8, 0)
            # Transform goban to ideal form
            ideal_img = perspective(img, good_corners) # TODO no hallar 2 veces

        if ideal_img:
            circles = search_stones(ideal_img, good_corners)
            false_stones = 0
            stones = []
            for n in range(circles.cols):
                pixel = Get1D(circles, n)
                pt = (Round(pixel[0]), Round(pixel[1]))
                radious = Round(pixel[2])
                # Comprobar el color en la imagen
                color = check_color_stone(pt, radious, ideal_img, threshold)
                if color == BLACK:
                    #print "BLACK"
                    Circle(ideal_img, pt, radious, CV_RGB(255,0,0),2)
                    stones.append(Stone(color, img=ideal_img, pix=pt))
                elif color == WHITE:
                    #print "WHITE"
                    Circle(ideal_img, pt, radious, CV_RGB(0,255,0),2)
                    stones.append(Stone(color, img=ideal_img, pix=pt))
                else:
                    #Circle(ideal_img, pt, radious, CV_RGB(255,255,0),2)
                    false_stones += 1

            #print "Hay %d piedras. " %(circles.cols - false_stones)
            # Añadimos las piedras para trabajar con ellas estadísticamente 
            goban.add_stones_to_statistical(stones)

            ShowImage("Ideal", ideal_img)
            

        # Show image
        ShowImage("Camera", img)

        
        # Detect stone
        
        # Upload to internet

        # FPS
        key = WaitKey(1)
        if key == 27: # Esc
            goban.kifu.end_file()
            goban.igs.close()
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rocamgo option. ')
    parser.add_argument('--record', action='store',
         help='Record video for help to developers. ')
    parser.add_argument('--version', action='version', version='Rocamgo 0.33')
    capture_source_arg_group = parser.add_mutually_exclusive_group(required='true')
    capture_source_arg_group.add_argument('--camera', action='store',
        help='Numbers of cameras in the computer. ')
    capture_source_arg_group.add_argument('--video', action='store', 
        help='Filename video. ')
    results = parser.parse_args()

    main(results)
