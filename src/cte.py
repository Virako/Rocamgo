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
:var NUM_EDGES: número de esquinas que existen en un tablero
:Type NUM_EDGES: int
:var RELATION_WEIGHT_HEIGHT: relación anchura/altura que existe en el tablero
:Type RELATION_WEIGHT_HEIGHT: float
:var MAX_CAMERAS: número máximo de cámaras a buscar
:Type MAX_CAMERAS: int
:var GOBAN_SIZE: tamaño del tablero
:Type GOBAN_SIZE: int
:var BLACK: constante para decir que una piedra es negra
:Type BLACK: int
:var WHITE: constante para decir que una piedra es blanca
:Type WHITE: int
:var HEADER_SGF: cabecera de un archivo .sgf 
:Type HEADER_SGF: str
"""

import time

NUM_EDGES = 4
RELATION_WEIGHT_HEIGHT = 14/15.0
MAX_CAMERAS = 99
GOBAN_SIZE = 19
BLACK = 1
WHITE = 2

current_date = time.strftime("%d %b %Y")

HEADER_SGF = [ "(;FF[4]GM[1]SZ[%d]" %(GOBAN_SIZE),
            "\nAP[Rocamgo]",  
            "\nHA[0]", 
            "\nKM[6.5]",
            "\nSZ[%s]" %GOBAN_SIZE,
            "\nDT[%s]" %current_date,
            "\nRU[Japanese]",
          ]

"""
FEATURES OF FILES .SGF
======================

* AB: Add Black: locations of Black stones to be placed on the board prior to the first move.
* AW: Add White: locations of White stones to be placed on the board prior to the first move.
* AN: Annotations: name of the person commenting the game.
* AP: Application: application that was used to create the SGF file (e.g. CGOban2,...).
* B: a move by Black at the location specified by the property value.
* BR: Black Rank: rank of the Black player.
* BT: Black Team: name of the Black team.
* C: Comment: a comment.
* CP: Copyright: copyright information. See Kifu Copyright Discussion.
* DT: Date: date of the game.
* EV: Event: name of the event (e.g. 58th Honinbo Title Match).
* FF: File format: version of SGF specification governing this SGF file.
* GM: Game: type of game represented by this SGF file. A property value of 1 refers to Go.
* GN: Game Name: name of the game record.
* HA: Handicap: the number of handicap stones given to Black. Placment of the handicap stones are set using the AB property.
* KM: Komi: komi.
* ON: Opening: information about the opening (fuseki), rarely used in any file.
* OT: Overtime: overtime system.
* PB: Black Name: name of the black player.
* PC: Place: place where the game was played (e.g.: Tokyo).
* PL: Player: color of player to start.
* PW: White Name: name of the white player.
* RE: Result: result, usually in the format "B+R" (Black wins by resign) or "B+3.5" (black wins by 3.5 moku).
* RO: Round: round (e.g.: 5th game).
* RU: Rules: ruleset (e.g.: Japanese).
* SO: Source: source of the SGF file.
* SZ: Size: size of the board, non square boards are supported.
* TM: Time limit: time limit in seconds.
* US: User: name of the person who created the SGF file.
* W: a move by White at the location specified by the property value.
* WR: White Rank: rank of the White player.
* WT: White Team: name of the White team. 
"""

