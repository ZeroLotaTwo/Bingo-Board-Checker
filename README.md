# Bingo Board Checker

A very barebones Python/Pygame application for checking a Bingo board. The program allows you to enter your Bingo card, mark called numbers, and check how many Bingo combinations you currently have.

## Requirements

* Python 3
* Pygame

## Installation

### 1. Make a directory then clone the repository

First make a directory you want to put the files inside. You can name it whatever you want.
Then you can download a zip of the files and move it into the directory then you can proceed to step 2.

If you are using the terminal in linux
Open a terminal and run:

Note: replace [name] with whatever name you want
'''bash
mkdir [name]
cd [name]
git clone https://github.com/ZeroLotaTwo/Bingo-Board-Checker.git
'''

### 2. Install Pygame

Install Pygame using pip:

```bash
pip install pygame
```

If `pip` is not recognized, try:

```bash
python -m pip install pygame
```

## Running the Program

The main file is `bingoMain.py`.

Run it with:

```bash
python bingoMain.py
```

On some systems, you may need to use:

```bash
python3 bingoMain.py
```

A Pygame window should open with the Bingo board.

## How to Use

### Entering Your Bingo Board

When the program starts, your Bingo board is displayed.

To enter a new board:

1. Enter `999`.
2. Press **Enter**.
3. The program will ask you to enter your Bingo numbers from left to right starting at the top left corner.
4. Enter all 25 numbers separated by spaces.
5. Press **Enter**.

For example:

```text
1 2 3 4 5 6 7 8 9 10 11 12 0 13 14 15 16 17 18 19 20 21 22 23 24
```

The `0` represents the free space in the center of the board.

### Marking Numbers

Type a called Bingo number and press **Enter**.

For example:

```text
42
```

The program will mark that number on the board.

Free Space will already be marked on the board and again is represented with a 0.

### Bingo Detection

The program automatically checks the board for winning combinations after numbers are marked.

When a Bingo is detected, the number of Bingos found will be displayed.

### After Getting a Bingo

When the program detects a Bingo, you have two options:

* Enter `0` to keep playing and ignore the current Bingo.
* Enter `1` to clear the board and start over.

## Project Files

```text
Bingo-Board-Checker/
│
├── bingoMain.py          # Main program and Pygame interface
├── BingoBoardClass.py    # Bingo board and number-marking logic
├── BingoBoardWin.py      # Bingo/winning-condition detection
└── bingoNumCaller.py     # Bingo number caller
```

## Project Structure

`bingoMain.py` is the entry point for the program. It creates the Bingo board, initializes the number caller, handles user input, displays the board using Pygame, and checks for winning combinations.

The other Python files contain the supporting classes used by the main program.

## Troubleshooting

### Pygame is not installed

If you receive an error such as:

```text
ModuleNotFoundError: No module named 'pygame'
```

Install Pygame with:

```bash
python -m pip install pygame
```

### Python is not recognized

Make sure Python is installed and added to your system's PATH.

You can check your Python installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

## Repository

[GitHub Repository](https://github.com/ZeroLotaTwo/Bingo-Board-Checker)
