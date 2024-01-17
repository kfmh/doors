import random


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

    def generate_maze(self):
        # random.seed(seed)
        top_left     = (1,1)
        bottom_right = (self.board_size_x - 1, self.board_size_y - 1)
        top_right    = (self.board_size_x - 1, 1) 
        bottom_left  = (1, self.board_size_y - 1)
        
        # Start coordinates top left corner
        x, y = top_left[0], top_left[1]
        while x != self.board_size_x \
        and y != self.board_size_x:
            self.path.append((x, y))
            direction = round(random.random())
            if direction:
                x += 1
            else: 
                y += 1

        x, y = top_right[0], top_right[1]
        while x != 1 \
        and y != self.board_size_y - 1:
            self.path.append((x, y))
            direction = round(random.random())
            if direction: 
                x -= 1
            else: 
                y += 1

        x, y = bottom_right[0], bottom_right[1]
        while x != 0 \
        and y != 0:
            self.path.append((x, y))
            direction = round(random.random())
            if direction: 
                x -= 1
            else: 
                y -= 1
                
        x, y = bottom_left[0], bottom_left[1]
        while x != top_right[0] \
        and y != 0:
            self.path.append((x, y))
            direction = round(random.random())
            if direction: 
                x += 1
            else: 
                y -= 1
        # print(self.path)
        # assets_xy_list = random.sample(self.path, 4)
        # assets_xy_list = self.path
        return self.path
