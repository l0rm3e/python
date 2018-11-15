player1 = input("Player1 picks : ")
player2 = input("Player2 picks : ")

if player1 == 'rock' and player2 == 'scissors':
    print("Player 1 wins")

if player1 == 'paper' and player2 == 'rock':
    print("Player 1 wins")

if player1 == 'scissors' and player2 == 'paper':
    print("Player 1 wins")

if player2 == 'rock'and player1 == 'scissors':
    print("Player 2 wins")

if player2 == 'paper' and player1 == 'rock':
    print("Player 2 wins")

if player2 == 'scissors' and player1 == 'paper':
    print("Player 2 wins")