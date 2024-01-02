[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<h1 align="center">Doors</h1>
Education is a societal investment from which everyone benefits, and it's never too late to start. The challenge increases with age, but it's surmountable. Time and money often appear as barriers to change, but imagine if they weren't. Consider a scenario where learning immediately translates into tangible monetary value, without exceptions, for as long as desired. This vision is rooted at the crossroads of educational technology, artificial intelligence, gaming, marketing, and blockchain. Our mission is straightforward: we don't aim to change anything; we simply want you to demonstrate the intelligence you inherently possess.

#### Version
doors 0.1.0-alpha <br>
The alpha version serves as an initial prototype designed for feature testing.

### Follow the journey on: 
[Logbook](https://kfmh.github.io/) 

<!--
<p align="center">
    <br>
    <img src="" width="500px"/>
    <br>
    Chessboard coordinates difficulty
    <img src="" width="80%"/>
    <br>
<p>
-->

## Installation
1. From terminal create a directory
```bash
mkdir <directory_name>
cd <directory_name>
``` 
2. Create and activate an environment
```bash
# Python environment
python3 -m venv <enviroment_neme>
source <enviroment_neme>/bin/activate
```
```bash
# Anaconda environment
conda create -n <enviroment_neme>
conda activate <enviroment_neme>
```
3. Install uw_chess package
```bash
pip install git+https://github.com/kfmh/doors.git
```

## Usage
 Command line parsing.
| Long Flag | Short Flag | Default | Description |
|----------|----------|----------|----------|
| --available_courses | -amcq | None | List all available courses |
| --mcq_course        | -mcq  | None | Choose course |

Available Courses
| Course Name | Description |
|----------|----------|
| python_logic | Multiple choice question about python logic |
| python_math  | Multiple choice question about python math operations |

Start program
```bash
# Run program
# Example: doors -mcq python_logic
doors -mcq <course_name>
```

Quit program: ctrl + c

<!--
## Documentation
-->


