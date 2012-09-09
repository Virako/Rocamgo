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
from functions import direction_between_two_points as direction
from functions import get_max_edge
from math import acos
from math import hypot


def is_same_quadrant(v1, v2):
    """ Comprueba si dos vectores pasados por parámetros se encuentran en el
    mismo cuadrante. 
    :param v1: vector
    :type v1: tuple
    :param v2: vector
    :type v2: tuple
    :return: True si se encuentran los vectores en el mismo cuadrante. 
    :rtype: bool """
    return v1[0]*v2[0] >= 0 and v1[1]*v2[1] >= 0


def degress_between_two_vectors(v1, v2):
    """ Halla los grados que existen entre dos vectores dados. 
    :param v1: vector
    :type v1: tuple
    :param v2: vector
    :type v2: tuple
    :return: grados en radianes
    :rtype: float """
    if v1 == v2:
        return 0
    try:
        v1_mod = hypot(v1[0], v1[1])
        v2_mod = hypot(v2[0], v2[1])
        v1 = (v1[0]/v1_mod, v1[1]/v1_mod)
        v2 = (v2[0]/v2_mod, v2[1]/v2_mod)
        value = abs(v1[0]*v2[0] + v1[1]*v2[1]) / \
        (hypot(v1[0], v2[0]) * hypot(v1[1], v2[1])) 
        return acos(value)
    except ZeroDivisionError:
        return 0
    except ValueError:
        print "ValueError" # TODO


def check_directions(directions):
    """ Comprueba si las direcciones entre los 4 vecores de movimiento de los
    corners del tablego tienen la misma dirección. 
    :param directions: lista de vectores directores
    :type directions: list
    :return: True si todos o ninguno de los vectores tienen la misma dirección.
    :rtype: bool
    """
    boolean = []
    for x in range(len(directions)-1):
        for y in range(x+1, len(directions)):
            if is_same_quadrant(directions[x], directions[y]) and \
                degress_between_two_vectors(directions[x], directions[y]) < 30:
                # misma direccion
                boolean.append(True)
            else:
                #distinta dirección
                boolean.append(False)
    return sum(boolean) in (0, len(boolean))


def check_goban_moved(prev_corners, current_corners):
    """ Comprobamos si es posible el movimiento de tablero detectado.
    :param prev_corners: corners detectados anteriormente
    :type prev_corners: list
    :param current_corners: corners detectados actualmente
    :type current_corners: list
    :return: True si el tablero se ha movido
    :rtype: bool """

    if not prev_corners or not current_corners:
        return True
    dist_min_of_movement = get_max_edge(prev_corners)/(2*GOBAN_SIZE)
    " Comprobamos primero si existe mucho movimiento. "
    dist = []
    directions = []
    for i in xrange(NUM_EDGES):
        dist.append(abs(distance(prev_corners[i], current_corners[i])))
        directions.append(direction(prev_corners[i], current_corners[i]))
    f = lambda x: x>1
    dist_list = filter(f, dist)
    if len(dist_list) > 2:
        # min_mov=1/3 square TODO check impossible movement (Direcction)
        min_mov = get_max_edge(prev_corners)/((GOBAN_SIZE-1)*3.0)
        dist_list.sort()
        if (dist_list[-1] - dist_list[0]) < min_mov:
            return check_directions(directions)
        elif (dist_list[-1] - dist_list[-3]) < min_mov:
            return check_directions(directions)
        else:
            return False
    else:
        return False

