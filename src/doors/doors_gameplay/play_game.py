import curses 
import json
import argparse
import random
from maze import Maze
from graphics import RenderASCII
from game_mechanichs import Game
# Create the parser
parser = argparse.ArgumentParser(description='Example argparse program')

# Add arguments
parser.add_argument('--show_maze', '-sm', 
                    action='store_false', 
                    help='Show maze')

# Parse arguments
args = parser.parse_args()

def main(stdscr):
    """Main function runs when script is called

    Args:
        stdscr (object): Curses window object
    """
    with open('../courses/genesis.json', 'r') as f:
        file = json.load(f)
    
    board_size_x = 40
    board_size_y = 30
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