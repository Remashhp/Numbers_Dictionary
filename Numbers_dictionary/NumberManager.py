from collections import defaultdict
class HashList:
    def __init__(self):
     self.List_map = defaultdict(list) #Initialize an empty dictionary to store numbers and names
     
    def add_number(self,name,number):
         exite=False
         while not exite:
           self.List_map[number].append(name) 
           print("Number added successfully!")
           addmore=input("enter 1 to add more")
           if addmore == '1':
             name = input("Enter the name of the owner of the number: ")
             number = input("Enter the number that you want to add: ")
             exite = False
           else:
               exite = True
               
    def search(self,name):
         for number, names in self.List_map.items():
            if name in names:
                print(f"Number: {number}, Owner: {name}")
        