import tkinter as tk
import main


def start_game():
    player1_mode = player1_mode_var.get()
    player2_mode = player2_mode_var.get()
    number_count = number_count_var.get()
    print("Player 1:", player1_mode)
    print("Player 2:", player2_mode)
    print("Number count:", number_count)
    main.main(player1_mode, player2_mode, number_count)
    root.destroy()


root = tk.Tk()
root.title("Game settings")
root.configure(bg="#222831")

# Player 1 mode selection
player1_frame = tk.Frame(root, bg="#222831")
player1_frame.grid(row=0, column=0, padx=10, pady=10)
tk.Label(player1_frame, text="Player 1", bg="#222831", fg="#eeeeee").pack()
player1_mode_var = tk.StringVar()
player1_mode_var.set("Player")  # Default selection
tk.Radiobutton(player1_frame,
               text="Player",
               variable=player1_mode_var,
               value="Player",
               bg="#222831",
               fg="#00adb5").pack(anchor=tk.W)
tk.Radiobutton(player1_frame,
               text="MinMax",
               variable=player1_mode_var,
               value="MinMax",
               bg="#222831",
               fg="#00adb5").pack(anchor=tk.W)
tk.Radiobutton(player1_frame,
               text="AlphaBeta",
               variable=player1_mode_var,
               value="AlphaBeta",
               bg="#222831",
               fg="#00adb5").pack(anchor=tk.W)

# Player 2 mode selection
player2_frame = tk.Frame(root, bg="#222831")
player2_frame.grid(row=0, column=1, padx=10, pady=10)
tk.Label(player2_frame, text="Player 2", bg="#222831", fg="#eeeeee").pack()
player2_mode_var = tk.StringVar()
player2_mode_var.set("Player")  # Default selection
tk.Radiobutton(player2_frame,
               text="Player",
               variable=player2_mode_var,
               value="Player",
               bg="#222831",
               fg="#00adb5").pack(anchor=tk.W)
tk.Radiobutton(player2_frame,
               text="MinMax",
               variable=player2_mode_var,
               value="MinMax",
               bg="#222831",
               fg="#00adb5").pack(anchor=tk.W)
tk.Radiobutton(player2_frame,
               text="AlphaBeta",
               variable=player2_mode_var,
               value="AlphaBeta",
               bg="#222831",
               fg="#00adb5").pack(anchor=tk.W)

# Number count selection
number_count_frame = tk.Frame(root, bg="#222831")
number_count_frame.grid(row=1, columnspan=2, padx=10, pady=10)
tk.Label(number_count_frame,
         text="Choose number count for the game",
         bg="#222831",
         fg="#eeeeee").pack()
number_count_var = tk.IntVar()
number_count_var.set(15)  # Default selection
for i in range(15, 21):
    tk.Radiobutton(number_count_frame,
                   text=str(i),
                   variable=number_count_var,
                   value=i,
                   bg="#222831",
                   fg="#00adb5").pack(side=tk.LEFT)

# Start button
start_button = tk.Button(
    root,
    text="Play",
    command=start_game,
    bg="#00adb5",
    fg="#eeeeee",
)
start_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()

