
#This is solved using Bipartite graph concept
#So what we're doing is trying to find an odd-length cycle which makes a bipartition impossible.
#Translating this to Two-Coloring Problem is going to make the job

RED = 0
BLUE = 1

def testBipartite(d:dict, dc:dict):
  for villain in d:
    villainColor= dc.get(villain)
    if(villainColor == None):
      if(not assignColor(d=d,dc=dc,villain=villain, color=RED)):
        return "No"
  return "Yes"


def assignColor(d:dict, dc:dict, villain:str, color:int):
  dc[villain] = color
  for enemy in d[villain]:
    if (dc.get(enemy)== None and not assignColor(d=d,dc=dc,villain=enemy, color=1-color)):
      return False
    elif(dc.get(enemy) == color):
      return False
  return True





def storeMembers(member1:str, member2:str, d: dict):
  isMember1ListEmpty =d.get(member1) == None
  isMember2ListEmpty =d.get(member2) == None

  if(isMember1ListEmpty ):
    d[member1] = [member2] 
  else:
    member1List = d.get(member1)
    member1List.append(member2)
  
  if(isMember2ListEmpty ):
    d[member2] = [member1] 
  else:
    member2List = d.get(member2)
    member2List.append(member1)

  return d


nCases = int(input())
for i in range(nCases):
  nCouples = int(input())
  dic = {}
  dc = {}

  #store members in a graph
  for j in range(nCouples):
    member1, member2 = list(input().split(" "))
    storeMembers(member1=member1, member2=member2, d=dic)
  #assign colors / check if graph is bipartite
  isPossible = testBipartite(d=dic, dc=dc)


  print(f"Case #{i+1}:", isPossible)