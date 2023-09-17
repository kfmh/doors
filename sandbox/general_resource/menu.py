
class Game_menu:
    def __init__(self):
        pass

    def select_game(console, panel):
        """
        Displays the introduction message.
        
        Args:
            console (Console): Rich Console instance for printing formatted output.
        """
        console.print(panel("[bold cyan]Welcome to the Addition Quiz![/bold cyan]"))
        console.print("Type [bold red]1 = Addision[/bold red]")
        console.print("Type [bold red]2 = Play Doors[/bold red]")
        console.print("Type [bold red]q[/bold red] anytime to quit.")
        game_choice = input("> ")
        return game_choice