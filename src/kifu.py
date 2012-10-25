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
:var player1: nombre del jugador 1
:Type player1: str
:var player2: nombre del jugador 2
:Type player2: str
:var handicap: numero de piedras de ventaja 
:Type handicap: int
:var path: directorio donde guardaremos las partidas 
:Type path: str
:var rank_player1: nivel del jugador 1
:Type rank_player1: str
:var rank_player2: nivel del jugador 2
:Type rank_player2: str
:var num_jug: número de jugada actual
:Type num_jug: int
:var dir: dirección del directorio donde guardaremos la partida
:Type dir: str
"""

import os.path
from datetime import datetime
from cte import BLACK
from cte import WHITE
from cte import HEADER_SGF
import cte

class Kifu:
    """Clase para crear un fichero .sgf y guardar la partida. """

    def __init__(self, player1="j1", player2="j2", handicap=0, path="sgf", \
            rank_player1='20k', rank_player2='20k'):
        """Inicializamos configuración del archivo sgf. 

        :Param  player1: nombre del jugador 1
        :Type  player1: str
        :Keyword  player1: j1 por defecto
        :Param  player2: nombre del jugador 2
        :Type  player2: str
        :Keyword  player2: j2 por defecto
        :Param  handicap: handicap dado en la partida
        :Type  handicap: int
        :Keyword  handicap: ninguno por defecto (0)
        :Param  path: ruta relativa donde guardamos el fichero
        :Type  path: str
        :Keyword  path: carpeta sgf por defecto
        :Param  rank_player1: rango del jugador 1
        :Type  rank_player1: str
        :Keyword  rank_player1: 20k por defecto, nivel de inicio en el go
        :Param  rank_player2: rango del jugador 2
        :Type  rank_player2: str
        :Keyword  rank_player2: 20k por defecto, nivel de inicio en el go """
        self.num_jug = 0
        self.player_black = player1
        self.player_white = player2
        filename = str(datetime.now()).replace(" ","_")  + "_" + player1 + "_vs_" + player2
        self.dir = os.path.join(path, filename + ".sgf")
        header_file = HEADER_SGF
        header_file += [ "\nPB[%s]" %player1, "\nBR[%s]" %rank_player1, \
                         "\nPW[%s]" %player2, "\nWR[%s]" %rank_player2]
        with open(self.dir, "w") as f:
            f.writelines(header_file)


    def add_stone(self, pos, color):
        """Añadir piedra al sgf. 

        :Param pos: posición de la piedra
        :Type pos: tuple
        :Param color: color de la piedra 
        :Type color: int """
        coord = chr(pos[0]+97) + chr(pos[1]+97) 
        with open(self.dir, "a") as f:
            if color == BLACK:
                f.write("\n;B[%s]" %coord)
            elif color == WHITE:
                f.write("\n;W[%s]" %coord)
            else:
                print _("el color debe ser BLACK or WHITE")
        self.num_jug += 1


    def end_file(self):
        """Cerrar el fichero y dejarlo listo para poder abrirlo."""
        with open(self.dir, "a") as f:
            f.write(")")

