
from tkinter import *
# 2 dimensions list with data
numbers = [
 [2, 4, 8, 16],
 [32, 64, 128, 256],
 [512, 1024, 2048, 0],
 [0, 0, 0, 0],
]
# 2 dimensions list (empty, with labels in the future)
labels = [
[None, None, None, None],
[None, None, None, None],
[None, None, None, None],
[None, None, None, None],
]

colours = {
    0: "#FFFFFF",
    2: "#DBDBDB",
    4: "#B3B3B3",
    8: "#8C8C8C",
    16: "#6B6B6B",
    32: "#FFB3B3",
    64: "#FE8181",
    128: "#FF6052",
    256: "#FF1A1A",
    512: "#FDFEA9",
    1024: "#FEEF81",
    2048: "#FEEF4D",
}

x0 = 200 # horizontal beginning of labels
y0 = 100 # vertical beginning of labels
width = 150 # horizontal distance between labels
height = 150 # vertical distance between labels
# Windows creation
win = Tk()
win.geometry("1000x1000")
win.title(" exemple labels positionnés par .place")
# Title
Label(text="2048", width=10, height=1, font=("Arial", 60)).place(x=50, y=8)
# labels creation and position (1. Creation 2. position)
for line in range(len(numbers)):
    for col in range(len(numbers[line])):
        #creation without placement
        labels[line][col] = Label(win, text=numbers[line][col] or "", width=10, height=5, borderwidth=1, relief="solid", font=("Arial", 15), bg=colours.get(numbers[line][col], "#74E2AE"))
        # label positionning in the windows
        labels[line][col].place(x=x0 + width * col, y=y0 + height * line)

def display_game():#Chat gpt je lui est demandé trouve moi le code
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            # Met à jour le texte et la couleur de fond du label en fonction de la valeur dans `numbers`
            labels[line][col].config(
                text=numbers[line][col],
                bg=colours.get(numbers[line][col], "#74E2AE")
            )

win.mainloop()


