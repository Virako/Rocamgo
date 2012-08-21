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


from cte import GOBAN_SIZE
from cte import WHITE
from cte import BLACK

class Goban:
    """Contains a matrix of Stones. """

    def __init__(self):
        """ Create empty matrix. 
            :param size: goban's size
            :type size: int"""
        self.matrix = [[None] * GOBAN_SIZE for i in range(GOBAN_SIZE)]
    
    
    def change_stone(self, pos, stone):
        """Edit stone in goban. """
        self.matrix[pos[0]][pos[1]] = stone

    def change_stones(self, pos_list, stones_list):
        """Edit stones in goban. """
        for index in range(len(pos_list)):
            self.change_stone(pos_list[index], stones_list[index])

    def __str__(self):
        string = ""
        for x in range(GOBAN_SIZE):
            for y in range(GOBAN_SIZE):
                if self.matrix[x][y] == BLACK:
                    string += " x "
                elif self.matrix[x][y] == WHITE:
                    string += " o "
                elif not self.matrix[x][y]:
                    string += " · "
            string += "   " + str(x+1) + "\n"
        return string
    
    
