import tkinter as tk
import random

class Game2048:
    def __init__(self, size=4):
        self.size = size
        self.score = 0
        self.board = [[0] * size for _ in range(size)]

        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.window.configure(bg="#faf8ef")

        # Center window and fix spacing
        self.window.geometry("420x520")
        self.window.resizable(False, False)

        self.bg_color = "#bbada0"
        self.colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8",
            8: "#f2b179", 16: "#f59563", 32: "#f67c5f",
            64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
            512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }

        self.grid_cells = []
        self.init_gui()
        self.start_game()

        self.window.bind("<Key>", self.key_press)
        self.window.mainloop()

    # ---------- GUI ----------
    def init_gui(self):
        title = tk.Label(
            self.window, text="2048", font=("Verdana", 30, "bold"), bg="#faf8ef", fg="#776e65"
        )
        title.pack(pady=(10, 0))

        score_frame = tk.Frame(self.window, bg="#bbada0")
        score_frame.pack(pady=(10, 5))
        self.score_label = tk.Label(
            score_frame, text=f"Score: {self.score}", font=("Arial", 16, "bold"), bg="#bbada0", fg="white"
        )
        self.score_label.pack(padx=10, pady=5)

        restart_btn = tk.Button(
            self.window, text="Restart", command=self.restart_game,
            font=("Arial", 14, "bold"), bg="#8f7a66", fg="white", relief="raised"
        )
        restart_btn.pack(pady=(5, 10))

        # Grid Frame
        grid_frame = tk.Frame(self.window, bg=self.bg_color)
        grid_frame.pack(padx=20, pady=10)

        for i in range(self.size):
            row = []
            for j in range(self.size):
                cell = tk.Frame(grid_frame, bg=self.colors[0], width=90, height=90)
                cell.grid(row=i, column=j, padx=5, pady=5)
                label = tk.Label(cell, text="", bg=self.colors[0],
                                 justify=tk.CENTER, font=("Arial", 24, "bold"))
                label.pack(expand=True, fill=tk.BOTH)
                row.append(label)
            self.grid_cells.append(row)

    # ---------- Game Logic ----------
    def start_game(self):
        self.add_new_tile()
        self.add_new_tile()
        self.update_gui()

    def restart_game(self):
        self.score = 0
        self.board = [[0] * self.size for _ in range(self.size)]
        self.start_game()

    def add_new_tile(self):
        empty = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if empty:
            i, j = random.choice(empty)
            self.board[i][j] = random.choice([2, 4])

    def update_gui(self):
        for i in range(self.size):
            for j in range(self.size):
                val = self.board[i][j]
                color = self.colors.get(val, "#3c3a32")
                self.grid_cells[i][j].configure(text=str(val) if val else "", bg=color)
        self.score_label.config(text=f"Score: {self.score}")
        self.window.update_idletasks()

    def key_press(self, event):
        key = event.keysym
        moved = False
        if key == "Up":
            moved = self.move_up()
        elif key == "Down":
            moved = self.move_down()
        elif key == "Left":
            moved = self.move_left()
        elif key == "Right":
            moved = self.move_right()

        if moved:
            self.add_new_tile()
            self.update_gui()
            if self.check_game_over():
                self.game_over()

    # ---------- Movement & Merging ----------
    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(self.size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                self.score += row[i]
                row[i + 1] = 0
        return self.compress(row)

    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def reverse(self):
        self.board = [row[::-1] for row in self.board]

    def move_left(self):
        moved = False
        new_board = []
        for row in self.board:
            merged_row = self.merge(self.compress(row))
            if merged_row != row:
                moved = True
            new_board.append(merged_row)
        self.board = new_board
        return moved

    def move_right(self):
        self.reverse()
        moved = self.move_left()
        self.reverse()
        return moved

    def move_up(self):
        self.transpose()
        moved = self.move_left()
        self.transpose()
        return moved

    def move_down(self):
        self.transpose()
        moved = self.move_right()
        self.transpose()
        return moved

    # ---------- Game End ----------
    def check_game_over(self):
        if any(2048 in row for row in self.board):
            return True
        if any(0 in row for row in self.board):
            return False
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    return False
                if self.board[j][i] == self.board[j + 1][i]:
                    return False
        return True

    def game_over(self):
        popup = tk.Toplevel(self.window)
        popup.title("Game Over")
        popup.configure(bg="#faf8ef")
        tk.Label(popup, text="Game Over!", font=("Arial", 20, "bold"), bg="#faf8ef", fg="#776e65").pack(padx=10, pady=10)
        tk.Button(popup, text="Restart", command=lambda: [popup.destroy(), self.restart_game()],
                  font=("Arial", 14), bg="#8f7a66", fg="white").pack(pady=5)
        tk.Button(popup, text="Exit", command=self.window.destroy, font=("Arial", 14),
                  bg="#8f7a66", fg="white").pack(pady=5)


if __name__ == "__main__":
    Game2048()
