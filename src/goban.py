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


from src.cte import GOBAN_SIZE
from src.cte import WHITE
from src.cte import BLACK
from src.kifu import Kifu
from igs import Igs

class Goban:
    """Contains a matrix of stones and other matrix for statistical. """

    def __init__(self, size):
        """ Create empty matrix. 
            :param size: goban's size
            :type size: int"""
        self.size = size
        # El valor 0 es para ir sumando(hay piedra) o restando(no hay)
        # El valor 8 es el nº de veces a buscar antes de hacer la estadística
        self.goban = [[None] * size for i in range(size)]
        self.statistical = [[[0, 8]] * size for i in range(size)]
        self.stones = set()
        self.kifu = Kifu()
        user = raw_input("Insert your user: ")
        password = raw_input("Insert your password: ")
        self.igs = Igs(user, password)
    

    def add_stones_to_statistical(self, stones):
        """ Recorremos la matriz statistical para buscar los cambios que se
        hayan realizado anteriormente en alguna intersección, para buscar de
        nuevo y comprobar si existe piedra o no nuevamente. TODO danger capturas 
        
        Recorremos las piedras que actualmente hemos detectado para añadirlas a
        las estadísticas. 
        
        Por último recorremos las piedras que nos han quedado sueltas, las
        cuales sabemos que no las hemos detectado, por lo cual restamos. """
        
        for st in stones:
            self.statistical[st.x][st.y][0] += 1
            self.statistical[st.x][st.y][1] -= 1
            values = self.statistical[st.x][st.y]
            if values[1] <= 0 and values[0] > 0: 
                if self.goban[st.x][st.y] != True:
                    print "Add", st.x+1, st.y+1 
                    # add kifu e igs
                    self.kifu.add_stone((st.x, st.y), st.color)
                    self.igs.add_stone((st.x, st.y))
                    self.statistical[st.x][st.y] = [0, 8]
                    self.goban[st.x][st.y] = True
            
        for st in self.stones.difference(stones):
            self.statistical[st.x][st.y][0] -= 1
            self.statistical[st.x][st.y][1] -= 1
            values = self.statistical[st.x][st.y]
            if values[1] <= 0 and values[0] > 0: 
                if self.goban[st.x][st.y] != True:
                    print "Add", st.x+1, st.y+1
                    # add kifu e igs
                    self.kifu.add_stone((st.x, st.y), st.color)
                    self.igs.add_stone((st.x, st.y))
                    self.statistical[st.x][st.y] = [0, 8]
                    self.goban[st.x][st.y] = True
            elif values[1] <= 0 and values[0] > 0:
                self.statistical[st.x][st.y] = [0, 8]
                if self.goban[st.x][st.y] == True:
                    print "Piedra %d, %d quitada?." %(st.x, st.y)

                # falsa piedra
        self.stones.update(stones)



    def print_st(self):
        string = ""
        for x in range(self.size):
            for y in range(self.size):
                string += '%s' %str(self.statistical[y][x])
            string += "   " + str(x+1) + "\n"
        return string
    

    def __str__(self):
        string = ""
        for x in range(self.size):
            for y in range(self.size):
                if self.goban[y][x] == BLACK:
                    string += " x "
                elif self.goban[y][x] == WHITE:
                    string += " o "
                elif not self.goban[y][x]:
                    string += " · "
            string += "   " + str(x+1) + "\n"
        return string
    
    
