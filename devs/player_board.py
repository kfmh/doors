import curses
import random

class Game:
    def __init__(self, 
                 stdscr, 
                 size_x=20, 
                 size_y=40, 
                 num_squares=5, 
                 square_size=4):
        self.stdscr = stdscr
        self.board_size_x = size_x
        self.board_size_y = size_y
        self.player_x = 1
        self.player_y = 1
        self.squares = self.generate_squares(num_squares, square_size)

    def is_within_bounds(self, x, y):
        return 1 <= x < self.board_size_x - 1 \
            and 1 <= y < self.board_size_y - 1

    def is_inside_square(self, x, y):
        for square_x, square_y, square_size in self.squares:
            if square_x <= x < square_x + square_size \
            and square_y <= y < square_y + square_size:
                return True
        return False

    def draw_board(self):
        self.stdscr.clear()
        for i in range(self.board_size_x):
            for j in range(self.board_size_y):
                if i == 0 or i == self.board_size_x - 1 \
                or j == 0 or j == self.board_size_y - 1:
                    self.stdscr.addstr(i, 2 * j, "#")
                elif i == self.player_x and j == self.player_y:
                    self.stdscr.addstr(i, 2 * j, "X")
                elif self.is_on_square_border(i, j):
                    self.stdscr.addstr(i, 2 * j, "#")
                else:
                    self.stdscr.addstr(i, 2 * j, " ")

        self.stdscr.refresh()

    def generate_squares(self, num_squares, square_size):
        squares = []
        while len(squares) < num_squares:
            x = random.randint(1, self.board_size_x - square_size - 1)
            y = random.randint(1, self.board_size_y - square_size - 1)
            opening_side = random.choice(["top", "bottom", "left", "right"])
            opening_pos = random.randint(1, square_size - 2)
            new_square = (x, y, square_size, opening_side, opening_pos)

            if all(not self.squares_overlap(new_square, existing_square) for existing_square in squares):
                squares.append(new_square)
        return squares

    def squares_overlap(self, square1, square2):
        x1, y1, size1, _, _ = square1
        x2, y2, size2, _, _ = square2
        return (x1 < x2 + size2 and x1 + size1 > x2 and
                y1 < y2 + size2 and y1 + size1 > y2)

    def is_on_square_border(self, x, y):
        for square_x, square_y, square_size, opening_side, opening_pos in self.squares:
            # Check each border of the square
            for i in range(square_size):
                border_positions = [
                    (square_x, square_y + i),  # left border
                    (square_x + i, square_y),  # top border
                    (square_x + square_size - 1, square_y + i),  # right border
                    (square_x + i, square_y + square_size - 1)  # bottom border
                ]

                # Check if position matches any border position
                if (x, y) in border_positions:
                    # Allow opening
                    if opening_side == "top" and x == square_x and y == square_y + opening_pos:
                        continue
                    if opening_side == "bottom" and x == square_x + square_size - 1 and y == square_y + opening_pos:
                        continue
                    if opening_side == "left" and x == square_x + opening_pos and y == square_y:
                        continue
                    if opening_side == "right" and x == square_x + opening_pos and y == square_y + square_size - 1:
                        continue
                    return True  # It's a border position
        return False

    def update_player_position(self, key):
        new_x, new_y = self.player_x, self.player_y
        if key == curses.KEY_UP:
            new_x -= 1
        elif key == curses.KEY_DOWN:
            new_x += 1
        elif key == curses.KEY_LEFT:
            new_y -= 1
        elif key == curses.KEY_RIGHT:
            new_y += 1

        # Check if the new position is within bounds and not a solid wall
        if self.is_within_bounds(new_x, new_y) and not self.is_on_square_border(new_x, new_y):
            self.player_x, self.player_y = new_x, new_y

    def run(self):
        curses.curs_set(0)
        self.draw_board()
        while True:
            key = self.stdscr.getch()
            self.update_player_position(key)
            self.draw_board()

def main(stdscr):
    game = Game(stdscr)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
