T = int(input())
for i in range(T):
    n,c = list(map(int, input().split())) 
    b = list(map(int, input().split()))
    sum = 0
    for bag in b:
        sum+= bag
    res = sum % c
    print(f"Case #{i+1}:", res)
    