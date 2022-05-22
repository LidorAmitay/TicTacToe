# Tic-Tac-Toe Project 
This project is the classic Tic-Tac-Toe game!

## Description
### About the game
Tic-Tac-Toe rules:
1. The game is played on a grid that's 3 cells by 3 cells.

2. You are X, the AI (computer) is O. Player and AI take turns putting their marks in empty cells.

3. The first one to get 3 of his marks in a row (horizontally, vertically or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
### About the project
This project built with Python, in OOP paradigm. 
The project have 3 main objects: **State**, **AI** and **Game**  
**State** object represent a state of the game (board, turn, and how many rounds played)  
**AI** object represent the computer player, which uses the minimax algorithm to determine his next move.  
After making a move the AI object updates the Game object state.  
**Game** object responsibility is to manage the flow of the game. Game object save and update the current state and turn of the game.


## Installation
We only need python3 installed.
To check if you already have python3 installed, run on terminal:  
`python --version`  
If no, download the suitable version for your machine from [here](https://www.python.org/downloads/), and run the installer.  
Then, run again on terminal: `python --version`, and it should show you the version you just installed.


## Usage
To start a game, open terminal in the project's folder and run:  
`python main.py`
You can shut it down by pressing `ctrl+c` on Windows or `command+.` on Mac 
### How to play
When you run the program, at first it will print short instructions.  
Afterwards, the board will be printed, and the game will start.  
Each turn, you will be asked to choose a number in range (0-8)
Each number represented cell from the game board:  

              0 |  1 | 2  
             ------------
              3 |  4 | 5  
             ------------
              6 |  7 | 8   

Choose your best move, until the game end
