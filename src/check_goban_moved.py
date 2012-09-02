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

from sys import path
path.append('/usr/lib/pymodules/python2.7')
from cv import QueryFrame
from cv import CaptureFromCAM
from cte import NUM_EDGES
from cte import GOBAN_SIZE
from functions import distance_between_two_points as distance
from functions import get_max_edge


def check_goban_moved(prev_corners, current_corners):
    """ Comprobamos si es posible el movimiento de tablero detectado. """

    if not prev_corners or not current_corners:
        return False
    dist_min_of_movement = get_max_edge(prev_corners)/(2*GOBAN_SIZE)
    " Comprobamos primeramente si existe mucho movimiento. "
    dist = []
    for i in xrange(NUM_EDGES):
        dist.append(abs(distance(prev_corners[i], current_corners[i])))
    f = lambda x: x>1
    dist_list = filter(f, dist)
    if len(dist_list) > 2:
        # min_mov=1/3 square TODO check impossible movement (Direcction)
        min_mov = get_max_edge(prev_corners)/((GOBAN_SIZE-1)*3.0)
        dist_list.sort()
        if (dist_list[-1] - dist_list[0]) < min_mov:
            return True
        elif (dist_list[-1] - dist_list[-3]) < min_mov:
            return True
        else:
            return False
    else:
        return False

