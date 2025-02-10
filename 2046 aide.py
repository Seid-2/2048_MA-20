from tkinter import *
import random

# Définition des couleurs pour les tuiles
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

# Initialisation de la grille
numbers = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

labels = [[None for _ in range(4)] for _ in range(4)]

# Fenêtre Tkinter
win = Tk()
win.geometry("700x700")
win.title("2048 - Jeu Tkinter")

# Fonction pour réorganiser et fusionner une ligne (ou colonne)
def pack_4(a, b, c, d):
    line = [x for x in [a, b, c, d] if x != 0]  # Supprime les 0
    moves = len(line) < 4  # Si des cases vides ont été trouvées, il y a un mouvement

    # Fusion des tuiles
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            line[i] *= 2
            line[i + 1] = 0
            moves = True

    # Réorganiser après fusion
    line = [x for x in line if x != 0]
    while len(line) < 4:
        line.append(0)

    return line[0], line[1], line[2], line[3], moves

# Met à jour l'affichage
def display_game():
    for row in range(4):
        for col in range(4):
            labels[row][col].config(
                text=numbers[row][col] or "",
                bg=colours.get(numbers[row][col], "#74E2AE"),
            )

# Ajoute une nouvelle tuile (2 ou 4) à une position aléatoire
def add_new_tile():
    empty_cells = [(r, c) for r in range(4) for c in range(4) if numbers[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        numbers[r][c] = 2 if random.random() < 0.9 else 4
        display_game()

# Vérifie si le jeu est terminé
def is_game_over():
    for row in range(4):
        for col in range(4):
            if numbers[row][col] == 0:
                return False  # Encore des cases vides
            if col < 3 and numbers[row][col] == numbers[row][col + 1]:
                return False  # Fusion possible horizontalement
            if row < 3 and numbers[row][col] == numbers[row + 1][col]:
                return False  # Fusion possible verticalement
    return True

# Déplace les cases vers la gauche
def move_left():
    moved = False
    for i in range(4):
        numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3], move = pack_4(
            numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3]
        )
        moved = moved or move
    if moved:
        add_new_tile()
    if is_game_over():
        game_over_screen()

# Déplace les cases vers la droite
def move_right():
    moved = False
    for i in range(4):
        numbers[i][3], numbers[i][2], numbers[i][1], numbers[i][0], move = pack_4(
            numbers[i][3], numbers[i][2], numbers[i][1], numbers[i][0]
        )
        moved = moved or move
    if moved:
        add_new_tile()
    if is_game_over():
        game_over_screen()

# Déplace les cases vers le haut
def move_up():
    moved = False
    for col in range(4):
        numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col], move = pack_4(
            numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col]
        )
        moved = moved or move
    if moved:
        add_new_tile()
    if is_game_over():
        game_over_screen()

# Déplace les cases vers le bas
def move_down():
    moved = False
    for col in range(4):
        numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col], move = pack_4(
            numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col]
        )
        moved = moved or move
    if moved:
        add_new_tile()
    if is_game_over():
        game_over_screen()

# Affichage de l'écran de fin de partie
def game_over_screen():
    game_over_label = Label(win, text="Game Over!", font=("Arial", 40), bg="red", fg="white")
    game_over_label.place(x=200, y=300)

# Liaison des touches clavier pour jouer
win.bind("<Left>", lambda event: move_left())
win.bind("<Right>", lambda event: move_right())
win.bind("<Up>", lambda event: move_up())
win.bind("<Down>", lambda event: move_down())

# Création des labels pour l'affichage
x0, y0, width, height = 100, 100, 150, 150
for row in range(4):
    for col in range(4):
        labels[row][col] = Label(win, text=numbers[row][col] or "", width=10, height=5,
                                 borderwidth=1, relief="solid", font=("Arial", 15),
                                 bg=colours.get(numbers[row][col], "#74E2AE"))
        labels[row][col].place(x=x0 + width * col, y=y0 + height * row)

# Ajoute deux tuiles pour commencer le jeu
add_new_tile()
add_new_tile()
display_game()

# Lancer la boucle principale
win.mainloop()
