
from tkinter import *
from tkinter import messagebox
import random
# 2 dimensions list with data

def pack4(a, b, c, d):
    moves = 0

    if c==0 and d != 0:
        c = d
        d = 0
        moves = moves+1

    if b==0 and c != 0:
        b=c
        c=d
        d=0
        moves = moves + 1

    if a==0 and b != 0:
        a=b
        b=c
        c=d
        d=0
        moves = moves + 1

    if a == b and a != 0:
        a = 2 * a
        b = c
        c = d
        d = 0
        moves = moves + 1

    if b == c and b != 0:
        b = 2 * b
        c = d
        d = 0
        moves = moves + 1

    if c==d and c != 0:
        c=2*c
        d=0
        moves = moves + 1



    return a, b, c, d, moves

print(pack4(0, 4, 8, 0))
'''
numbers = [
 [2, 4, 8, 16],
 [32, 64, 128, 256],
 [512, 1024, 2048, 0],
 [0, 0, 0, 0],
]
'''



numbers = [
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
]
positions = random.sample([(x, y) for x in range(len(numbers)) for y in range(len(numbers))], 2) # Affichage aléatoire sur la grille (avec ChatGPT)
for x, y in positions: numbers[x][y] = 2 # Placer un 2 sur la grille

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
    16: "#FECDCD",
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
        labels[line][col] = Label(win, text=numbers[line][col] or "", width=10, height=5, borderwidth=1, relief="solid", font=("Arial", 18), bg=colours.get(numbers[line][col], "#74E2AE"))
        # label positionning in the windows
        labels[line][col].place(x=x0 + width * col, y=y0 + height * line)

def display_game():#Chat gpt je lui est demandé trouve moi le code
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            # Met à jour le texte et la couleur de fond du label en fonction de la valeur dans `numbers`
            labels[line][col].config(
                text=numbers[line][col] or "",
                bg=colours.get(numbers[line][col], "#74E2AE")
            )
            # Affectation des touches aux fonctions, q pour quitter, le reste pour "tasser" dans une certaine direction

def key_pressed(event):
    key = event.keysym  # récupérer le symbole de la touche

    #code qui permet de faire les mouvement gauche, droite, haut, bas avec les touches w,a,s,d
    if key == "Right" or key == "d" or key == "D":
        for line in range(len(numbers)):
            numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0], moves = pack4(numbers[line][3],numbers[line][2],numbers[line][1],numbers[line][0])
    if key == "Left" or key == "a" or key == "A":
        for line in range(len(numbers)):
            numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3], moves = pack4(numbers[line][0],numbers[line][1],numbers[line][2],numbers[line][3])
    if key == "Up" or key == "w" or key == "W":
        for col in range(len(numbers[0])):
            numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col], moves = pack4(numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col])

    if key == "Down" or key == "s" or key == "S":
        for col in range(len(numbers[0])):
            numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col], moves = pack4(numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col])

    display_game()
# code qui permet de quitter le jeu
    if key == "Q" or key == "q":
        result = messagebox.askokcancel("Confirmation", "Voulez-vous vraiment quitter ?")
        if result:
            quit()

# permet d'appeler key_pressed avec n'importe quelle touche
win.bind("<Key>", key_pressed)
win.mainloop()


