
for turn in range(4):
print "Turn", turn+1
  if guess_row == ship_row and guess_col == ship_col:
  	print "Congratulations! You sank my battleship!"   
  else:
  	if guess_row not in range(5) or \
    	guess_col not in range(5):
        print "Oops, that's not even in the ocean."
  	else:
      print "You missed my battleship!"
    	board[guess_row][guess_col] = "X"
  print_board(board)