import random
from general_resource.fnds_functionality import Avg_TTA, AnswerTracker  # Importing the necessary modules and classes

class Addision_game:
    """
    Class for updating random integers a and b for addition questions.
    """
    def __init__(self):
        """
        Initializes the RandomABIntUpdater instance.
        """
        self.a = 0
        self.b = 0
        self.a_new = 0
        self.b_new = 0
    
    def update(self):
        """
        Updates the random integers a and b while ensuring they are not the same as before.
        
        Returns:
            tuple: A tuple containing the sum of the updated integers, the updated a, and the updated b.
        """
        while self.a_new == self.a and self.b_new == self.b:
            self.a_new = random.randint(1, 9)
            self.b_new = random.randint(1, 9)
            sum_result = self.a_new + self.b_new
        
        self.a, self.b = self.a_new, self.b_new
        
        return sum_result, self.a, self.b

    def display_question(self, console, score, a, b):
        """
        Displays the question to the user.
        
        Args:
            console (Console): Rich Console instance for printing formatted output.
            score (int): Current score of the user.
            a (int): First integer of the addition.
            b (int): Second integer of the addition.
        """
        console.print(f"Score: [bold magenta]{score}[/bold magenta]\n")
        console.print(f"What is the sum of\n\n[bold cyan]{a} + {b} = ?[/bold cyan]")
        console.print("\nType [bold red]q[/bold red] to quit.")
    
    def game_loop(self, score, Panel, clear_screen, console):
        response = "run"
        timer = Avg_TTA()
        tracker = AnswerTracker()
        while response != "q":
            clear_screen()
            correct, a, b = self.update()

            self.display_question(console, score, a, b)
            timer.start()

            response = input("> ")

            if response == "q":
                clear_screen()
                console.print(Panel(f"Your final score is [bold green]{score}[/bold green]", expand=False))
                break

            try:
                user_response = int(response)
                if user_response == correct:
                    score += 1
                    tracker.add_correct()
                    console.print("[bold green]Correct! Well done![/bold green]\n")
                    timer.log_time(console)
                else:
                    tracker.add_wrong()
                    console.print(f"[bold red]Oops! That's incorrect. \n{a} + {b} = {correct}[/bold red]\n")
                
            except ValueError:
                console.print("[bold yellow]Invalid input. Please enter a number or 'q' to quit.[/bold yellow]\n")

            fraction = tracker.fraction_wrong_over_correct()
            if fraction is not None:
                print(f"Fraction of wrong answers over total answers: {fraction:.2f}")
            else:
                print("No correct answers recorded yet.")
            print(input("Press enter"))