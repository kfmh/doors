import curses
import time
from collections import Counter

class RenderASCII:
    def __init__(self, 
                 stdscr,
                board_size_x, 
                board_size_y,
                path,
                assets_xy_list,
                doors_xy_list,
                door_propertys
                ):
        self.assets_xy_list = assets_xy_list
        self.doors_xy_list = doors_xy_list
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.stdscr = stdscr
        self.path = path
        self.door_propertys = door_propertys

        # with open('render_door_graphic_ASCII.txt', 'r') as f:
        #     door_graphics = f.readlines()
        # self.door_graphics = [line.strip('\n') for line in door_graphics]

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    def draw_board(self, 
                   pos,
                   player_y,
                   player_x,
                   assets_xy_list,
                   doors_xy_list,
                   hide_maze,
                   resource_pickups,
                   resources,
                   doors_graphic,
                   illuminate,
                   show_door,
                   door_name
                   ):
        
        self.stdscr.clear()
        r = resources
        d = doors_graphic
        if show_door:
            self.ASCIIDoor(door_name, )
        else:
            for y in range(self.board_size_y):
                for x in range(self.board_size_x):
                    if y == 0 or y == self.board_size_y - 1 \
                    or x == 0 or x == self.board_size_x - 1:
                        self.stdscr.addstr(y, 2 * x, '#')
                    elif y == player_y and x == player_x:
                        self.stdscr.attron(curses.color_pair(2))  # Turn on red color
                        self.stdscr.addstr(y, 2 * x, 'x')
                        self.stdscr.attroff(curses.color_pair(2))  # Turn off red color
                    elif self.is_on_path(x, y):
                        if illuminate != 0:
                            hide_maze = False
                        if hide_maze:
                            if (x,y) == (player_x - 1,  player_y)\
                            or (x,y) == (player_x - 2,  player_y):
                                self.stdscr.addstr(y, 2 * x, '.') # Path behind
                                
                                if (x,y) in assets_xy_list:
                                    self.render_resources((x,y), r)
                                elif (x,y) in doors_xy_list:
                                    self.render_door_in_mze((x,y), d)

                            elif (x,y) == (player_x + 1,  player_y)\
                            or (x,y) == (player_x + 2,  player_y):

                                self.stdscr.addstr(y, 2 * x, '.') # Path infront
                                
                                if (x,y) in assets_xy_list:
                                    self.render_resources((x,y), r)
                                elif (x,y) in doors_xy_list:
                                    self.render_door_in_mze((x,y), d)

                            elif (x,y) == (player_x,  player_y + 1) \
                            or (x,y) == (player_x,  player_y + 2):
                                self.stdscr.addstr(y, 2 * x, '.') # Path above
                                
                                if (x,y) in assets_xy_list:
                                    self.render_resources((x,y), r)
                                elif (x,y) in doors_xy_list:
                                    self.render_door_in_mze((x,y), d)

                            elif (x,y) == (player_x,  player_y - 1)\
                            or (x,y) == (player_x,  player_y - 2):
                                self.stdscr.addstr(y, 2 * x, '.') # Path below

                                if (x,y) in assets_xy_list:
                                    self.render_resources((x,y), r)
                                elif (x,y) in doors_xy_list:
                                    self.render_door_in_mze((x,y), d)
                        else: 
                            if (x,y) in assets_xy_list:
                                self.render_resources((x,y), r)
                            elif (x,y) in doors_xy_list:
                                self.render_door_in_mze((x,y), d)
                            else:
                                self.stdscr.addstr(y, 2 * x, '.')
            
        
        game_play_baar = (
            f'\n| {str(pos)}'
            f' | R:{resource_pickups}'
        )
        strr =Counter(self.path)
        more_than_one = {item: strr[item] for item in strr if strr[item] > 1}
        self.stdscr.addstr(game_play_baar)
        self.stdscr.addstr(str(show_door))
        self.stdscr.addstr(f'\n{str(more_than_one)}')
        # self.stdscr.addstr(f'\n{str(assets_xy_list)}')

    def render_resources(self, crd, resources):
        i = self.assets_xy_list.index((crd[0],crd[1]))
        self.stdscr.attron(curses.color_pair(1))  # Turn on red color
        self.stdscr.addstr(crd[1], 2 * crd[0], resources[i])
        self.stdscr.attroff(curses.color_pair(1))  # Turn off red color

    def render_door_in_mze(self, crd, door):
        i = self.doors_xy_list.index((crd[0],crd[1]))
        self.stdscr.attron(curses.color_pair(1))  # Turn on red color
        self.stdscr.addstr(crd[1], 2 * crd[0], door[i])
        self.stdscr.attroff(curses.color_pair(1))  # Turn off red color


    def is_on_path(self, x, y):
        """Returns bool if player is on path"""
        return (x, y) in self.path
    

    def ASCIIDoor(self, door_name):
        door_property_str = "        MMMMMMMd|                          |bMMMMMMM"
        door = self.door_propertys[door_name]
        with open('render_door_graphic_ASCII.txt', 'r') as f:
            door_graphics = f.readlines()
        clean_door_graphics = [line.strip('\n') for line in door_graphics]

        ppy_line_index = [3, 4, 5, 6, 7, 8, 
                          12, 13, 14, 15, 16, 
                          17, 18, 19, 20]

        for i, property_index in enumerate(door):
            pct = door[property_index]['percentage']
            ppy = door[property_index]['property']

            start_property = 19 + (3 - len(str(pct)))
            start_str = door_property_str[:start_property]
            
            separator_str = "% : "

            end_property = len(start_str) + len(str(pct)) + len(ppy) + len(separator_str)
            end_str = door_property_str[end_property:]

            property_str = f"{start_str}{pct}{separator_str}{ppy}{end_str}"

            clean_door_graphics[ppy_line_index[i]] = property_str
        
        for i, line in enumerate(clean_door_graphics):
            time.sleep(0.05)
            self.stdscr.addstr(i, 0, line)
            self.stdscr.refresh()

        self.stdscr.addstr(str(door))