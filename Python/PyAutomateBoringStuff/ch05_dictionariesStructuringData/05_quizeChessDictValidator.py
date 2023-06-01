import re, pprint

# Valid board
# theBoard = {
#   '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
#   '5h': 'bqueen', '3e': 'wking', 
# }

# Invalid Position
# theBoard = {
#   '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
#   '5h': 'bqueen', '3e': 'wking', 
#   '9z': 'bknight', '1x': 'wknight', '0b': 'wpawn'
# }

# Invalid: Unknown Piece
# theBoard = {
#   '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
#   '5h': 'bqueen', '3e': 'wking', 
#   '5a': 'bspearman'
# }

# Invalid: More than 1 King per team
# theBoard = {
#   '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
#   '5h': 'bqueen', '3e': 'wking', 
#   '3c': 'bking'
# }

# Invalid: More than 8 pawns per team
# theBoard = {
#   '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
#   '5h': 'bqueen', '3e': 'wking', 
#   '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', 
#   '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn', 
#   '6a': 'wpawn'
# }

# Invalid: More than 16 pieces per team
theBoard = {
  '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
  '5h': 'bqueen', '3e': 'wking', 
  '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', 
  '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn', 
  '6a': 'wrook', '6b': 'wknight', '6d': 'wbishop', 
  '6e': 'wbishop', '6f': 'wknight', '6g': 'wrook',
  '5a': 'wqueen', '5b': 'wqueen' 
}

def isValidChessBoard():
  return None

def isValidPosition(board):
  invalidCtr = 0
  
  # Valid spaces: '1a' to '8h'
  for position in board:
    isValid = re.search("[1-8][a-h]", position)

    if not isValid:
      invalidCtr += 1

  if invalidCtr > 0:
    print('Invalid. There are ' + str(invalidCtr) + ' unknown positions.')
    return False
  else:
    print('ALL Positions: OK')
    return True
  

def isValidPlayer(allPieces):
  invalidCtr = 0
  # 'w' represents white & 'b' represents black
  # 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
  
  # For the board: 1 black king, 1 white king
  if not checkKings(allPieces):
    invalidCtr += 1
    return False
  # Per player: 8 pawns max 
  if not checkPawns(allPieces):
    invalidCtr += 1
    return False
  # Per player: 16 pieces max
  if not checkNumPiecesPerTeam(allPieces):
    invalidCtr += 1
    return False

  print('ALL Pieces per Player: OK')
  return True


def checkKings(allPieces):
  if allPieces['wking'] == 1 and allPieces['bking'] == 1:
    return True
  else:
    print('Invalid. There are ' + str(allPieces['bking']) + ' Black King/s', end='')
    print(' and ' + str(allPieces['wking']) + ' White King/s')
    return False


def checkPawns(allPieces):
  if (allPieces['wpawn'] >= 0 and allPieces['wpawn'] <= 8) and \
      (allPieces['bpawn'] >= 0 and allPieces['bpawn'] <= 8):
    return True
  else:
    print('Invalid. There is/are ' + str(allPieces['bpawn']) + ' Black Pawn/s', end='')
    print(' and ' + str(allPieces['wpawn']) + ' White Pawn/s')
    return False


def checkNumPiecesPerTeam(allPieces):
  wtotal = 0
  btotal = 0
  for piece, count in allPieces.items():
    if re.search('^w', piece):
      wtotal += count
    if re.search('^b', piece):
      btotal += count

  print('Total Whites: ', wtotal, ', Total Blacks: ', btotal)
  if (wtotal >= 1 and wtotal <= 16) and (btotal >= 1 and btotal <= 16):
    return True
  elif wtotal > 16:
    print('Invalid. White team exceeds 16 pieces')
  elif btotal > 16:
    print('Invalid. Black team exceeds 16 pieces')
  
  return False

def isValidNumPieces(board):
  # Count the number of chess pieces and if there are invalid ones
  numPieces = {
    'others': 0,
    'wking': 0, 'wqueen': 0, 'wpawn': 0,
    'wbishop': 0, 'wknight': 0, 'wrook': 0,
    'bking': 0, 'bqueen': 0, 'bpawn': 0,
    'bbishop': 0, 'bknight': 0, 'brook': 0
  }
  
  for pos, piece in board.items():
    if piece not in numPieces.keys():
      numPieces['others'] += 1
    else:
      numPieces[piece] += 1

  if numPieces['others'] > 0:
    print('There is/are ' + str(numPieces['others']) + ' piece/s that do not belong to any team')
    return False
  else:
    return isValidPlayer(numPieces)


# MAIN LOOP
if isValidPosition(theBoard) and isValidNumPieces(theBoard):
  print('CONGRATULATIONS! This is a VALID BOARD!')