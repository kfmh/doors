# ============================================================================
# main.py
# 
# ============================================================================

from .mcq_courses import MCQ
from .cli_parser import get_parser

def main():
    mcq = MCQ()
    parser = get_parser()
    args = parser.parse_args()

    try:
        if args.available_courses:
            mcq.available_courses()
        else:
            mcq.mcq_process(args.mcq_course)
    except KeyboardInterrupt:
        print("Program interrupted by user. Cleaning up...")



if __name__ == '__main__':
    main()
