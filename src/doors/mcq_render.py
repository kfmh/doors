# -------------------------------------------------------------
from rich import print as p
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json
import time
import os
import random
from tqdm import tqdm
# MCQ emojies
correct_emoji = "🔑"
wrong_emoji = "❌"
a, b, c = "🅰", "🅱", "🅲"
question_mark = "❔"

# -------------------------------------------------------------
class MCQ:
    def __init__(self, mcq_json:str):
        """_summary_

        Args:
            mcq_json (str): _description_
        """
        with open(mcq_json, 'r') as file:
            self.courses = json.load(file)
        self.console = Console()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render_table(self, question, answers, step):
        p(question['question'])
        table = Table(show_header=False)
        table.add_column(style="cyan")
        table.add_column(style="magenta")

        table.add_row(a, answers[0][0], answers[0][step])
        table.add_row(b, answers[1][0], answers[1][step])
        table.add_row(c, answers[2][0], answers[2][step])
        self.console.print(table, justify="center")
        if step == 2:
            time.sleep(0.1)
            p(f"\nExplanation:\n{question['explanation']}\n")
    
# -------------------------------------------------------------
    def mcq_process(self, course):
        for q in list(self.courses[course]):
            self.clear_screen()
            answers = [[self.courses[course][q]['wrong_1'], question_mark, wrong_emoji], 
                    [self.courses[course][q]['wrong_2'], question_mark, wrong_emoji], 
                    [self.courses[course][q]['correct'], question_mark, correct_emoji]]
            random.shuffle(answers)

            self.render_table(self.courses[course][q], answers, 1)
            print("")

            for i in tqdm(range(100), bar_format='{l_bar}|{bar}||Answer '):
            # for i in tqdm(range(10), bar_format='Answer in {remaining} | {bar}'):
                time.sleep(0.1)

            self.clear_screen()
            self.render_table(self.courses[course][q], answers, 2)

            response = input("next question: ")
            if response.upper() == "N":
                break
            else: pass
         