#Edison, the robot, performs the next prioritized steps to walk
# 1. Go to left if possible
# 2. Go Forward if possible
# 3. Rotate 90 degrees and go to step 1. 

# First step is to check whether Edison is stuck (he cant walk), if thats not the case, start to walk, 
# considering the limits steps<= 10000

left=0
forward=1

empty = "."
wall = "#"
east = "E"
west = "W"
north = "N"
south = "S"

def amIStuck(curCell,maze,n):
  x,y= curCell
  return (isAWall([x+1,y],n,maze) and isAWall([x-1,y],n,maze) and isAWall([x,y+1],n,maze) and isAWall([x,y-1],n,maze))

def moveTo(direction, curCell,looking):
  x, y = curCell
  if (direction == left):
    if (looking == north ):
      return [[x,y-1], west]
    elif(looking == east ):
       return [[x-1,y], north]
    elif(looking == south ):
       return [[x,y+1], east]
    else: # west
       return [[x+1,y], south]
  elif (direction == forward):
    if (looking == north ):
      return [[x-1,y], north]
    elif(looking == east ):
       return [[x,y+1], east]
    elif(looking == south ):
       return [[x+1,y], south]
    else: # west
       return [[x,y-1], west]
  else: #Ignore This
    print("I Should not be here")
    return [[],'f']

def rotate90degrees(looking):
  if (looking == north ):
    return east
  elif(looking == east ):
    return south
  elif(looking == south ):
    return west
  else: # west
    return north

def canIGoLeft(curCell, looking, maze, n):
  x, y = curCell
  if (looking == north ):
    return not isAWall([x, y-1],n ,maze)
  elif(looking == east ):
    return not isAWall([x-1, y],n ,maze)
  elif(looking == south ):
    return not isAWall([x, y+1],n ,maze)
  else: # west
    return not isAWall([x+1, y],n ,maze)

def canIGoForward(curCell, looking, maze, n):
  x, y = curCell
  if (looking == north ):
    return not isAWall([x-1, y],n ,maze)
  elif(looking == east ):
    return not isAWall([x, y+1],n ,maze)
  elif(looking == south ):
    return not isAWall([x+1, y],n ,maze)
  else: # west
    return not isAWall([x, y-1],n ,maze)


def walk(initialCell, n, maze, exitCell):
  steps=[]
  #Initial direction Im looking
  looking = north
  if initialCell == [0,0]: looking = north
  if initialCell == [0,n-1]: looking = east
  if initialCell == [n-1,0]: looking = west
  if initialCell == [n-1,n-1]: looking = south
  currentCell = initialCell
  curX , curY = currentCell
  exitX, exitY = exitCell
  finished= False
  
  while(len(steps) < 10000 and (not finished)):
    isLeftPosible= canIGoLeft(currentCell,looking,maze,n)
    if( isLeftPosible ):
      currentCell, looking = moveTo(left, [curX,curY], looking)
      steps.append(looking)
      curX, curY = currentCell
      if [curX,curY] == [exitX,exitY]: finished = True
    elif( canIGoForward(currentCell,looking, maze,n)): #isForwardPossible?
      currentCell, looking = moveTo(forward,[curX,curY], looking)
      steps.append(looking)
      curX, curY = currentCell
      if [curX,curY] == [exitX,exitY]: finished = True
    else:
      looking= rotate90degrees(looking)
  return  [finished,''.join(steps)]



def isAWall(cell, n ,maze):
  isWall = False
  x, y = cell 
  if( x<0 or  x>=n or y<0 or y>= n): 
    isWall = True #limit wall
  elif( maze[x][y] == wall): 
    isWall= True #is Actually a wall
  return isWall


#---Main---- 
nTests = int(input())
for i in range(nTests):
  N = int(input())
  maze = []
  for rows in range(N):
    maze.append(input())
  sx, sy , ex, ey = list(map(int, input().split(" ")))
  initialCell = [sx-1,sy-1] #0-index
  exitCell = [ex-1, ey-1] #0-index
  if(amIStuck(initialCell,maze,N)): 
    print(f"Case #{i+1}: Edison ran out of energy.")
  else:
   isPossible, pathString= walk(initialCell,N,maze,exitCell)
   if(not isPossible):
    print(f"Case #{i+1}: Edison ran out of energy.")
   else:
     print(f"Case #{i+1}: {len(pathString)}")
     print(pathString)

