from render_door_graphic import ASCIIDoor
import json
import curses
# # Load door properties from JSON file
with open('../courses/genesis.json', 'r') as f:
    door = json.load(f)
def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Create an instance of ASCIIDoor with the stdscr
    ase = ASCIIDoor(stdscr)

    door_ = door["genesis"]["doors"]["random_seed"]
    # Add your logic here to use 'ase'

    ase.print_property_line(door_)
    # Refresh the screen to see the changes
    stdscr.refresh()

    # Wait for a key press
    stdscr.getkey()

# Run your program inside the curses environment
curses.wrapper(main)