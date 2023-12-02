#read marks of 3 subject and calculate total marks of 3 sub and display grade...
dldm = int(input("Enter the marks in dldm   "))
m3 = int(input("Enter the marks in m3   "))
coep = int(input("Enter the marks in coep   "))
total = dldm+m3+coep
print("The total of three subject is ",total)
if total>90:
    print("you are in 1st class ") 
elif total>80:
    print("you are in 2nd class ")
    
elif total>60:
    print("you are in 3rd class")


   
elif total>40: 
    print(" you are in avrage",)      
else:
    print(" sorry! better luck next time  ")    
