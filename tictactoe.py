import pyfiglet

def check():
    if game_board[0][0]==" X "and game_board[0][1]==" X "and game_board[0][2]==" X ":
        print("player1 win")
    if game_board[0][0]==" O "and game_board[0][1]==" O "and game_board[0][2]==" O ":
        print("player2 win")
    if game_board[1][0]==" X "and game_board[1][1]==" X "and game_board[1][2]==" X ":
        print("player1 win")
    if game_board[1][0]==" O "and game_board[1][1]==" O "and game_board[1][2]==" O ":
        print("player2 win")
    if game_board[2][0]==" X "and game_board[2][1]==" X "and game_board[2][2]==" X ":
        print("player1 win")
    if game_board[2][0]==" O "and game_board[2][1]==" O "and game_board[2][2]==" O ":
        print("player2 win")
    if game_board[0][0]==" X "and game_board[1][1]==" X "and game_board[2][2]==" X ":
        print("player1 win")
    if game_board[0][0]==" O "and game_board[1][1]==" O "and game_board[2][2]==" O ":
        print("player2 win")
    if game_board[0][1]==" X "and game_board[1][1]==" X "and game_board[2][0]==" X ":
        print("player1 win")
    if game_board[0][1]==" O "and game_board[1][1]==" O "and game_board[2][0]==" O ":
        print("player2 win")
    if game_board[0][0]==" X "and game_board[1][0]==" X "and game_board[2][0]==" X ":
        print("player1 win")
    if game_board[0][0]==" O "and game_board[1][0]==" O "and game_board[2][0]==" O ":
        print("player2 win")
    if game_board[0][1]==" X "and game_board[1][1]==" X "and game_board[2][1]==" X ":
        print("player1 win")
    if game_board[0][1]==" O "and game_board[1][1]==" O "and game_board[2][1]==" O ":
        print("player2 win")
    if game_board[0][2]==" X "and game_board[1][2]==" X "and game_board[2][2]==" X ":
        print("player1 win")
    if game_board[0][2]==" O "and game_board[1][2]==" O "and game_board[2][2]==" O ":
        print("player2 win")
        exit()

def show():
    for row in game_board:
        for cell in row:
            print(cell,end="")
        print()
title=pyfiglet.figlet_format("Tic Tac Toe",font="slant")
print(title)

game_board=[[" - "," - "," - "],
            [" - "," - "," - "],
            [" - "," - "," - "]]
show() 

def game():
    while True:
        print("player1")
        while True:
            row=int(input("choose row:"))
            col=int(input("choose col:"))
            if game_board[row][col]==" - ":
                game_board[row][col]=" X "
                show()
                check()
                break
            else:
                print("khone dige ntekhab kon")
            print('player2')
        while True:
            row=int(input("choose row:"))
            col=int(input("choose col:"))
            if game_board[row][col]==" - ":
                game_board[row][col]=" O "
                show() 
                check()          
                break
            else:
                print("khone dige entekhab kon")
                

game()
