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

"""
:var s: socket para la conexión con el servidor
:Type s: socket
:var user: usuario del servidor Igs
:Type user: str
:var pwd: password correspondiente al usuario de Igs
:Type pwd: str
"""

from socket import socket
from cte import GOBAN_SIZE


class Igs:
    """Clase que se comunica con el servidor de IGS. """
    def __init__(self, user='rocamgo', pwd='qwe'):
        """Inicializamos la conexión con el servidor y creamos un tablero de aprendizaje dentro del servidor para comenzar a subir la partida. 

        :Param user: usuario que se conectará al servidor
        :Type user: str
        :Param pwd: contraseña del usuario para conetarse al servidor
        :Type pwd: str """
        # TODO comprobar que se conecta al servidor
        self.s = socket()
        self.s.connect(('igs.joyjoy.net', 7777))
        self.s.recv(4096)
        self.s.send("%s\n" %user)
        self.s.recv(4096)
        self.s.send("%s\n" %pwd)
        self.s.recv(4096)
        self.s.send("teach %d\n" %GOBAN_SIZE)
        self.s.send("title 'Rocamgo'\n")

    
    def add_stone(self, pos):
        """Añadimos piedra al servidor. 

        :Param pos: posición de la piedra a añadir 
        :Type pos: tuple """
        if pos[0] >= ord('I')-65:
            pos_igs = chr(pos[0]+66) + str(19-pos[1]) 
        else:
            pos_igs = chr(pos[0]+65) + str(19-pos[1]) 
        self.s.send("%s\n" %pos_igs)


    def close(self):
        """Cerramos la conexión con el servidor. """
        self.s.close()
