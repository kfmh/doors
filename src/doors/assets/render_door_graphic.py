# import json
# import time

# # import door properties json file
# with open(f'door_name.json', 'r') as f:
#     door = json.load(f)

# # Clean up doors.txt to doors_graphics list
# def clean_up_graphics():
#     with open('doors.txt', 'r') as f:
#         door_graphics = f.readlines()
#     for i, line in enumerate(door_graphics):
#         if i != len(door_graphics)-1:
#             door_graphics[i] = line[:-1]
#         else:
#             door_graphics[i] = line
#     return door_graphics
    
# door_graphics = clean_up_graphics()
# door_graphics
# def print_property_line(door_propertys, door_graphics):
#     door_property_str = f"        MMMMMMMd|                          |bMMMMMMM"

#     ppy_line_index = [3, 4, 5, 6, 7, 8, 
#                       12, 13, 14, 15, 16, 
#                       17, 18, 19, 20]
    

#     for i , property_index in enumerate(door_propertys):
#         pct = door_propertys[property_index]['percentage']
#         ppy = door_propertys[property_index]['property']

#         start_property = 19 + (3 - len(str(pct)))
#         start_str = door_property_str[:start_property]
        
#         separator_str = "% : " 

#         end_property = len(start_str) + len(str(pct)) + len(ppy) + len(separator_str)
#         end_str = door_property_str[end_property:]

#         property_str = f"{start_str}{pct}{separator_str}{ppy}{end_str}"

#         door_graphics[ppy_line_index[i]] = property_str
    
#     for i in door_graphics:
#         time.sleep(0.05)
#         print(i)

# print_property_line(door['door_name'], door_graphics)


import json
import curses
import time

# Load door properties from JSON file
with open('door_name.json', 'r') as f:
    door = json.load(f)

# Clean up doors.txt to doors_graphics list
def clean_up_graphics():
    with open('doors.txt', 'r') as f:
        door_graphics = f.readlines()
    door_graphics = [line.strip('\n') for line in door_graphics]
    return door_graphics

door_graphics = clean_up_graphics()

def print_property_line(door_propertys, door_graphics, stdscr):
    door_property_str = "        MMMMMMMd|                          |bMMMMMMM"
    ppy_line_index = [3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for i, property_index in enumerate(door_propertys):
        pct = door_propertys[property_index]['percentage']
        ppy = door_propertys[property_index]['property']

        start_property = 19 + (3 - len(str(pct)))
        start_str = door_property_str[:start_property]
        
        separator_str = "% : "

        end_property = len(start_str) + len(str(pct)) + len(ppy) + len(separator_str)
        end_str = door_property_str[end_property:]

        property_str = f"{start_str}{pct}{separator_str}{ppy}{end_str}"

        door_graphics[ppy_line_index[i]] = property_str
    
    for i, line in enumerate(door_graphics):
        time.sleep(0.05)
        stdscr.addstr(i, 0, line)
        stdscr.refresh()

def main(stdscr):
    # Set up curses environment
    stdscr.clear()
    curses.curs_set(0)
    print_property_line(door['door_name'], door_graphics, stdscr)
    stdscr.getch()  # Wait for user input to close

# Run the curses application
curses.wrapper(main)
