import math

#Max distance of a projectile xmax= V^2*sin(2*theta)/g
#We can solve theta
nCases = int(input())
for i in range(nCases):
  V, D = list(map(int, input().split(" ")))
  argument = round( D*9.8/V**2,8) #fix precision errors  (argument > 1)
  theta = math.degrees( (1/2) * math.asin(argument))
  
  print(f"Case #{i+1}:", theta)