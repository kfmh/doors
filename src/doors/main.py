from rich import print as p
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from tqdm import tqdm
import time
import os
import json
import random

path = "./src/doors/mcq.json"
with open(path, 'r') as file:
    question = json.load(file)

correct_emoji = "🔑"
wrong_emoji = "❌"

a, b, c = "🅰", "🅱", "🅲"
question_mark = "❔"

console = Console()

def clar_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_table(m_a, answers, step):
    text = p(m_a['question'])

    table = Table(show_header=False)
    table.add_column(style="cyan")
    table.add_column(style="magenta")

    table.add_row(a, answers[0][0], answers[0][step])
    table.add_row(b, answers[1][0], answers[1][step])
    table.add_row(c, answers[2][0], answers[2][step])
    console.print(table, justify="center")
    if step == 3:
        time.sleep(0.1)
        p(f"\nExplanation:\n{m_a['explanation']}")


def main(m_a):
    clar_screen()
    answers = [[m_a['wrong_1'], question_mark, wrong_emoji], [m_a['wrong_2'], question_mark, wrong_emoji], [m_a['correct'], question_mark, correct_emoji]]
    random.shuffle(answers)

    render_table(m_a, answers, 1)
    print("")

    for i in tqdm(range(10), bar_format='{l_bar}|{bar}||Answer '):
    # for i in tqdm(range(10), bar_format='Answer in {remaining} | {bar}'):
        time.sleep(0.1)

    clar_screen()
    render_table(m_a, answers, 2)
