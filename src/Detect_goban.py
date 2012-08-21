import unittest
from opencv import 

import sys
sys.path.append("../src/")

from Stone import Stone
from Goban import Goban
from cte import *


class Detect_goban(unittest.TestCase):

    def setUp(self):


    def tearDown(self):
        self.goban = None
        self.goban_6 = None
        pass 
    
    # Create and modificate goban 
    def test_create_matrix_6x6_in_goban(self):
        goban = Goban(6)
        self.assertEquals(self.goban_6, goban.matrix)
    
    def test_create_matrix_9x9_in_goban(self):
        goban = Goban(9)
        self.assertEquals(self.goban_9, goban.matrix)
    
    def test_change_stone(self):
        goban = Goban(6)
        goban.change_stone((0,0), ST_BLACK)
        self.assertEquals(goban.matrix,self.goban_6_1)

    def test_change_stones(self):
        goban = Goban(6)
        pos_list = ( (0,0),(1,0),(2,0),(0,1),(0,0))
        stones_list = (ST_BLACK, ST_WHITE, ST_BLACK, ST_WHITE, ST_NONE)
        goban.change_stones(pos_list, stones_list)
        self.assertEquals(goban.matrix,self.goban_6_4)

    def test_set_corner_ext(self):
        state = ((10,100),(500,100),(450,90),(450,490))
        goban = Goban(6)
        goban.set_corners_ext(state)
        self.assertEquals(goban.get_corners_ext(), state)

    def test_set_corner_int(self):
        state = ((10,100),(500,100),(450,90),(450,490))
        goban = Goban(6)
        goban.set_corners_int(state)
        self.assertEquals(goban.get_corners_int(), state)
        
    def test_set_position_pixels_in_intersection(self):
        pos_inter_list = ((1,1),(4,3),(5,3))
        pos_pixel_list = ((100,100),(400,400),(401,450))
        goban = Goban(9)
        goban.set_pos_intersections(pos_inter_list, pos_pixel_list)
        self.assertEquals(goban.matrix, self.goban_9_pixel_changed)

    # Detect goban 
    def test_detect_all_corner_with_brightness(self):
        # TODO
        self.assertTrue(False)
    
    def test_detect_all_corner_without_brightness(self):
        # TODO
        self.assertTrue(False)
    
    def test_detect_corner_with_hand_disturb_in_goban(self):
        # TODO
        self.assertTrue(False)

    def test_detect_corner_with_stone_in_goban(self):
        # TODO
        self.assertTrue(False)

    # Create and modificate kifu (Is a file where the game is saved.)
    def test_create_game_none_for_two_players(self):
        # TODO
        self.assertTrue(False)

    def test_create_game_none_for_two_players_with_handicap(self):
        # TODO
        self.assertTrue(False)

    def test_add_stone_in_the_kifu(self):
        # TODO
        self.assertTrue(False)

    def test_add_stones_in_the_kifu(self): # state of game. Un estado del juego
        # TODO
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
