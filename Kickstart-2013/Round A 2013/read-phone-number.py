#Constant with numbers
numbersName={'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine",'0':"zero"}

#Constant with names of consecutive number
consecutiveNames = ["double", "triple", "quadruple", "quintuple", "sextuple", "septuple", "octuple", "nonuple", "decuple"] #-2

def getnumOcurrences(partialStr: str, index: int):
  maxIndex= len(partialStr)-1
  counter=1
  while( index + 1 <= maxIndex and partialStr[index] == partialStr[index+1] ):
    index+=1
    counter+=1
  return counter # ocurrences


def readnDigits(partialStr: str, n: int):
  readList = []
  index= 0
  while(index < n):
    num= partialStr[index]
    numOcurrences = getnumOcurrences(partialStr=partialStr, index=index)
    if(numOcurrences==1): 
      readList.append(numbersName.get(num))
    elif( numOcurrences <= 10 ):
      readList.append(consecutiveNames[numOcurrences-2])
      readList.append(numbersName.get(num))
    else:
      for j in range(numOcurrences):
        readList.append(numbersName.get(num))
    index+=numOcurrences
  return readList


nTests = int(input())
for i in range(nTests):
  number, format = list(input().split(" "))
  format = list(map(int, format.split("-")))
  
  wholeWord =[]
  readDigits= 0
  for j in range(len(format)):
    wholeWord= wholeWord + readnDigits(number[readDigits : readDigits+format[j]], n=format[j]) #Join lists
    readDigits += format[j]
  
  resStr = ' '.join([str(elem) for elem in wholeWord])
  print(f"Case #{i+1}:", resStr)
  