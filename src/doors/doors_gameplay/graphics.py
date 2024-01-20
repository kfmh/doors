import curses
import time
from collections import Counter
import operator

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
        self.stdscr = stdscr
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.path = path
        self.assets_xy_list = assets_xy_list
        self.doors_xy_list = doors_xy_list
        self.door_propertys = door_propertys

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
                   assets_graphic,
                   doors_graphic,
                   illuminate,
                   show_door,
                   door_name
                   ):
        
        self.stdscr.clear()
        a = assets_graphic
        d = doors_graphic
        resource_list = [(self.assets_xy_list, a), (self.doors_xy_list, d)]
        vpr_list = [['.', operator.sub, 'horizontal'], 
                    ['.', operator.add, 'horizontal'], 
                    ['.', operator.sub, 'vertical'], 
                    ['.', operator.add, 'vertical']] 
        
        if show_door:
            self.ASCIIDoor(door_name, )
        else:
            for y in range(self.board_size_y):
                for x in range(self.board_size_x):

                    if y == 0 or y == self.board_size_y - 1 \
                    or x == 0 or x == self.board_size_x - 1:
                        self.stdscr.addstr(y, 2 * x, '#')

                    elif y == player_y and x == player_x:
                        self.curses_color_print((x, y), 2, 'x')

                    elif self.is_on_path(x, y):
                        if illuminate != 0:
                            hide_maze = False

                        if hide_maze:
                            
                            for i in vpr_list: # Visible_Path_Radius_list
                                self.visible_path_radius(x, y,
                                                        player_x, player_y,
                                                        visual_str=i[0],
                                                        op=i[1], direction=i[2],
                                                        resource_list=resource_list,
                                                        hide_maze=hide_maze
                                                        )
                                
                        else: 
                            self.render_object((x,y), resource_list, hide_maze)
                    
            self.game_play_baar((player_x, player_y))
                

    def visible_path_radius(self, 
                            x, y, 
                            player_x, player_y,
                            visual_str, op, direction, 
                            resource_list, hide_maze):
        """_summary_

        Args:
            visual_str (str): ASCI visual string
            x (int): redner visual at position x
            y (int): redner visual at position y
            player_x (int): palyer x coordiante
            player_y (int): player y coordinate

        """
        if direction == 'horizontal':
            if  (x,y) == (op(player_x, 1),  player_y) or \
                (x,y) == (op(player_x, 2),  player_y):
                self.stdscr.addstr(y, 2 * x, visual_str) 
                self.render_object((x, y), resource_list, hide_maze)
                
        else:
            if  (x,y) == (player_x,  op(player_y, 1)) or \
                (x,y) == (player_x,  op(player_y, 2)):
                self.stdscr.addstr(y, 2 * x, visual_str) 
                self.render_object((x, y), resource_list, hide_maze)

            

    def game_play_baar(self, pos):
        game_play_baar_str = (
            f'\n| {str(pos)}'
            # f' | R:{resource_pickups}'
        )
        self.stdscr.addstr(game_play_baar_str)
        # strr =Counter(self.path)
        # more_than_one = {item: strr[item] for item in strr if strr[item] > 1}
        # self.stdscr.addstr(f'\n{str(more_than_one)}')

    def render_object(self, coordiantes, resource_list, hide_maze):
        if not hide_maze:
            self.curses_color_print(coordiantes=coordiantes, 
                                    color=2, 
                                    graphic='.')
            
        for resources in resource_list:
            if coordiantes in resources[0]:
                i = resources[0].index(coordiantes)
                r = resources[1][i]     
                self.curses_color_print(coordiantes=coordiantes, 
                                        color=1, 
                                        graphic=r)

    def curses_color_print(self, coordiantes, color, graphic):
        self.stdscr.attron(curses.color_pair(color)) 
        self.stdscr.addstr(coordiantes[1], 2 * coordiantes[0], graphic)
        self.stdscr.attroff(curses.color_pair(color)) 


    def is_on_path(self, x, y):
        """Returns bool if player is on path"""
        return (x, y) in self.path
    

    def ASCIIDoor(self, door_name):
        door_property_str = "        Md|                          |bM"
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

            start_property = 12 + (3 - len(str(pct)))
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

        # self.stdscr.addstr(str(door))