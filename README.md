# 2048-Game-Implementation
A simple and elegant implementation of the classic 2048 puzzle game built using Python’s Tkinter library for GUI.
Use your arrow keys to slide tiles — merge them to reach the 2048 tile!

# 📦 Installation
Prerequisites

Make sure you have Python 3.7+ installed.
You can check your version using:

python --version

Step 1: Clone or Download the Repository

If you have Git:

git clone https://github.com/sh1ma2/2048-Game-Implementation.git
cd 2048-tkinter


Or simply download the .zip file and extract it.

Step 2: Install Dependencies

The game only requires the built-in tkinter and random libraries — no external installations needed.
If Tkinter is not available, install it manually:

For Windows:

pip install tk


For Ubuntu/Debian:

sudo apt-get install python3-tk

# ▶️ Running the Game

Once installed, run the game with:

python game_2048.py


The game window will open automatically.

# 🎮 How to Play

Goal: Combine tiles with the same number to create the tile 2048.

Controls:

⬆️ Up Arrow – Move tiles up

⬇️ Down Arrow – Move tiles down

⬅️ Left Arrow – Move tiles left

➡️ Right Arrow – Move tiles right

Each move adds a new 2 or 4 tile to a random empty space.

When no more moves are possible (no empty cells and no adjacent equal tiles), the game ends.

Use the Restart button anytime to start a new game.

# 🧠 Implementation Details
💡 Structure

Class: Game2048 — Handles both the GUI and game logic.

Main Components:

Board Initialization: Creates a 4x4 matrix with two random tiles (2 or 4) at the start.

Movement Logic:

move_left, move_right, move_up, move_down
handle tile movement and merging logic.

Tile Management:

compress() – Moves all non-zero tiles to the left.

merge() – Merges adjacent equal tiles and updates the score.

Utility Functions:

transpose() – For column-wise moves.

reverse() – Used for right/down movements.

GUI Update:

update_gui() – Refreshes tile colors, text, and score dynamically.

Game State:

check_game_over() – Detects win/loss conditions.

game_over() – Displays popup when the game ends.
