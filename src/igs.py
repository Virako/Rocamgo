#!/usr/bin/env python
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


from socket import socket


class Igs:
    """ """
    def __init__(self, user='rocamgo', pwd='qwe'):

        self.s = socket()
        self.s.connect(('igs.joyjoy.net', 7777))
        self.s.recv(4096)
        self.s.send("%s\n" %user)
        self.s.recv(4096)
        self.s.send("%s\n" %pwd)
        self.s.recv(4096)
        self.s.send("teach 19\n")
        self.s.send("title 'Rocamgo'\n")

    
    def add_stone(self, pos):
        if pos[0] >= ord('I')-65:
            pos_igs = chr(pos[0]+66) + str(19-pos[1]) 
        else:
            pos_igs = chr(pos[0]+65) + str(19-pos[1]) 
        self.s.send("%s\n" %pos_igs)

    def close(self):
        self.s.close()
