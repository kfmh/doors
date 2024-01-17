import curses


class RenderASCII:
    def __init__(self, 
                 stdscr,
                board_size_x, 
                board_size_y,
                path,
                assets_xy_list,
                ):
        self.assets_xy_list = assets_xy_list
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.stdscr = stdscr
        self.path = path
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    def draw_board(self, 
                   pos,
                   player_y,
                   player_x,
                   assets_xy_list,
                   hide_maze,
                   resource_pickups,
                   resources,
                   illuminate
                   ):
        
        self.stdscr.clear()
        r = resources
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

                        elif (x,y) == (player_x + 1,  player_y)\
                        or (x,y) == (player_x + 2,  player_y):

                            self.stdscr.addstr(y, 2 * x, '.') # Path infront
                            if (x,y) in assets_xy_list:
                                self.render_resources((x,y), r)
                        elif (x,y) == (player_x,  player_y + 1) \
                        or (x,y) == (player_x,  player_y + 2):
                            self.stdscr.addstr(y, 2 * x, '.') # Path above
                            if (x,y) in assets_xy_list:
                                self.render_resources((x,y), r)
                        elif (x,y) == (player_x,  player_y - 1)\
                        or (x,y) == (player_x,  player_y - 2):
                            self.stdscr.addstr(y, 2 * x, '.') # Path below
                            if (x,y) in assets_xy_list:
                                self.render_resources((x,y), r)
                    else: 
                        if (x,y) in assets_xy_list:
                            self.render_resources((x,y), r)
                        else:
                            self.stdscr.addstr(y, 2 * x, '.')
        
        game_play_baar = (
            f'\n| {str(pos)}'
            f' | R:{resource_pickups}'
        )
        self.stdscr.addstr(game_play_baar)
        # self.stdscr.addstr(f'\n{str(path)}')
        # self.stdscr.addstr(f'\n{str(assets_xy_list)}')

    def render_resources(self, crd, resources):
        i = self.assets_xy_list.index((crd[0],crd[1]))
        self.stdscr.attron(curses.color_pair(1))  # Turn on red color
        self.stdscr.addstr(crd[1], 2 * crd[0], resources[i])
        self.stdscr.attroff(curses.color_pair(1))  # Turn off red color


    def is_on_path(self, x, y):
        """Returns bool if player is on path"""
        return (x, y) in self.path