s=int(input("enter a selling price"))
c=int(input("enter a cost price"))

if c<s:
    m=s-c
    print("You are in profit by RS.",m )
else:
    n=c-s
    print("you are in loss by RS.",n)        