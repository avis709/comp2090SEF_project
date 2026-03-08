id_list = [0, 1, 2, 3]
from binary_search import binarySearch
import random
class race_100meter:
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

    def getsname(self):
        print(self.name)

    def getscore(self):
        print(self.score)

    def getid(self):
        print(self.id)

    def gethouse(self):
        print(self.house)


def register():
    mistake = False
    while mistake == False:
        new_name = input("please enter your name")
        new_house = str(input("please enter your house"))
        if new_house.upper() != "PINK" and new_house.upper() != "RED" and new_house.upper() != "YELLOW" and new_house.upper() != "BLUE":
            print("house not found")
            mistake = True
        contest = int(input("what contest did you attend? \n1.100m race\t2.300m race\t3.400m relay\t4.long jump\n please enter the number of the contest you attended  "))
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
            return new_name, new_id, new_score, new_house.upper(), "100meter_run"


            


    if contest == 1:
        print("hi") 


    









Alex = race_100meter("alex", 17, 15, "red")
Alex.getid()
logout = False
while logout == False:
    print(len(id_list))
    print(Alex.id, Alex.score, Alex.house)
    print("what would you like to do? \n1. record score \n2.check score \n3.check top ranking")
    choice = input()
    if choice == "1":
        new_name, new_id, new_score, new_house, match = register()
        print(new_id)
        a = race_100meter(new_name, new_id, new_score, new_house)
        a.getid()
        


        




