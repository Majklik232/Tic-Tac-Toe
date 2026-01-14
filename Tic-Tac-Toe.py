# Hrací pole
board = [" " for _ in range(9)]

# Symboly hráčů
player1 = "X"
player2 = "O"
current_player = 2

# Zobrazení hracího pole
def show_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

# Kontrola výhry
def check_winner(symbol):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

# Kontrola remízy
def check_draw():
    return " " not in board

# Úvod
print("Vítej ve hře Tic-Tac-Toe")
print("Hráč 1 má symbol:", player1)
print("Hráč 2 má symbol:", player2)
print("Zadej číslo pole 1–9\n")

show_board()

# Smyčka hry
while True:
    symbol = player1 if current_player == 1 else player2
    move = input(f"Hráč {current_player} ({symbol}), zadej pozici (1-9): ")

    if not move.isdigit():
        print("Zadej číslo!")
        continue

    move = int(move)

    if move < 1 or move > 9:
        print("Zadej číslo od 1 do 9!")
        continue

    if board[move - 1] != " ":
        print("Pole je obsazené!")
        continue

    board[move - 1] = symbol
    show_board()

    if check_winner(symbol):
        print(f" Vyhrál Hráč {current_player} ({symbol})!")
        break

    if check_draw():
        print(" Remíza!")
        break

    # Přepnutí hráče přepiště current_player = na 1 nebo 2 podle počtu hráčů (Jestli tohle čtete můžete přepnout i do modu pro jednoho hráče, aby jste se mohly cítit sámy a mít deprese že nemáte kamarády ): )

    current_player = 2 if current_player == 1 else 1
