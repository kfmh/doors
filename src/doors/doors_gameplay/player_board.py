import curses
import random
import argparse

# Create parsers
parser = argparse.ArgumentParser(
    description='This is the core game mechanics script for Doors')

parser.add_argument('--show_maze', 
                    action='store_false', 
                    help='Shows the entire maze')

args = parser.parse_args()

class Game:
    def __init__(self,
                 stdscr,
                 hide_maze,
                 size_x=4,
                 size_y=5,
                 resource_pickups = 0):
        self.stdscr = stdscr
        self.board_size_x = size_x
        self.board_size_y = size_y
        self.player_x = 1
        self.player_y = 1
        self.path = []
        self.assets_xy_list = []
        
