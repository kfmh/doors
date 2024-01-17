import curses 
import json
import argparse
import random
from maze import Maze
from graphics import RenderASCII
# import random
# Create the parser
parser = argparse.ArgumentParser(description='Example argparse program')

# Add arguments
parser.add_argument('--show_maze', '-sm', action='store_false', help='Show maze')

# Parse arguments
args = parser.parse_args()

class Game:
    def __init__(self,
                 stdscr,
                 hide_maze,
                 path,
                 assets_xy_list,
                 size_x=4,
                 size_y=5,
                 resource_pickups = 0,
                 illuminate_pickups = []
                 ):
        self.stdscr = stdscr
        self.board_size_x = size_x
        self.board_size_y = size_y
        self.player_x = 1
        self.player_y = 1
        self.path = path
        self.hide_maze = hide_maze
        self.resource_pickups = resource_pickups
        self.assets_xy_list = assets_xy_list
        self.illuminate_pickups = illuminate_pickups
        self.illuminate = 0


    def is_within_bounds(self, x, y):
        """Returns bool if player is within bounds"""
        return 1 <= y < self.board_size_y - 1\
            and 1 <= x < self.board_size_x - 1
    
    def is_on_path(self, x, y):
        """Returns bool if player is on path"""
        return (x, y) in self.path
    
    def update_player_position(self, key):
        new_x, new_y = self.player_x, self.player_y
        if   key == curses.KEY_UP:    new_y -= 1
        elif key == curses.KEY_DOWN:  new_y += 1
        elif key == curses.KEY_LEFT:  new_x -= 1
        elif key == curses.KEY_RIGHT: new_x += 1
        
        if self.is_within_bounds(new_x, new_y) \
        and self.is_on_path(new_x, new_y) \
        and new_x != 0 and new_y != 0:
            self.player_x, self.player_y = new_x, new_y
            if self.illuminate != 0:
                self.illuminate -= 1

            if (self.player_x, self.player_y) in self.assets_xy_list:
                x, y = self.player_x, self.player_y
                self.resource_pickups += 1
                i = self.assets_xy_list.index((x, y))
                self.illuminate_pickups.pop(i)
                self.assets_xy_list.remove((x,y))
                self.illuminate_maze(3)

        return [self.player_x, self.player_y]
    
    def illuminate_maze(self, steps):
        self.illuminate = steps

    def run(self, render_method, assets_xy_list):
        curses.curs_set(0)
        render_method.draw_board(
                        (1,1),
                        self.player_y,
                        self.player_x,
                        assets_xy_list,
                        self.hide_maze,
                        self.resource_pickups,
                        self.illuminate_pickups,
                        self.illuminate)
        try:
            while True:
                # self.draw_board(pos)
                key = self.stdscr.getch()
                pos = self.update_player_position(key)
                render_method.draw_board(
                                        pos,
                                        self.player_y,
                                        self.player_x,
                                        assets_xy_list,
                                        self.hide_maze,
                                        self.resource_pickups,
                                        self.illuminate_pickups,
                                        self.illuminate
                                        )


        except KeyboardInterrupt:
            print("Program interrupted by user. Cleaning up...")

def main(stdscr):
    with open('../courses/genesis.json', 'r') as f:
        file = json.load(f)
    
    
    board_size_x = 70
    board_size_y = 40
    illuminate_pickups_count = file["genesis"]["illuminate_packs"] 
    maze = Maze(board_size_x, board_size_y)
    path = maze.generate_maze()
    illuminate_pickups = ['*' for i in range(illuminate_pickups_count)]
    assets_xy_list = random.sample(path, illuminate_pickups_count)
    game = Game(stdscr, args.show_maze, 
                path = path,
                assets_xy_list = assets_xy_list,
                size_x= board_size_x, 
                size_y= board_size_y, 
                illuminate_pickups = illuminate_pickups
                )
    
    render_ASCII = RenderASCII(stdscr,
                               board_size_x,
                               board_size_y,
                               path,
                               assets_xy_list
                               )
    game.run(render_ASCII, assets_xy_list)

if __name__=="__main__":
    curses.wrapper(main)