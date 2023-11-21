#TicTacToe Lesson 5
#The game now validates input and (unfinished) checks for winner
board = [['_', '_', '_'], 
         ['_', '_', '_'], 
         ['_', '_', '_']]
turn = "X"
won = False
numberOfMoves = 0

def printBoard():
  print("Tic-Tac-Toe Board")
  print("    0    1    2")
  count = 0
  while count <= 2:
    print(count, board[count])
    count += 1

def makeMove():
  xPos = 3 #intentionally invalid
  yPos = 3 #intentionally invalid
  while(xPos < 0 or xPos > 2 or yPos < 0 or yPos > 2 or board[yPos][xPos] != '_'):
    xPos = int(input("Enter the X position of your piece: "))
    yPos = int(input("Enter the Y position of your piece: "))
  
  board[yPos][xPos] = turn

def checkWinner():
  rowNumber = 0
  columnNumber = 0
  #Check for a horizontal winner
  while rowNumber < 3:
    if (board[rowNumber][0] == board[rowNumber][1] == board[rowNumber][2] == turn):
      print("Winner detected horizontally")
      return True
    rowNumber += 1

  #Check for a vertical winner
  while columnNumber < 3:
    if (board[0][columnNumber] == board[1][columnNumber] == board[2][columnNumber] == turn):
      print("Winner detected vertically")
      return True
    columnNumber += 1

  #Check for a diagonal winner
  if (board[0][0] == board[1][1] == board[2][2] == turn or board[0][2] == board [1][1] == board[2][0] == turn):
    print("Winner detected diagonally")
    return True

printBoard()
while not won:
  print("It is " + turn + "'s turn")
  makeMove()
  printBoard()
  numberOfMoves += 1

  if checkWinner():
    print(+turn+"has won the game")
  elif numberOfMoves == 9:
      print("The players have tied")
  else:
    if turn == "X":
      turn = "O"
    else:
      turn = "X"
