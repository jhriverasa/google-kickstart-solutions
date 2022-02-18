# Solution O(NLog(N)) time complexity
import heapq as hq

def getHindex(cNum: int, c: list):
  minHeap= []
  ans= []
  curH= 0
  for i in range(cNum):
    if c[i] > curH :
      hq.heappush(minHeap,c[i])
      while(minHeap and minHeap[0] <= curH):  
        hq.heappop(minHeap)
    if len(minHeap)  >= curH+1:
      curH+=1
    ans.append(curH)
  return ans

T = int(input())
for i in range(T):
  cNum = int(input())
  c = list(map(int, input().split()))
  res = getHindex(cNum, c)
  print(f"Case #{i+1}:", *res)