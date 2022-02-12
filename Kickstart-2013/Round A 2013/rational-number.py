
def getChildValue(pq, side):
  if (pq == [0,0]): return [1,1] # first 1 means root
  p,q = pq
  if (side == "1"): #Right = "1"
    return [p+q,q]
  else: #left = 0
    return [p, p+q]

def calculateN(p,q):
  binaryStr= ""
  while(p != q):
    if (p>q):
      p-=q
      binaryStr = '1'+ binaryStr
    else:
      q-=p
      binaryStr = '0'+ binaryStr
  binaryStr= '1'+ binaryStr
  return int(binaryStr,2)


nTests = int(input())
for i in range(nTests):
  problemData = list(map(int, input().split(" ")))
  resStr = ""
  if(problemData[0]==1): #Find p,q
    n=problemData[1]
    nBin = bin(n)
    p,q = [0,0]
    for digit in nBin[2:]:
      p,q = getChildValue([p, q], digit)
    resStr = ' '.join([str(elem) for elem in [p,q] ])
  else:#Find n
    p, q = list(map(int, problemData[1:3]))
    resStr = calculateN(p,q)

  print(f"Case #{i+1}:", resStr)