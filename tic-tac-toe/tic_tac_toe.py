import re
import random
_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

_DIAG_1= [0,4,8]
_DIAG_2= [2,4,6]

_ROW_1= [0,1,2]
_ROW_2= [3,4,5]
_ROW_3= [6,7,8]

_COLUMN_1= [0,3,6]
_COLUMN_2= [1,4,7]
_COLUMN_3= [2,5,8]

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    
    if self.board[_DIAG_1[0]] == self.board[_DIAG_1[1]] and self.board[_DIAG_1[1]] == self.board[_DIAG_1[2]] and self.board[_DIAG_1[2]] is not None:
      self.is_game_over = True
    elif self.board[_DIAG_2[0]] == self.board[_DIAG_2[1]] and self.board[_DIAG_2[1]] == self.board[_DIAG_2[2]] and self.board[_DIAG_2[2]] is not None:
      self.is_game_over = True
    elif self.board[_ROW_1[0]] == self.board[_ROW_1[1]] and self.board[_ROW_1[1]] == self.board[_ROW_1[2]] and self.board[_ROW_1[2]] is not None:
      self.is_game_over = True
    elif self.board[_ROW_2[0]] == self.board[_ROW_2[1]] and self.board[_ROW_2[1]] == self.board[_ROW_2[2]] and self.board[_ROW_2[2]] is not None:
      self.is_game_over = True
    elif self.board[_ROW_3[0]] == self.board[_ROW_3[1]] and self.board[_ROW_3[1]] == self.board[_ROW_3[2]] and self.board[_ROW_3[2]] is not None:
      self.is_game_over = True
    elif self.board[_COLUMN_1[0]] == self.board[_COLUMN_1[1]] and self.board[_COLUMN_1[1]] == self.board[_COLUMN_1[2]] and self.board[_COLUMN_1[2]] is not None:
      self.is_game_over = True
    elif self.board[_COLUMN_2[0]] == self.board[_COLUMN_2[1]] and self.board[_COLUMN_2[1]] == self.board[_COLUMN_2[2]] and self.board[_COLUMN_2[2]] is not None:
      self.is_game_over = True
    elif self.board[_COLUMN_3[0]] == self.board[_COLUMN_3[1]] and self.board[_COLUMN_3[1]] == self.board[_COLUMN_3[2]] and self.board[_COLUMN_3[2]] is not None:
      self.is_game_over = True
    
    if self.is_game_over and self.turn == _PLAYER:
         self.winner = _MACHINE
    elif self.is_game_over:
         self.winner= _PLAYER

    return self.is_game_over

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    
    while True: 
      rand = random.randint(0,8)
      cell = self.board[rand]
      if cell is None:
        self.board[rand] = _MACHINE_SYMBOL
        break

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
     if self.winner is None:
       print("Tie!")
     else:
      print("The winner is: "+self.winner)  

