#Joey Harig and Mesa Martorell
#JES 5.0
#Tetris Game ( Traptris )

# ---------------------------------------------
#    
#    This script runs a tetris game using the gui library. We use a 10*22 matrix of 0s 
#    for the game logic. 2s represent the active pieces and 1s represent stationary
#    pieces. The game loop checks all positions, adds scores, and updates the colors on
#    the visual board which is made up of gui rectangles. 
#
#    Use the left, right and down arrow keys to move the active piece and use
#    the up arrow key to rotate the piece 90 deg clockwise. The game will move faster the
#    higher your score gets.
#
#    When running the script, open the sound files in the alphabetical order that they
#    are listed in the folder.
#    
# ---------------------------------------------

 
import gui
from time import sleep
from random import randint

#----------------------------------------------
#    Config
#----------------------------------------------

config = {
  'name': 'Traptris',
  'worldSize': 500,
  'worldMarginX': 150,
  'worldMarginY': 20,
  'worldCenter': 250,
  'cellSize': 20,
  'columns': 10,
  'rows': 22,
  'background': gui.Color(50,50,50),
  'color': gui.Color(3,248,255)
}


#----------------------------------------------
#    Score Class
#----------------------------------------------

class Score:
  currentScore = 0
  scoreString = str(currentScore) + '           '
  scoreLabel = gui.Label(scoreString)
  fps = 1
  time = 0 
  
  def changeScore(self, update): #update is an in
      self.currentScore += update # change the score value
      self.fps -= (0.02)
      self.scoreString = str(self.currentScore)
      self.scoreLabel.setText(self.scoreString) # change the score label display
  
  def changeTime(self):
      self.time += self.fps
      if self.time > getDuration(song):
        play(song)
        self.time = 0

#----------------------------------------------
#    A blank tertiary game board
#----------------------------------------------

newBoard = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# make a copy of the board to use for the game
currentBoard = newBoard



#----------------------------------------------
#    A list of Tetris Shapes ( 7 total )
#----------------------------------------------

shapes = [
	   [[2, 2, 2, 2], # IPiece
          [0, 0, 0, 0]], 
	
	   [[2, 0, 0, 0], # LPiece
	   [2, 2, 2, 0]],
           
          [[0, 0, 2, 0], # JPiece
          [2, 2, 2, 0]],
           
          [[0, 2, 2, 0], # OPiece
          [0, 2, 2, 0]],
           
          [[0, 2, 2, 0], # SPiece
          [2, 2, 0, 0]],
           
          [[0, 2, 0, 0], # TPiece
          [2, 2, 2, 0]],
            
          [[2, 2, 0, 0], # ZPiece
          [0, 2, 2, 0]]
]


# add a random piece to the game
def randomPiece():
  rand = randint(0, len(shapes) - 1)
  return gamePiece.addPiece(shapes[rand])

#----------------------------------------------
#    Game Piece Class
#----------------------------------------------

class GamePiece:
  
  currentShape = []
  
  def addPiece(self, shape):
    self.currentShape = shape
   
    for i in range(0, 2): # first 2 rows of board
      for j in range(3, 7): # center 4 columns
        currentBoard[i][j] = shape[i][j - 3] # set the cell in the tetris board = to the shape
  
       
                 
  # All of the Piece Movements
  
  def move(self, key): 
    
    # Leftward Movement
    def left():
      for i in range(0, config['rows']):
        for j in range(0, config['columns']):  # loop goes through array from left to right
          if currentBoard[i][j] == 2:
            currentBoard[i][j - 1] = 2 # change the cell to the left to a 2
            currentBoard[i][j] = 0 # change the selected cell to a 0
            
    # Rightward Movement
    def right():
      for i in range(0, config['rows']):
        j = config['columns'] - 1
        while j >= 0: # loop goes through array from right to left
          if currentBoard[i][j] == 2:  
            currentBoard[i][j + 1] = 2 # change the cell to the right to a 2
            currentBoard[i][j] = 0 # change the selected cell to a 0  
          j = j - 1 
          
    # Downward Movement
    def down():
      i = config['rows'] - 1  
      while i >= 0: # loop goes through array from bottom to top        
        for j in range(0, config['columns']):          
          if currentBoard[i][j] == 2: 
            currentBoard[i + 1][j] = 2 # change the cell below to a 2
            currentBoard[i][j] = 0 # change the selected cell to a 0
        i = i - 1
    
    # Rotate Movemnet
    def rotate():
      cs = self.currentShape # shorten self.currentshape
      for i in range(0, config['rows']): # rows
        for j in range(0, config['columns']): # cols
          if currentBoard[i][j] == 2: # if it is a 2
            if len(self.currentShape) == 2:# if it is a horizantal shape
              # if it is the square shape, don't rotate
              if cs[0][1] == 2 and cs[0][2] == 2 and cs[1][1] == 2 and cs[1][2] == 2:
                return
          
          
              ### if it is the I shape
              if cs[0][0] == 2 and cs[0][3] == 2:
                for n in range(0, 4):
                  # if it isn't able to rotate 
                  if currentBoard[i - n - 1][j] != 0 or i < 2:                 
                    return
                # if it is able to rotate
                for n in range(0, 3):
                  currentBoard[i - n][j] = 2
                  currentBoard[i][j + n + 1] = 0
                currentBoard[i - 3][j] = 2
                self.currentShape = [[2, 0], [2,0], [2,0], [2,0]] # update shape
                return
              
              
              ### if it is not an I shape
              else:
                if cs[0][0] == 2: # if it is a shape with a 2 at [0][0]
                    j += 0
                
                elif cs[0][1] == 2:  # if it is a shape with a 0 at [0][0] and 2 at [0][1]
                  j -= 1 # correct i by 1 
                  
                elif cs[0][1] == 0:  # if it is a shape with a 0 at [0][0] and [0][1] 
                  j -= 2 # correct i by 2
                  
                # if its too far towards the top
                if i < 1:                 
                  return
                #if there are 1s in the way
                for n in range(0, 3):
                  for m in range(0, 2):
                    if currentBoard[i - n][j + m] == 1:
                      return
                # if its able to rotate
                newShape = [ # rotate the shape
                  [cs[1][0], cs[0][0]],
                  [cs[1][1], cs[0][1]],
                  [cs[1][2], cs[0][2]],
                  [cs[1][3], cs[0][3]]                    
                ]
                self.currentShape = newShape # update currentShape
                for n in range(0, 3): 
                  for m in range(0, 2):
                    if currentBoard[i + m][j + n] != 1: # if the shape wouldn't delete a 1
                      currentBoard[i + m][j + n] = 0
                n = 2
                ns = newShape[::-1] # reverse the order of the shape to add it from bottom to top
                while n >= 0:
                  for m in range(0, 2):
                     if currentBoard[i - n + 1][j + m] != 1:
                       currentBoard[i - n + 1][j + m] = ns[n + 1][m]
                  n = n - 1
                return
      
      
            # if it is a vertical shape    
            if len(self.currentShape) == 4:
              sideCorrection = 0 # need to adjust based on if it is on right or left side as to not hit a wall

              ### if it is the I shape
              if cs[0][0] == 2 and cs[3][0] == 2:
                if j >= 5: # if the shape is on the right side of the board, adjust x axis by -3
                  sideCorrection = -3
                for n in range(1, 4):
                  # if it isn't able to rotate because of a 1, return  
                  if currentBoard[i - 3][j + n + sideCorrection] != 0:               
                    return
                # if it is able to rotate
                for n in range(0, 4):
                  currentBoard[i + n][j] = 0
                  currentBoard[i + 3][j + 3 - n + sideCorrection] = 2
                if sideCorrection != 0:
                  currentBoard[i + 3][j] = 2
                self.currentShape = [[2, 2, 2, 2], [0, 0, 0, 0]]
                return
                
                
              ### if it is not an I shape
              else:
                if cs[0][0] == 2: # if it is a shape with a 2 at [0][0]
                    j += 0
                
                elif cs[0][0] == 0:  # if it is a shape with a 0 at [0][0] and 2 at [0][1]
                  j -= 1 # correct i by 1
                  
                # if its on the right side, adjust the x axis
                if j >= 5:                 
                  sideCorrection = -1
                #if there are 1s in the way
                for n in range(0, 3):
                  for m in range(0, 2):
                    if currentBoard[i + m][j + n + sideCorrection] == 1:
                      return
                # if its able to rotate
                newShape = [ # rotate the shape list
                  [cs[2][0], cs[1][0], cs[0][0], [0, 0]],
                  [cs[2][1], cs[1][1], cs[0][1], [0, 0]]
                ]
                self.currentShape = newShape # update currentShape
                for n in range(0, 3): 
                  for m in range(0, 2):
                    currentBoard[i + n][j + m] = 0 # clear the 2s
                for n in range(0, 2): 
                  for m in range(0, 3):
                    currentBoard[i + 1 + n][j + m + sideCorrection] = newShape[n][m]
                return

   

    # Check which directions it can move
    canItMoveRight = true
    canItMoveLeft = true
    canItMoveDown = true
    
    for i in range(0, config['rows']): # rows
      for j in range(0, config['columns']): # column within row
        
        if currentBoard[i][j] == 2: # if the cell is the active piece
          
          # Downward Check
          if i == config['rows'] - 1 or currentBoard[i + 1][j] == 1: # it is either at the bottom, or has hit a 1
            canItMoveDown = false
            return "can't"
          
          # Rightward Check
          if j == config['columns'] - 1 or currentBoard[i][j + 1] == 1: # has an index of 9 
            canItMoveRight = false
          
          # Leftward Check
          if j == 0 or currentBoard[i][j - 1] == 1:
            canItMoveLeft = false
        
    if key == 'left' and canItMoveLeft == true:
      left()

    if key == 'right' and canItMoveRight == true: 
      right()
    
    if key == 'down' and canItMoveDown == true:
      down()

    if key == 'rotate':
      rotate()
      


#----------------------------------------------
#    Visual Board 
#----------------------------------------------
        
class VisualBoard:
  
  def __init__(self):
    self.cells = [] # 220 squares to make up the visual board 
    self.scoreLabel = score.scoreLabel
    self.yourFinalScore = gui.Label('Your Final Score Is')
    world.add(self.scoreLabel, config['worldSize'] - (config['worldMarginY'] * 4 ), (config['worldMarginY']))
  
  
  def draw(self): # called once to draw the board
    for i in range(0, config['rows']):
      for j in range(0, config['columns']): 
          x1 = config['worldMarginX'] + (j * config['cellSize'])
          y1 = config['worldMarginY'] + (i * config['cellSize'])
          x2 = x1 + config['cellSize']
          y2 = y1 + config['cellSize']
          
          color = config['background'] # color all of the cells dark grey
          
          self.cells.append(gui.Rectangle(x1, y1, x2, y2, color, true))
              
    for cell in self.cells:
      world.add(cell)
  
  
  def reDraw(self): # called every time the screen refreshes
    for i in range(0, config['rows']):
      for j in range(0, config['columns']):
        string = str(i) + str(j) # convert [i][j] to "ij"
        cell = int(string) # convert "ij" to int
        
        if currentBoard[i][j] == 0:
          color = config['background']
        else:
          color = config['color']
        
        self.cells[cell].setColor(color)
        
  def gameOver(self): # called when the game ends
    for cell in self.cells:
      world.remove(cell)
      
    world.remove(self.scoreLabel)
    
    world.add(self.scoreLabel, config['worldCenter'] - 20, config['worldCenter'])
    world.add(self.yourFinalScore, config['worldCenter'] - 60, config['worldCenter'] - 30)
  

#----------------------------------------------
#    Game Loop
#----------------------------------------------


def gameLoop():
  
  gamePlaying = true
  
  while gamePlaying == true:
  
    moveDown = gamePiece.move('down') # move the 2s down
  
  
    if moveDown == "can't": # if the cur piece can't go down 
    
      # change all 2s to 1s
      for i in range(0, config['rows']): 
        for j in range(0, config['columns']):
        
          if currentBoard[i][j] == 2: 
            currentBoard[i][j] = 1
    
      # check for full rows
      playClap = false
      for i in range(0, config['rows']): # check each row
      
        rowSum = 0
      
        for j in range(0, config['columns']): # add up the 1s
          rowSum += currentBoard[i][j] 
      
        if rowSum == 10: # if the row is full
          
          playClap = true
          
          score.changeScore(100) # update the score
        
          row = i 
        
          while row > 0: # loop through rows from bottom to top
            currentBoard[row] = currentBoard[row - 1] # replace each row with the row above it
            row = row - 1 # go up a row
        
          currentBoard[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # set the top row to 0
        
      if playClap:
        play(clap)
        
      # check the center 2 columns of board for 1s, if they are: game over
      if currentBoard[0][4] == 1 or currentBoard[0][5] == 1: 
        play(cry)
        stopPlaying(song)
        
        visualBoard.gameOver()
        
        gamePlaying = false
    
      # if game isn't over
      else: 
        randomPiece()
    
    # redraw the board
    visualBoard.reDraw()
  
    # sleep and recall gameLoop
    score.changeTime()
    sleep(score.fps)



#----------------------------------------------
#    Set Up Variables
#----------------------------------------------
  
world = gui.Display(config['name'], config['worldSize'], config['worldSize'])
score = Score()
visualBoard = VisualBoard()
gamePiece = GamePiece()

clap = makeSound(pickAFile()) 
cry = makeSound(pickAFile()) 
song = makeSound(pickAFile())

# key event function
def keyDown(key):
  keyHit = key
  
  if keyHit == 37:
    gamePiece.move('left')
  
  if keyHit == 39:
    gamePiece.move('right')
  
  if keyHit == 40:
    gamePiece.move('down')
  
  if keyHit == 38:
    gamePiece.move('rotate')
  
  visualBoard.reDraw()

def close(): 
  stopPlaying(song)
  stopPlaying(cry)

label = gui.Label(config['name'])
world.add(label, config['worldMarginY'], config['worldMarginY'])

label.requestFocus()
label.onKeyDown(keyDown)

world.onClose(close)
  

# start the game
def startGame():
  play(song)
  visualBoard.draw()
  randomPiece()
  visualBoard.reDraw()
  gameLoop()  

startGame()


    
  
  




