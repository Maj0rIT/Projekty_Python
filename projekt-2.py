import os

plansza = [[" "," "," "], [" ", " ", " "], [" "," ", " "]]

def display_plansza():
    os.system('cls' if os.name == 'nt' else 'clear') #Clear Consol
    for row in plansza:
        print("|".join(row))

def get_move(player):
    print(f"Gracz {player}, podaj wynik (0-2): ")
    row = int(input())
    print(f"Gracz {player}, podaj wynik (0-2): ")
    col = int(input())
    return row, col

def place_move(player, row, col):
    plansza[row][col] = player

def is_winner(player):
    #Check the line
    for row in plansza:
        if row == [player, player, player]:
            return True
        
    
    #Check the columns
    for col in range(3):
        if [plansza[0][col], plansza[1][col], plansza[2][col]] == [player, player, player]:
            return True
    
    #Check the diagonals
    if [plansza[0][0], plansza[1][1], plansza[2][2]] == [player, player, player] or \
            [plansza[0][2], plansza[1][1], plansza[2][0]] == [player, player, player]:
        return True
    
    return False

def is_plansza_full():
    for row in plansza:
        if " " in row:
            return False
    return True

while True:
    display_plansza()
    row, col = get_move("X")
    place_move("X", row, col)
    if is_winner("X"):
        display_plansza()
        print("Gracz X wygrał!")
        break
    if is_plansza_full():
        display_plansza()
        print("Remis!")
        break
    display_plansza()
    row, col = get_move("O")
    place_move("O", row, col)
    if is_winner("O"):
        display_plansza()
        print("Gracz O wygrał!")
        break
    if is_plansza_full():
        display_plansza()
        print("Remis!")
        break

input()

