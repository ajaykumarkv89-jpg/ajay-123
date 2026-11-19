class employe:
    def getemploye(self):
        print("enter employe detalis:")
        self.id = input("id:")
        self.name = input("name:")
        self.sal = int(input("salary:"))
            
    def salary(self):
        da = self.sal * 40/100
        hra = self.sal * 16/100
        self.na = self.sal + da + hra
        
    def display(self):
        print("%5s %25s %10s %10s" %(self.id,self.name,self.sal,self.na))

# main
n = int(input("enter total number of empolye:"))
emplist = []
for i in range(n):
    e = employe()
    e.getemploye()
    e.salary()
    emplist.append(e)
    
print("_"*50)
print("EMPLOYEE DETAILS")
print("_"*50)   
      
for e in emplist:
    e.display()
    