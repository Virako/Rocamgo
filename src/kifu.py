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

import os.path
from datetime import datetime
from cte import BLACK
from cte import WHITE
from cte import HEADER_SGF
import cte

class Kifu:
    """Create file(.sgf) for save the game. """

    def __init__(self, player1="j1", player2="j2", handicap=0, path="sgf", \
            rank_player1='20k', rank_player2='20k'):
        """ TODO Add information about players, path, filename. """
        self.num_jug = 0
        self.player_black = player1
        self.player_white = player2
        filename = str(datetime.now())  + "_" + player1 + "_vs_" + player2
        self.dir = os.path.join(path, filename + ".sgf") # TODO with module os
        header_file = HEADER_SGF
        header_file += [ "\nPB[%s]" %player1, "\nBR[%s]" %rank_player1, \
                         "\nPW[%s]" %player2, "\nWR[%s]" %rank_player2]
        with open(self.dir, "w") as f:
            f.writelines(header_file)


    def add_stone(self, pos, color):
        """ TODO """
        coord = chr(pos[0]+97) + chr(pos[1]+97) 
        with open(self.dir, "a") as f:
            if color == BLACK:
                f.write("\n;B[%s]" %coord)
            elif color == WHITE:
                f.write("\n;W[%s]" %coord)
            else:
                print _("el color debe ser BLACK or WHITE")


    def end_file(self, part=None):
        """Part es para guardar en otro archivo, lo que llevemos de partida."""
        # TODO hacer la parte de part
        with open(self.dir, "a") as f:
            f.write(")")

