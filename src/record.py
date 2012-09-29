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

from cv import CreateVideoWriter
from cv import WriteFrame
from cv import CV_FOURCC


class Record:
    """ Grabar video de la partida para enviar al desarrollador y poder ayudarlo
    a mejorar el programa. """
    def __init__(self, filename, frame):
        """
        :Param filename: Nombre del archivo del video.  
        :Type filename: str
        """
        FPS = 8
        MJPG = 1196444237 # CV_FOURCC('M','J','P','G')
        MPEG_1 = CV_FOURCC('P','I','M','1') 
        motion_jpeg = CV_FOURCC('M','J','P','G') 
        MPEG_42 = CV_FOURCC('M','P','4','2') 
        MPEG_43 = CV_FOURCC('D','I','V','3') 
        MPEG_4 = CV_FOURCC('D','I','V','X') 
        H263 = CV_FOURCC('U','2','6','3') 
        H263I = CV_FOURCC('I','2','6','3') 
        FLV1 = CV_FOURCC('D','I','V','X') 

        self.video = CreateVideoWriter(filename, FLV1, FPS, (frame.width, frame.height))
        print "SELFFFF", self.video
        self.frame = 0

    def add_frame(self, frame):
        """ 
        :Param frame: Frame del video
        :Type frame: iplimage
        """
        self.frame += 1
        add = WriteFrame(self.video, frame)
        print "WriteFrame -->", add

    def part_video(self, first_frame, last_frame):
        """ Dado dos frames, obtener el video que se encuentre entre ambos.
        :Param first_frame: Frame donde comenzará el video.
        :Type first_frame: int 
        :Param last_frame: Frame donde finalizará el video. 
        :Type last_frame: int
        """
        pass #TODO

