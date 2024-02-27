import curses 
class Game:
    """Main game loop"""
    def __init__(self,
                 stdscr,
                 hide_maze,
                 path,
                 assets_xy_list,
                 doors_xy_list,
                 doors_name_list = [],
                 size_x=4,
                 size_y=5,
                 illuminate_pickups = [],
                 resource_pickups = 0,
                 ):
        """Initialize variables for the game.

        Args:
            stdscr (object): Curses window object
            hide_maze (bool): Hides maze
            path (list): x,y coordinates of the path
            assets_xy_list (list): list of x,y coordinates of assets
            size_x (int, optional): Width of board. Defaults to 4.
            size_y (int, optional): _description_. Defaults to 5.
            resource_pickups (int, optional): Count of resource pickups
            . Defaults to 0.
            illuminate_pickups (list, optional): List of string charchters.
            . Defaults to [].
        """
        self.stdscr = stdscr
        self.board_size_x = size_x
        self.board_size_y = size_y
        self.player_x = 1
        self.player_y = 1
        self.path = path
        self.hide_maze = hide_maze
        self.resource_pickups = resource_pickups
        self.assets_xy_list = assets_xy_list
        self.doors_xy_list  = doors_xy_list
        self.doors_name_list = doors_name_list
        self.illuminate_pickups = illuminate_pickups
        self.illuminate = 0
        self.door_name = ""
        self.listen_for_trigger = False
        

    def is_within_bounds(self, x, y):
        """Returns bool if player is within bounds"""
        return 1 <= y < self.board_size_y - 1\
            and 1 <= x < self.board_size_x - 1
    
    def is_on_path(self, x, y):
        """Returns bool if player is on path"""
        return (x, y) in self.path
    
    def assets_handler(self):
        if (self.player_x, self.player_y) in self.assets_xy_list:
            x, y = self.player_x, self.player_y
            self.resource_pickups += 1

            i = self.assets_xy_list.index((x, y))
            self.illuminate_pickups.pop(i)
            self.assets_xy_list.remove((x,y))
            self.illuminate_maze(3)
    
    def doors_handler(self):
        if (self.player_x, self.player_y) in self.doors_xy_list:
            door_index = self.doors_xy_list.index((self.player_x, self.player_y))
            self.door_name = self.doors_name_list[door_index]
            self.listen_for_trigger = True
        elif (self.player_x, self.player_y) not in self.doors_xy_list:
            self.listen_for_trigger = False

    def handle_items(self):
        if self.illuminate != 0:
            self.illuminate -= 1
        self.assets_handler()
        self.doors_handler()


    def update_player_position(self, key):
        """Hanldes player input and position update"""
        new_x, new_y = self.player_x, self.player_y
        show_door = False
        if   key == curses.KEY_UP:    new_y -= 1
        elif key == curses.KEY_DOWN:  new_y += 1
        elif key == curses.KEY_LEFT:  new_x -= 1
        elif key == curses.KEY_RIGHT: new_x += 1

        elif key in [ord('\n'), ord('\r'), 10] and self.listen_for_trigger: 
            show_door = True
            self.listen_for_trigger = False

        elif key == curses.KEY_BACKSPACE: 
            self.listen_for_trigger = False
            show_door = False

        if self.is_within_bounds(new_x, new_y) \
        and self.is_on_path(new_x, new_y) \
        and new_x != 0 and new_y != 0:
            
            self.player_x, self.player_y = new_x, new_y
            self.handle_items()

        return show_door
    
    def illuminate_maze(self, steps):
        """Sets how many steps the maze should be visible

        Args:
            steps (int): How many steps the player can take before
            maze goes dark again.
        """
        self.illuminate = steps

    def run(self, render_method, assets_xy_list, doors_xy_list, doors_frames):
        """Starts the game loop

        Args:
            render_method (object): Method of rendering graphics
            assets_xy_list (list): list of (x, y) coordiantes for game assets 
        """
        curses.curs_set(0)
        show_door = False
        render_method.draw_board(
                        self.player_y,
                        self.player_x,
                        self.hide_maze,
                        self.resource_pickups,
                        self.illuminate_pickups,
                        doors_frames,
                        self.illuminate,
                        show_door,
                        self.door_name
                        )
        try:
            while True:
                key = self.stdscr.getch()
                show_door = self.update_player_position(key)
                render_method.draw_board(
                                        self.player_y,
                                        self.player_x,
                                        self.hide_maze,
                                        self.resource_pickups,
                                        self.illuminate_pickups,
                                        doors_frames,
                                        self.illuminate,
                                        show_door,
                                        self.door_name
                                        )


        except KeyboardInterrupt:
            print("Program interrupted by user. Cleaning up...")
