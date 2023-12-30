from mcq_render import MCQ

mcq = MCQ("mcq.json")

def main():
    mcq.mcq_process('python_logic')

if __name__ == '__main__':
    main()