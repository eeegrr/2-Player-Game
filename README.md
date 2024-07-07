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

### Game Classes and Structure

#### 'Turn' Class
Represents a player's action: taking a number or splitting it.
Attributes:

mode: Boolean indicating the action (True for take, False for split).
number: The number to act upon.
index: The index of the number in the sequence (optional).
'Game' Class
Handles the game state, including the sequence, player points, and turn logic.
Methods:

available_turns: Returns possible actions for the current player.
do_turn: Executes a turn and updates the game state.
copy: Creates a copy of the current game state.
'GameNode' Class
Used by AI to represent game states and potential future states.
Constructs a tree of possible game states up to a specified depth.
Methods:

do_estimate: Evaluates the game state for AI decision-making.
#### 'Player' Abstract Class
Represents a player in the game, requiring the implementation of the choose_turn method.

'MinMax' and 'AlphaBeta' Classes
Inherit from Player and implement AI decision-making using respective algorithms.

###User Interface

#### 'GameGUI' Class
Uses Tkinter for the graphical user interface.
Displays game information, sequence, and actions available to the player.
Methods:

create_widgets: Sets up the UI components.
update_ui: Refreshes the display with the current game state.
choose_mode: Allows the player to choose between taking or splitting a number.
turn: Executes the chosen turn and updates the game state.
'main.py'
Entry point for the game.
Initializes the main window and the game GUI.
Provides options to start the game with different player modes (human or AI) and sequence lengths.

'startWindow.py'
Provides a start window for selecting game settings, such as player modes and sequence length.
On clicking "Play", the selected settings are used to start the game in main.py.

How It Works

Starting the Game: Run the game using 'python3 main.py'. The start window will appear, allowing players to select modes and sequence length.
Playing the Game: The main game window displays the sequence and available actions. Players take turns making moves until the sequence is empty.
AI Decision Making: If playing against AI, the AI calculates the best move using MinMax or AlphaBeta algorithm and makes its move when prompted.
End of Game: The game ends when all numbers are taken or split. The player with the most points wins, or it's a draw if points are equal.
