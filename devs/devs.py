import curses

# Initialize the player's position
player_x, player_y = 1, 1  # Start the player inside the wall boundaries
board_size = 10

# Function to draw the game board
def draw_board(stdscr, x, y):
    stdscr.clear()  # Clear the screen

    for i in range(board_size):
        for j in range(board_size):
            if i == 0 or i == board_size - 1 or j == 0 or j == board_size - 1:
                stdscr.addstr(i, 2*j, "#")  # Draw walls
            elif i == x and j == y:
                stdscr.addstr(i, 2*j, "X")  # Draw player
            else:
                stdscr.addstr(i, 2*j, " ")  # Draw empty space
        stdscr.addstr("\n")

    stdscr.refresh()

# Function to handle the game logic
def game(stdscr):
    global player_x, player_y

    # Set up the screen
    curses.curs_set(0)  # Hide cursor

    # Draw the initial board
    draw_board(stdscr, player_x, player_y)

    while True:
        # Wait for key press
        key = stdscr.getch()

        # Update player position based on key press, checking for walls
        if key == curses.KEY_UP and player_x > 1:
            player_x -= 1
        elif key == curses.KEY_DOWN and player_x < board_size - 2:
            player_x += 1
        elif key == curses.KEY_LEFT and player_y > 1:
            player_y -= 1
        elif key == curses.KEY_RIGHT and player_y < board_size - 2:
            player_y += 1

        # Redraw the board
        draw_board(stdscr, player_x, player_y)

# Run the curses application
curses.wrapper(game)
