# Artificial Intelligence Fundamentals Practical Assignment #1
## Run the Assignment
A Python 3.10 interpreter with Tkinter support is required.
To run, use the command python3 main.py in the project directory.

Below are the given conditions.
### Additional Software Requirements
At the beginning of the game, the human player specifies the length of the number sequence to be used in the game, which can range from 15 to 20 numbers. The game software randomly generates a number sequence of the specified length, including the numbers 1, 2, 3, and 4.

### Game Description
At the beginning of the game, the generated number sequence is given. Each player starts with 0 points. Players take turns executing their moves. During a turn, a player can:
* take any number from the sequence and add it to their score;
* split a "2" into two "1"s, but not gain any points for it;
* split a "4" into two "2"s and gain 1 point for it.
The game ends when the sequence is empty. The player with the most points wins. If the point totals are equal, the result is a draw.
