# ============================================================================
# cli_parser.py
# Argument parser library
# ============================================================================

import argparse

def get_parser():
    # Argument parser setup for command-line options
    parser = argparse.ArgumentParser(prog="Doors", 
                                    description="Ed-Tech Game",
                                    epilog="Prototype POC")

    # Argument for specifying the path to the chess engine
    parser.add_argument('-mcq', 
                        '--mcq_course', 
                        type=str, 
                        help='run mcq_courses.py to list available courses')

    parser.add_argument('-amcq', 
                        '--available_courses', 
                        type=bool,
                        help='run mcq_courses.py to list available courses')

    return parser 
