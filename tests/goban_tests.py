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

from src.goban import Goban
import unittest
from nose.tools import *

class Test_goban(unittest.TestCase):
    
    def setUp(self):
        self.goban = Goban()
    
    def tearDown(self):
        self.goban = None
    
    def test_create_matrix(self):
        assert_equals(self.goban.matrix, [[None]*GOBAN_SIZE,]*GOBAN_SIZE)
    
    def _test_change_stone(self):
        # TODO add matrix
        pos = ((0,0), (1,1), (1,2), (2,2))
        stone = (BLACK, WHITE, BLACK, WHITE)
        for i in xrange(len(pos)):
            self.goban.change_stone(pos[i], stone[i])
        assert_equals(self.goban.matrix, [])

    def _test_change_stones(self):
        # TODO add matrix
        pos = ((0,0), (1,1), (1,2), (2,2))
        stone = (BLACK, WHITE, BLACK, WHITE)
        self.goban.change_stones(pos, stone)
        assert_equals(self.goban.matrix, [])


if __name__ == '__main__':
    print "Run test with nosetest"
