class Employee():
    count=101
    
    def __init__(self,n,b):
        self.id=Employee.count    #static member...........................................
        self.name=n
        self.basicsalary=b
        Employee.count+=1
        
    def calculate(self):
        self.da=self.basicsalary*10/100
        self.hra=self.basicsalary*30/100
        self.gs=self.basicsalary+self.da+self.hra
        
    def display(self):
        print("Id=",self.id,"Name=",self.name,"Gross salary=",self.gs)        
        
        
e1=Employee("Arbaz",12000)
e1.calculate()
e1.display()

e2=Employee("Shri",15000)
e2.calculate()
e2.display()


e2=Employee("Sangram",18000)
e2.calculate()
e2.display()
              
e3=Employee("Salman",17880)
e3.calculate()
e3.display()