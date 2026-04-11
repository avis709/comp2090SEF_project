id_list = [0, 1, 2, 3]
from binary_search import binarySearch
import random
class race_rec:
    def __init__(self, name, uid, score, house):
        self.name = name
        self.id = uid
        self.score = score
        self.house = house

    def __add__(self, other):
        total_score = self.score + other.score
        
    def __eq__(self, other):
        if self.score > other.score:
            return "you have a higher score"
        elif self.score < other.score:
            return "you have a lower score"
        else:
            return "you have an equal score"

    def getname(self):
        print(self.name)

    def getid(self):
        print(self.id)

    def gethouse(self):
        print(self.house)



class race_100meter(race_rec):
    def getscore(self):
        print(self.score,"second")
        
class race_300meter(race_rec):
    def getscore(self):
        print(self.score,"second")
        
class race_400mrelay(race_rec):
    def __init__(self, name, uid, score, house,teammate1,teammate2,teammate3,teammate4):
        super().def __init__(self, name, uid, score, house)
        self.teammate1 = teammate1
        self.teammate2 = teammate2
        self.teammate3 = teammate3
        self.teammate4 = teammate4

    def getscore(self):
        print(self.score,"second")
        
    def getteamates(self):
        print("first runner name:",self.teamate1,"second runner name:",self.teamate2,"third runner name:",self.teamate3,"fourth runner name:",self.teamate4)
        
class race_longjump(race_rec):
    def getscore(self):
        print(self.score,"cm")

def start(filename):
    try:
        with open(filename, 'r') as file:
            
            array = file.readlines()
            
            array = [line.strip() for line in array]
            
            return array
                
           

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []







def save(filename,main_array):
    print("Saving")
    
    try:
        with open(filename, 'w') as file:
            for item in main_array:
                file.write(str(item)+"\n")
                
        print("Saved")
        
    except Exception as e:
        print(f"Error saving file: {e}")

def arrange1(kind, place, extra, contact, isfinder, UID):
    
    main_array = []
    
    length = len(name)
    
    for i in range(length):
        item = name[i]
        item2 = id_list[i]
        item3 = score[i]
        item4 = house[i]
        item5 = teamates[i*3]
        item6 = teamates[i*3+1]
        item7 = teamates[i*3+2]
        item8 = rank[i]
        
        main_array.append(item)
        main_array.append(item2)
        main_array.append(item3)
        main_array.append(item4)
        main_array.append(item5)
        main_array.append(item6)
        main_array.append(item7)
        main_array.append(item8)

                        
                        
    return main_array

def

 
name=[] 

id_list=[] 

score=[] 

house=[] 

teammates=[]  

rank= [] 


Main = start("leaderboard_data.txt")

count = 0

while count != len(Main):
    name.append(Main[count])
    id_list.append(Main[count+1])
    score.append(Main[count+2])
    house.append(Main[count+3])
    teammates.append(Main[count+4])
    teammates.append(Main[count+5])
    teammates.append(Main[count+6])
    rank.append(Main[count+7])
    count = count+8

def ranking():
    for a in scores

def register():
    mistake = False
    while mistake == False:
        new_name = input("please enter your name/first runner in relay")
        new_house = str(input("please enter your house"))
        if new_house.upper() != "PINK" and new_house.upper() != "RED" and new_house.upper() != "YELLOW" and new_house.upper() != "BLUE":
            print("house not found")
            mistake = True
        contest = int(input("what contest did you attend? \n1.100m race\t2.300m race\t3.4x100m relay\t4.long jump\n please enter the number of the contest you attended  "))
        if contest < 1 or contest > 4:
            print("enter a valid number")
        new_score = input("please enter your score(in second or cm):")
        finale = False
        while finale == False:
            new_id = contest * 1000 + random.randint(0, 999)
            if binarySearch(id_list, 0, len(id_list)-1, new_id) == -1:
                finale = True
                
                id_list.append(new_id)
        print(id_list)
            
        if contest == 1:
            print("po")
            return new_name, new_id, new_score, new_house.upper(), " ", " ", " ", " ", "100meter_run"

        if contest == 2:
            print("hi") 
            return new_name, new_id, new_score, new_house.upper(), " ", " ", " ", " ", "300meter_run"
            
        if contest == 3:
            teammate1 = new_name
            print("please enter the name if the second runner") 
            teammate2 = input(name:)
            print("please enter the name if the third runner") 
            teammate3 = input(name:)
            print("please enter the name if the fourth runner") 
            teammate4 = input(name:)
            return new_name, new_id, new_score, new_house.upper(), teammate1, teammate2, teammate3, teammate4, "4x100mrelay"
             
        if contest == 4:
            print("hi") 
            return new_name, new_id, new_score, new_house.upper(), " ", " ", " ", " ", "longjump"

    









Alex = race_100meter("alex", 17, 15, "red")
Alex.getid()
logout = False
while logout == False:
    print(len(id_list))
    print(Alex.id, Alex.score, Alex.house)
    print("what would you like to do? \n1. record score \n2.check score \n3.check top ranking\n4.exit")
    choice = input()
    if choice == "1":
        new_name, new_id, new_score, new_house, match, t1, t2, t3, t4 = register()
        print(new_id)
        if match = "100meter_run":
            for s in rank[] where 
            user = race_100meter(new_name, new_id, new_score, new_house)
        elif match = "300meter_run":
            user = race_300meter(new_name, new_id, new_score, new_house)
        elif match = "4x100mrelay":
            user = race_400mrelay(new_name, new_id, new_score, new_house, t1, t2, t3, t4)
        elif match = "longjump":
            user = race_longjump(new_name, new_id, new_score, new_house)
            
        print("your ID is ", user.getid(), " please remember it")
    elif choice == "2":
        user_ID = input("please insert your ID:")
        if binarySearch(id_list, 0, len(id_list)-1, user_ID) == -1:
            print("ID not found")
        else:
            if  
    elif choice == "3":
        print("the top 10 for 100m:\n",
        
        


        




