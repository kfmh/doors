import curses 
import argparse
import random
# from maze import Maze
from generate import Maze, GameItems
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
    
    board_size_x = 40
    board_size_y = 30
    maze = Maze(board_size_x, board_size_y)
    path = maze.generate_maze()
    # Generate game items
    course = GameItems('genesis')
    illuminate_pickups = course.generate_resourses()
    resource_count = len(illuminate_pickups)
    door_propertys, doors_name_list, door_graphics = course.generate_doors()

    assets_xy_list = random.sample(path, len(illuminate_pickups))
    doors_xy_list  = random.sample(path, len(door_propertys))    
    
    while any(item in doors_xy_list  for item in assets_xy_list):
        doors_xy_list  = random.sample(path, len(door_propertys))    

    game = Game(stdscr, 
                args.show_maze, 
                path = path,
                assets_xy_list = assets_xy_list,
                doors_xy_list  = doors_xy_list,
                doors_name_list = doors_name_list,
                size_x= board_size_x, 
                size_y= board_size_y, 
                illuminate_pickups = illuminate_pickups,
                )
    
    render_ASCII = RenderASCII(stdscr,
                               board_size_x,
                               board_size_y,
                               path,
                               assets_xy_list,
                               doors_xy_list,
                               door_propertys,
                               resource_count
                               )
    game.run(render_ASCII, assets_xy_list, doors_xy_list, door_graphics)

if __name__=="__main__":
    curses.wrapper(main)