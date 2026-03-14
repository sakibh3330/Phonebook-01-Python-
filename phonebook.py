#--> Author <--#
###sakibh3330###
print("Phonebook")

class Phonebook:
    names = []
    numbers = []
    
    def __init__(self):
        print("1.Find number\n2.Add number\n3.Edit number\n4.Delete number")
        
        self.userCh = input("Enter 1,2,3,4:- ")
        
        if self.userCh == '1':
            self.find()
        elif self.userCh == '2':
            self.add()
        elif self.userCh == '3':
            self.edit()
        elif self.userCh =='4':
            self.delete()
        
    def find(self):
        print("1.Name\n2.Number")
        self.usrCh = input("Enter 1,2:- ")
        
        if self.usrCh == '1':
            self.usrCh = input("Enter name:-  ")
            
            self.size = len(self.names)
            
            for i in range(self.size) :
                if self.names[i]==self.usrCh:
                    print(self.numbers[i])
                    break
                
                    
        elif self.usrCh == '2':
            self.usrCh = input("Enter number:-  ")
            self.size = len(self.names)
           
            for i in range(self.size) :
                if self.numbers[i]==self.usrCh:
                    print(self.names[i])
                    break
                    
         
    def add(self):
        self.usrNam = input("Enter name:- ")
        self.usrNum = input("Enter number:- ")
        
        self.names.append(self.usrNam)
        self.numbers.append(self.usrNum)
        
        self.usrCh = input("Enter C, E:- ")
        
        if self.usrCh == 'C':
            self.add()
            
    def delete(self):
        self.size = len(self.names)
        for i in range(self.size):
            print(f"{i}.{self.names[i]} - {self.numbers[i]}")
        
        self.usrIn = int(input("Enter serial no:- "))
        
        del self.names[self.usrIn]
        del self.numbers[self.usrIn]
        
        self.usrIn = input("Enter C,E:- ")
        
        if self.usrIn == 'C':
            self.delete()
        
    def edit(self):
         print("Edit contact")
            
         self.size = len(self.names)
            
         for i in range(self.size):
            print(f"{i}.{self.names[i]} - {self.numbers[i]}")
         self.usrIn = input("1.Name\n2.Number\nEnter 1,2:- ")
         
         if self.usrIn == '1':
            self.usrSl = int(input("Enter serial:- "))
            self.usrN = input("Enter name:- ")
            
            self.names[self.usrSl] = self.usrN
            
        
while True:
    print(Phonebook())



        