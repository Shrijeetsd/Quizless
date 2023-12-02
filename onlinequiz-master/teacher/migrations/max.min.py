#read three number and print which maximum,minimum
first=int(input("enter a 1st number"))
sec=int(input("enter a 2nd number"))
third=int(input("enter a 3rd number"))
if first>sec and first>third:
    print("first number is maximum ")
elif sec>first and sec>third:
    print("second number is maximum")
else:
    print("third number is geater ")    
    
