#Using queue Implemented with heap Data Structure
import heapq as hq

def addToPriorityQueue(w:int, aQ: list, bQ: list ):
    if(w%2 ==0): #Bob
      hq.heappush(bQ,-w) #Save using additive inverse, so heap is gonna pop the inverse additive of maximum
    else: #Alex
      hq.heappush(aQ,w)
    
def sort(shelf:list , aQ: list, bQ: list):
  sorted = []
  for i in range(len(shelf)):
    if(shelf[i] % 2 ==0): #Bob
      sorted.append(hq.heappop(bQ)*-1)
    else: #Alex
      sorted.append(hq.heappop(aQ))
  return sorted

nTests = int(input())
for i in range(nTests):
  N = int(input())
  shelf = list(map(int, input().split(" ")))
  aQ =[]
  bQ = []
  for w in shelf:
    addToPriorityQueue(w,aQ,bQ)
  sortedShelf= sort(shelf, aQ, bQ)
  resStr = ' '.join([str(elem) for elem in sortedShelf])
  print(f"Case #{i+1}:", resStr)
    

  