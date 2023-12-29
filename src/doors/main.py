from tqdm import tqdm
from rich import print as p
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time
import os
import json

multi_answer = {
    "question": "\n# What is the output of the Python expression:\n\n>>>print(3*1**3)\n",
    "answer_1": ["🅰", "27", "❔", "❌"],
    "answer_2": ["🅱", "9", "❔", "❌"],
    "answer_3": ["🅲", "3", "❔", "🔑"],
    "explanation": "Exponents (1**3) have higher precedence than multiplication (3*1)"
}

correct_emoji = "🔑"
wrong_emoji = "❌"

a, b, c = "🅰", "🅱", "🅲"
question_mark = "❔"

path = "./mcq.json"
with open(path, 'r') as file:
    question = json.load(file)

console = Console()

def clar_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def render_table(m_a, step):
    text = p(m_a['question'])

    table = Table(show_header=False)
    table.add_column(style="cyan")
    table.add_column(style="magenta")
    table.add_row(m_a['answer_1'][0], m_a['answer_1'][1], m_a['answer_1'][step])
    table.add_row(m_a['answer_2'][0], m_a['answer_2'][1], m_a['answer_2'][step])
    table.add_row(m_a['answer_3'][0], m_a['answer_3'][1], m_a['answer_3'][step])
    console.print(table, justify="center")
    if step == 3:
        time.sleep(0.1)
        p(f"\nExplanation:\n{m_a['explanation']}")


def main(m_a):
    clar_screen()

    render_table(m_a, 2)
    print("")

    for i in tqdm(range(100), bar_format='{l_bar}|{bar}||Answer '):
    # for i in tqdm(range(10), bar_format='Answer in {remaining} | {bar}'):
        time.sleep(0.1)

    clar_screen()
    render_table(m_a, 3)

if __name__ == '__main__':
    main(multi_answer)