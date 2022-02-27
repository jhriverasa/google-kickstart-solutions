from sys import stdin

#This solution only passes test case and Test Set #1
#Despite of that, no one in the Kickstart 2013 - round B actually passed Test Set #2
#Also, I found out that any participant that passed only Test Set #1 got the points for Sets #1 and #2
#I suppose that was an error with Test Set #2, Im not completely sure.

def readAllFile(path): #To read from File (and test locally)
  #Open a file: file
  file = open(path,mode='r')
  # read all lines at once
  all_of_it = file.read()
  # close the file
  file.close()
  return all_of_it
 
#This function looks for "/*" 
#then looks for its closing tag "*/" if it finds another "/*" looks for 2 "*/" and so on
#finally return the indices between comments so we can cut our string.
def findIndexes(l: list, index: int): 
  cb = l.find('/*',index)
  i = cb+2
  counter =1
  while(counter>0):
    nB = l.find('/*',i)
    nE = l.find('*/',i)
    if(nB == -1): return [cb,nE] #when cB is the index of last comment begin, nB will be -1
    if( nB< nE):
      counter+=1
      i=nB+2
    else:
      counter-=1
      i=nE+2
      ce = nE
  return [cb,ce]


lines = "" 
for line in stdin: #read all lines and create a single string
  lines += line
curIndex= 0
toDelete = []
finished = False
length = (len(lines))
while(not finished):
  cb, ce =  findIndexes(lines, curIndex)
  if(cb != -1 and ce != -1):
    lines = lines[:cb] +lines[ce+2:] #Cut String
    curIndex=cb+2
  else:
    finished = True
print('Case #1:')
print(lines)
