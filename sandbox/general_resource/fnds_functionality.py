import time
from collections import deque
import os

# Average Time To Answer 
class Avg_TTA:
    def __init__(self):
        self.start_time = None
        self.last_five = deque(maxlen=5)  # Will store the last 5 times.

    def start(self):
        """Starts the timer."""
        self.start_time = time.time()

    def stop(self):
        """Stops the timer and returns the elapsed time in seconds."""
        if self.start_time is None:
            raise ValueError("Timer hasn't started yet!")
        elapsed_time = time.time() - self.start_time
        self.last_five.append(elapsed_time)  # Add the time taken to the deque.
        self.start_time = None  # reset for the next start
        return elapsed_time

    def average_time(self):
        """Returns the average of the last 5 times."""
        return sum(self.last_five) / len(self.last_five)

    def log_time(self, console):
        """Logs the elapsed time and average time over last 5 answers after stopping the timer."""
        elapsed_time = self.stop()
        avg_time = self.average_time()
        console.print(f"\n[bold blue]Time taken to answer: {elapsed_time:.2f} seconds.[/bold blue]")
        console.print(f"[bold blue]Average time over last 5 answers: {avg_time:.2f} seconds.[/bold blue]\n")

# Answer tracking
class AnswerTracker:
    def __init__(self):
        self.correct_count = 0
        self.wrong_count = 0

    def add_correct(self):
        """Increments the count of correct answers by 1."""
        self.correct_count += 1

    def add_wrong(self):
        """Increments the count of wrong answers by 1."""
        self.wrong_count += 1

    def fraction_wrong_over_correct(self):
        """Returns the fraction of wrong answers divided by correct answers.
        If there are no correct answers, return None.
        """
        if self.correct_count == 0:
            return None
        return self.wrong_count / (self.correct_count + self.wrong_count)


class ScreenManager:
    def __init__(self):
        pass

    @staticmethod
    def clear_screen():
        """Clears the terminal screen."""
        # Check if OS is POSIX compliant (e.g., Linux, macOS)
        if os.name == 'posix':
            print("\033c", end="")  # ANSI escape sequence to clear screen
        else:
            os.system('cls')  # Windows command to clear screen