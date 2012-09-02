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

from cte import NUM_EDGES
from cte import GOBAN_SIZE
from math import sqrt

def distance_between_two_points(p1, p2):
    return sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)


def get_max_edge(corners):
    edges = []
    for c in xrange(NUM_EDGES):
        edges.append(sqrt((corners[c][0]-corners[(c+1)%4][0])**2 + \
                    (corners[c][1]-corners[(c+1)%4][1])**2))
    return int(max(edges)*((GOBAN_SIZE+2.0)/GOBAN_SIZE))


def get_external_corners(corners):
    external_corners = []
    for c in range(len(corners)):
        if c >= 2:
            x = corners[c][0] + distance_between_two_points(corners[c],\
            corners[(c+2)%4])/GOBAN_SIZE/2
        else:
            x = corners[c][0] - distance_between_two_points(corners[c],\
            corners[(c+2)%4])/GOBAN_SIZE/2
        if c == 1 or c == 3:
            y = corners[c][1] + distance_between_two_points(corners[c],\
            corners[(c+2)%4])/GOBAN_SIZE/2
        else:
            y = corners[c][1] - distance_between_two_points(corners[c],\
            corners[(c+2)%4])/GOBAN_SIZE/2
        external_corners.append((x,y))
    return external_corners
