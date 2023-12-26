from tqdm import tqdm
from rich import print as p
from rich.table import Table
from rich.console import Console
import time
import os

multi_answer = {
    "question": "What is the output of the expression : 3*1**3",
    "answer_1": ["🅰", "27", "❔", "❌"],
    "answer_2": ["🅱", "9", "❔", "❌"],
    "answer_3": ["🅲", "3", "❔", "🔑"],
    "explanation": "Precedence of ** is higher than that of 3, thus first 1**3 will be executed and the result will be multiplied by 3."
}

console = Console()

def clar_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_table(m_a, step):
    p(f"{m_a['question']}\n")
    table = Table(show_header=False)
    table.add_column(style="cyan")
    table.add_column(style="magenta")
    table.add_row(m_a['answer_1'][0], m_a['answer_1'][1], m_a['answer_1'][step])
    table.add_row(m_a['answer_2'][0], m_a['answer_2'][1], m_a['answer_2'][step])
    table.add_row(m_a['answer_3'][0], m_a['answer_3'][1], m_a['answer_3'][step])
    console.print(table, justify="center")
    if step == 3:
        p(f"\nExplanation:\n{m_a['explanation']}")


def main(m_a):
    clar_screen()

    render_table(m_a, 2)
    print("")
    for i in tqdm(range(100), bar_format='{l_bar}{bar}') :
        time.sleep(0.1)
    clar_screen()
    render_table(m_a, 3)

if __name__ == '__main__':
    main(multi_answer)