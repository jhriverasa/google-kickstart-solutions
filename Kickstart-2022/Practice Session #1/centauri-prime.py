T = int(input())
for test in range(T):
    name = input()
    l = len( name )
    last = name[ l-1 ].lower()
    rule = ""
    
    if (last in ["a","e", "i","o","u"]): rule="Alice"
    elif( last == "y"): rule = "nobody"
    else: rule= "Bob"
  
    print(f"Case #{test+1}: {name} is ruled by {rule}.")
        