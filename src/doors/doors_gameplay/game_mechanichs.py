import curses 
import json
import random
from maze import Maze
from graphics import RenderASCII

class Game:
    """Main game loop"""
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
        """Initialize variables for the game.

        Args:
            stdscr (object): Curses window object
            hide_maze (bool): Hides maze
            path (list): x,y coordinates of the path
            assets_xy_list (list): list of x,y coordinates of assets
            size_x (int, optional): Width of board. Defaults to 4.
            size_y (int, optional): _description_. Defaults to 5.
            resource_pickups (int, optional): Count of resource pickups
            . Defaults to 0.
            illuminate_pickups (list, optional): List of string charchters.
            . Defaults to [].
        """
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
        """_summary_

        Args:
            key (obejct): Player input key, left, up, down, right

        Returns:
            tuple: with (x, y) coordinates of player position 
        """
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

        return (self.player_x, self.player_y)
    
    def illuminate_maze(self, steps):
        """Sets how many steps the maze should be visible

        Args:
            steps (int): How many steps the player can take before
            maze goes dark again.
        """
        self.illuminate = steps

    def run(self, render_method, assets_xy_list):
        """Starts the game loop

        Args:
            render_method (object): Method of rendering graphics
            assets_xy_list (list): list of (x, y) coordiantes for game assets 
        """
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
