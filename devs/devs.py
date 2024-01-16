import curses 
import random
import argparse



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
                 size_x=4,
                 size_y=5):
        self.stdscr = stdscr
        self.board_size_x = size_x
        self.board_size_y = size_y
        self.player_x = 1
        self.player_y = 1
        self.path = []
        self.generate_maze()
        self.hide_maze = hide_maze
    
    def generate_maze(self):

        # random.seed(2)
        top_left = (1,1)
        bottom_right = (self.board_size_x - 1, self.board_size_y - 1)
        top_right = (self.board_size_x - 1, 1)
        bottom_left = (1, self.board_size_y -1 )

        x, y = top_left[0], top_left[1]
        while x !=  self.board_size_x\
        and y != self.board_size_y:
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

    def is_within_bounds(self, x, y):
        """Returns bool if player is within bounds"""
        return 1 <= y < self.board_size_y - 1\
            and 1 <= x < self.board_size_x - 1
    
    def is_on_path(self, x, y):
        """Returns bool if player is on path"""
        return (x, y) in self.path
    
    def draw_board(self, pos):
        self.stdscr.clear()
        for y in range(self.board_size_y):
            for x in range(self.board_size_x):
                if y == 0 or y == self.board_size_y - 1 \
                or x == 0 or x == self.board_size_x - 1:
                    self.stdscr.addstr(y, 2 * x, '#')
                elif y == self.player_y and x == self.player_x:
                    self.stdscr.addstr(y, 2 * x, 'x')
                elif self.is_on_path(x, y):
                    if self.hide_maze:
                        if (x,y) == (self.player_x - 1,  self.player_y):
                            self.stdscr.addstr(y, 2 * x, '.') # Path behind
                        elif (x,y) == (self.player_x + 1,  self.player_y):
                            self.stdscr.addstr(y, 2 * x, '.') # Path infront
                        elif (x,y) == (self.player_x,  self.player_y + 1):
                            self.stdscr.addstr(y, 2 * x, '.') # Path above
                        elif (x,y) == (self.player_x,  self.player_y - 1):
                            self.stdscr.addstr(y, 2 * x, '.') # Path below
                    else: 
                        self.stdscr.addstr(y, 2 * x, '.')
        self.stdscr.addstr(f'\n{str(pos)}')
        # self.stdscr.addstr(f'\n{str(self.path)}')

    def update_player_position(self, key):
        new_x, new_y = self.player_x, self.player_y
        if key == curses.KEY_UP:
            new_y -= 1
        elif key == curses.KEY_DOWN:
            new_y += 1
        elif key == curses.KEY_LEFT:
            new_x -= 1
        elif key == curses.KEY_RIGHT:
            new_x += 1
        
        if self.is_within_bounds(new_x, new_y) \
        and self.is_on_path(new_x, new_y) \
        and new_x != 0 and new_y != 0:
            self.player_x, self.player_y = new_x, new_y
        return [self.player_x, self.player_y]
    
    def run(self):
        curses.curs_set(0)
        self.draw_board([0, 0])
        while True:
            key = self.stdscr.getch()
            pos = self.update_player_position(key)
            self.draw_board(pos)

def main(stdscr):
    game = Game(stdscr, args.show_maze, size_x= 30, size_y= 20, )
    game.run()

if __name__=="__main__":
    curses.wrapper(main)