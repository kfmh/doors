import json
import random

class GameItems:
    def __init__(self, course_name):
        self.course_name = course_name
        with open(f'../courses/{course_name}.json', 'r') as f:
            course = json.load(f)
        self.course = course

    def generate_resourses(self):
        illuminate_pickups_count = self.course[self.course_name]["game_items"]["illuminate_packs"] 
        
        illuminate_pickups = ['*' for i in range(illuminate_pickups_count)]
        return illuminate_pickups

    def generate_doors(self):
        doors = self.course[self.course_name]["doors"]
        doors_list = list(doors.keys())
        doorframes = ['∩' for i in range(len(doors_list))]
            
        return doors, doors_list, doorframes

class Maze:
    def __init__(self,
             board_size_x,
             board_size_y,
             path = [],
             seed = None):
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.path = path
        self.seed = seed

    def generate_maze_loop(self, 
                           x, y, 
                           x_limit, y_limit,
                           x_, y_):
        """Loop for generating maze, recives a start postion
        and limit. From start position it alterantes dirction untill 
        it reaches the limit

        Args:
            x (int): Start x coordinate
            y (int): Start y coordinate
            x_limit (int): Runs untill limit
            y_limit (int): Runs untill limit
            x_ (bool): Should x increse 
            y_ (bool): Should y increse 
        """
        # Start coordinates top left corner
        x_steps = 0
        y_steps = 0
        while x != x_limit and y != y_limit:
            self.path.append((x, y))
            direction = round(random.random())

            if direction or x_steps > 0 and y_steps == 0:
                if x_: x += 1 
                else:  x -= 1
                if x_steps > 1:
                    x_steps = 0 
                else:
                    x_steps  += 1 

            else: 
                if y_: y += 1
                else:  y -= 1

                if y_steps > 1:
                    y_steps = 0 
                else:
                    y_steps  += 1 

    def generate_maze(self):
        """Generates a maze as a list of tupels with (x,y) coordinates 

        Returns:
            list: list of (x,y) coordinates
        """
        # random.seed(seed)

        top_left     = (1,1)
        bottom_right = (self.board_size_x - 1, self.board_size_y - 1)
        top_right    = (self.board_size_x - 1, 1) 
        bottom_left  = (1, self.board_size_y - 1)
        
        gen_maze_vars = [
            [top_left[0], top_left[1], 
             self.board_size_x, self.board_size_x,
             True, True
             ],
            
            [top_right[0], top_right[1], 
             1, self.board_size_y - 1,
             False, True
             ],

            [bottom_right[0], bottom_right[1], 
             0, 0,
             False, False
             ],

            [bottom_left[0], bottom_left[1],
             top_right[0], 0,
             True, False, 
             ],

             ]
        # Start coordinates top left corner
        for i in gen_maze_vars:
            self.generate_maze_loop(
                i[0], i[1], i[2], i[3], i[4], i[5]
            )

        return self.path
