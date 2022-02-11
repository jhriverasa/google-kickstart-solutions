nCases = int(input())
for i in range(nCases):
  nWords = int(input())
  lastCard = ""
  totalPrice = 0
  for j in range(nWords):
    currentCard = input()
    if lastCard == "": 
      lastCard = currentCard #first time case
    else:
      if currentCard < lastCard:
        totalPrice+=1
      if currentCard > lastCard:
        lastCard= currentCard #current is gonna be the last card
  print(f"Case #{i+1}:", totalPrice)


      
    


      