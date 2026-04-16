from abc import ABC, abstractmethod



class race_rec(ABC):
    def __init__(self, name, uid, score, house):
        self._name = name
        self._id = uid
        self._score = float(score)
        self._house = house
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._id = int(value)
        else:
            raise ValueError("ID must be a positive number")
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._score = float(value)
        else:
            raise ValueError("Score must be a non-negative number")
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, value):
        valid_houses = ["pink", "red", "yellow", "blue"]
        if value.lower() in valid_houses:
            self._house = value.lower()
        else:
            raise ValueError("Invalid house. Must be Pink, Red, Yellow, or Blue")
    
    @abstractmethod
    def getscore(self):
        pass
    
    @abstractmethod
    def get_unit(self):
        pass
    
    @abstractmethod
    def get_race_type(self):
        pass
    
    def getname(self):
        print(self._name, ":")
    
    def getid(self):
        print("UID:", self._id)
    
    def gethouse(self):
        print("house:", self._house)
    
    def can_compare(self, other):
        if not isinstance(other, race_rec):
            return False
        return self.get_race_type() == other.get_race_type()
    
    def __eq__(self, other):
        if not isinstance(other, race_rec):
            return NotImplemented
        if not self.can_compare(other):
            return "Cannot compare different race types"
        if self._score < other._score:
            return "you have a higher score"
        elif self._score > other._score:
            return "you have a lower score"
        else:
            return "you have an equal score"
    
    def __lt__(self, other):
        if not isinstance(other, race_rec):
            return NotImplemented
        if not self.can_compare(other):
            raise TypeError(f"Cannot compare {self.get_race_type()} with {other.get_race_type()}")
        return self._score < other._score
    
    def __gt__(self, other):
        if not isinstance(other, race_rec):
            return NotImplemented
        if not self.can_compare(other):
            raise TypeError(f"Cannot compare {self.get_race_type()} with {other.get_race_type()}")
        return self._score > other._score
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict['name'], data_dict['uid'], data_dict['score'], data_dict['house'])
    
    @staticmethod
    def validate_house(house):
        return house.upper() in ["PINK", "RED", "YELLOW", "BLUE"]





class race_100meter(race_rec):
    def getscore(self):
        print("your score is:", self._score, "second")
    
    def get_unit(self):
        return "second"
    
    def get_race_type(self):
        return "100m"






class race_300meter(race_rec):
    def getscore(self):
        print("your score is:", self._score, "second")
    
    def get_unit(self):
        return "second"
    
    def get_race_type(self):
        return "300m"






class race_400mrelay(race_rec):
    def __init__(self, name, uid, score, house, team):
        super().__init__(name, uid, score, house)
        self._team = team
        self._teammates = []
    
    @property
    def team(self):
        return self._team
    
    @team.setter
    def team(self, value):
        if isinstance(value, int) and value > 0:
            self._team = value
        else:
            raise ValueError("Team number must be positive")
    
    @property
    def teammates(self):
        return self._teammates
    
    def add_teammate(self, teammate):
        if isinstance(teammate, race_400mrelay) and len(self._teammates) < 3:
            self._teammates.append(teammate)
        else:
            raise ValueError("Invalid teammate or team is full")
    
    def __add__(self, other):
        if isinstance(other, race_400mrelay):
            return self._score + other._score
        elif isinstance(other, (int, float)):
            return self._score + other
        return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def get_total_team_score(self):
        total = self._score
        for teammate in self._teammates:
            total += teammate.score
        return total
    
    def getscore(self):
        print(self._score, "second")
    
    def getteam(self):
        print("you are team ", self._team)
    
    def get_unit(self):
        return "second"
    
    def get_race_type(self):
        return "4x100m_relay"





class race_longjump(race_rec):
    def __init__(self, name, uid, score, house):
        super().__init__(name, uid, score, house)
        if float(score) < 1 or float(score) > 9:
            print(f"Warning: Long jump score {score}m seems unusual. Typical range is 1-9 meters.")
    
    def getscore(self):
        print("your score is:", self._score, "m")
    
    def get_unit(self):
        return "m"
    
    def get_race_type(self):
        return "long_jump"
    
    def __eq__(self, other):
        if not isinstance(other, race_longjump):
            return NotImplemented
        if not self.can_compare(other):
            return "Cannot compare different race types"
        if self._score > other._score:
            return "you have a higher score"
        elif self._score < other._score:
            return "you have a lower score"
        else:
            return "you have an equal score"
    
    def __lt__(self, other):
        if not isinstance(other, race_longjump):
            return NotImplemented
        if not self.can_compare(other):
            raise TypeError(f"Cannot compare {self.get_race_type()} with {other.get_race_type()}")
        return self._score > other._score
    
    def __gt__(self, other):
        if not isinstance(other, race_longjump):
            return NotImplemented
        if not self.can_compare(other):
            raise TypeError(f"Cannot compare {self.get_race_type()} with {other.get_race_type()}")
        return self._score < other._score





class RaceFactory:
    @staticmethod
    def create_race(race_type, name, uid, score, house, team=None):
        race_types = {
            "100meter_run": race_100meter,
            "300meter_run": race_300meter,
            "4x100mrelay": race_400mrelay,
            "longjump": race_longjump
        }
        
        race_class = race_types.get(race_type)
        if race_class:
            if race_type == "4x100mrelay" and team is not None:
                return race_class(name, uid, score, house, team)
            elif race_type != "4x100mrelay":
                return race_class(name, uid, score, house)
        raise ValueError(f"Unknown race type: {race_type}")





def register():
    while True:
        new_name = input("please enter your name/first runner in relay ")
        if not new_name.strip():
            print("Name cannot be empty")
            continue
            
        new_house = str(input("please enter your house "))
        if not race_rec.validate_house(new_house):
            print("house not found")
            continue
        
        try:
            contest = int(input("what contest did you attend? \n1.100m race\t2.300m race\t3.4x100m relay\t4.long jump\n please enter the number of the contest you attended  "))
            if contest < 1 or contest > 4:
                print("enter a valid number")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        
        try:
            new_score = float(input("please enter your score(in second or m): "))
            if new_score < 0:
                print("Score cannot be negative")
                continue
            
            if contest == 4 and (new_score < 1 or new_score >= 9):
                print("Note: Long jump scores are typically between 1-8 meters. Please ensure you entered the score in meters (m).")
                confirm = input("Is this score in meters? (y/n): ")
                if confirm.lower() != 'y':
                    print("Please re-enter the score in meters")
                    continue
                    
        except ValueError:
            print("Please enter a valid number for score")
            continue
 
        if contest == 1:
            print("Registering for 100m race...")
            return new_name, 1154, new_score, "", "", "", "", "", "", new_house.lower(), "100meter_run"

        if contest == 2:
            print("Registering for 300m race...") 
            return new_name, 2347, new_score, "", "", "", "", "", "", new_house.lower(), "300meter_run"
           
        if contest == 3:
            teammate1 = new_name
            print("please enter the name for the second runner") 
            teammate2 = input("name:")
            try:
                new_score2 = float(input("please enter your score(in seconds):"))
                if new_score2 < 0:
                    print("Score cannot be negative")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
                
            print("please enter the name for the third runner") 
            teammate3 = input("name:")
            try:
                new_score3 = float(input("please enter your score(in seconds):"))
                if new_score3 < 0:
                    print("Score cannot be negative")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
                
            print("please enter the name for the fourth runner") 
            teammate4 = input("name:")
            try:
                new_score4 = float(input("please enter your score(in seconds):"))
                if new_score4 < 0:
                    print("Score cannot be negative")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
                
            return new_name, 3062, new_score, teammate2, teammate3, teammate4, new_score2, new_score3, new_score4, new_house.lower(), "4x100mrelay"
             
        if contest == 4:
            print("Registering for long jump...") 
            print("Note: Please enter the score in METERS (m)")
            return new_name, 4199, new_score, "", "", "", "", "", "", new_house.lower(), "longjump"

def check():
    try:
            user_ID = input("Please insert your ID: ")
            if int(user_ID) != int(user.id):
                print("Non-existent UID")
            else:
                print("")
                user.getname()
                user.getid()
                user.gethouse()
                user.getscore()
                if 3000 <= int(user_ID) < 4000 and isinstance(user, race_400mrelay):
                    user.getteam()
                    if hasattr(user, 'get_total_team_score'):
                        print(f"Total team score: {user.get_total_team_score()} {user.get_unit()}")
                    print("\nTeammates:")
                    for i, teammate in enumerate(user.teammates, 1):
                        print(f"   {i}. {teammate.name} - Score: {teammate.score} {teammate.get_unit()}")
                print("")
        except ValueError:
            print("Invalid ID format. Please enter numbers only.")


def comparsion:
    try:
            user_ID = input("Please insert your ID: ")
            if int(user_ID) != int(user.id):
                print("Non-existent UID")
            else:
                # Show available participants including teammates if user is in relay
                same_race_participants = [p for p in participants_by_race.get(user.get_race_type(), []) if p.name != user.name]
                
                # If user is a relay team member, also show other relay members
                if isinstance(user, race_400mrelay) and user.teammates:
                    for teammate in user.teammates:
                        if teammate not in same_race_participants and teammate.name != user.name:
                            same_race_participants.append(teammate)
                
                if not same_race_participants:
                    print(f"\nNo other participants found in {user.get_race_type()} to compare with")
                    continue
                
                print(f"\nAvailable {user.get_race_type()} participants to compare:")
                print("-" * 50)
                for i, p in enumerate(same_race_participants, 1):
                    print(f"{i}. {p.name:15}\tScore: {p.score:6.2f} {p.get_unit():5}\tHouse: {p.house}")
                
                rival_name = input("\nPlease enter the name of the person you'd like to compare: ")
                rival = participants_dict.get(rival_name.lower())
                
                if rival:
                    if not user.can_compare(rival):
                        print(f"\nCannot compare {user.get_race_type()} with {rival.get_race_type()}!")
                        print(f"   {user.name} participates in {user.get_race_type()} ({user.score} {user.get_unit()})")
                        print(f"   {rival.name} participates in {rival.get_race_type()} ({rival.score} {rival.get_unit()})")
                        print("   You can only compare participants from the same event.")
                    else:
                        comparison_result = user.__eq__(rival)
                        print(f"\nComparison result: {comparison_result}")
                        
                        try:
                            print("")
                            print(f"{user.name} ({user.get_race_type()}): {user.score} {user.get_unit()}")
                            print(f"{rival.name} ({rival.get_race_type()}): {rival.score} {rival.get_unit()}")
                            print("")
                            
                            if user.get_race_type() == "long_jump":
                                if user.score > rival.score:
                                    print(f"WINNER: {user.name} with {user.score} {user.get_unit()}!")
                                    print(f"   {user.name} jumped {user.score - rival.score:.2f}m further than {rival.name}")
                                elif rival.score > user.score:
                                    print(f"WINNER: {rival.name} with {rival.score} {rival.get_unit()}!")
                                    print(f"   {rival.name} jumped {rival.score - user.score:.2f}m further than {user.name}")
                                else:
                                    print(f"TIE! Both athletes jumped the same distance!")
                            else:
                                if user.score < rival.score:
                                    print(f"WINNER: {user.name} with {user.score} {user.get_unit()}!")
                                    print(f"   {user.name} was {rival.score - user.score:.2f}{user.get_unit()} faster than {rival.name}")
                                elif rival.score < user.score:
                                    print(f"WINNER: {rival.name} with {rival.score} {rival.get_unit()}!")
                                    print(f"   {rival.name} was {user.score - rival.score:.2f}{rival.get_unit()} faster than {user.name}")
                                else:
                                    print(f"TIE! Both athletes finished with the same time!")
                        except TypeError as e:
                            print(f"Error: {e}")
                else:
                    print(f"Participant '{rival_name}' not found. Please check the spelling.")
        except ValueError:
            print("Invalid ID format. Please enter numbers only.")
        except Exception as e:
            print(f"Error during comparison: {e}")



try:
    muhammed = race_100meter("muhammed", 1245, 15.25, "red")
    jane = race_100meter("jane", 1787, 14.32, "blue")
    terry = race_100meter("terry", 1756, 15, "yellow")
    ken = race_100meter("ken", 1724, 15, "red")
    bob = race_100meter("bob", 1384, 15, "pink")
    alice = race_100meter("alice", 1113, 15, "red")
    priya = race_100meter("priya", 1002, 12, "blue")
    daniel = race_100meter("daniel", 1003, 10, "yellow")
    maria = race_100meter("maria", 1004, 14, "red")
    james = race_100meter("james", 1034, 13, "blue")
    chloe = race_100meter("chloe", 1006, 11, "pink")
    ethan = race_100meter("ethan", 1007, 11.21, "red")
    sophia = race_100meter("sophia", 1008, 12.67, "yellow")
    hannah = race_100meter("hannah", 1009, 13.56, "blue")



    alex = race_300meter("alex", 2578, 30.25, "red")
    ryan = race_300meter("ryan", 2384, 38, "pink")
    emily = race_300meter("emily", 2002, 37.67, "blue")
    noah = race_300meter("noah", 2003, 39.07, "yellow")
    grace = race_300meter("grace", 2004, 36.88, "red")
    jack = race_300meter("jack", 2113, 38, "red")
    olivia = race_300meter("olivia", 2034, 37.92, "blue")
    ben = race_300meter("ben", 2006, 38.33, "pink")
    sarah = race_300meter("sarah", 2007, 39.21, "red")
    david = race_300meter("david", 2008, 37.66, "yellow")
    lily = race_300meter("lily", 2009, 38.54, "blue")
    



    michael = race_400mrelay("michael", 3384, 10.20, "pink", 1)
    ava = race_400mrelay("ava", 3002, 12.32, "pink", 1)
    jason_relay = race_400mrelay("jason", 3003, 11.45, "pink", 1)
    mei_relay = race_400mrelay("mei", 3004, 11.35, "pink", 1)
    
    michael.add_teammate(ava)
    michael.add_teammate(jason_relay)
    michael.add_teammate(mei_relay)

    carlos = race_400mrelay("carlos", 3113, 11.20, "red", 2)
    anna = race_400mrelay("anna", 3034, 11.45, "red", 2)
    tom = race_400mrelay("tom", 3006, 12.32, "red", 2)
    hailee = race_400mrelay("hailee", 3007, 11.04, "red", 2)
    
    carlos.add_teammate(anna)
    carlos.add_teammate(tom)
    carlos.add_teammate(hailee)

    william = race_400mrelay("william", 3008, 11.15, "yellow", 3)
    isabella = race_400mrelay("isabella", 3009, 11.42, "yellow", 3)
    henry = race_400mrelay("henry", 3010, 11.38, "yellow", 3)
    victoria = race_400mrelay("victoria", 3011, 11.82, "yellow", 3)
    
    william.add_teammate(isabella)
    william.add_teammate(henry)
    william.add_teammate(victoria)

    oliver = race_400mrelay("oliver", 3012, 10.92, "blue", 4)
    natalie = race_400mrelay("natalie", 3013, 11.15, "blue", 4)
    samuel = race_400mrelay("samuel", 3014, 11.38, "blue", 4)
    julia = race_400mrelay("julia", 3015, 11.44, "blue", 4)
    
    oliver.add_teammate(natalie)
    oliver.add_teammate(samuel)
    oliver.add_teammate(julia)





    ted = race_longjump("ted", 4456, 4.15, "red")
    jayson = race_longjump("jayson", 4236, 6.21, "red")
    mel = race_longjump("mel", 4236, 5.87, "red")
    emi = race_longjump("emi", 4236, 6.45, "red")
    noelle = race_longjump("noelle", 4455, 5.92, "red")
    annabell = race_longjump("annabell", 4954, 6.08, "red")
    grent = race_longjump("grent", 4852, 6.33, "red")
    oscar = race_longjump("oscar", 4236, 5.12, "red")
    jet = race_longjump("jet", 4384, 4.50, "red")
    marc = race_longjump("marc", 4002, 4.78, "pink")
    marcus = race_longjump("marcus", 4003, 5.20, "blue")
    kyle = race_longjump("kyle", 4004, 5.03, "pink")
    mac = race_longjump("mac", 4113, 4.98, "red")
    avis = race_longjump("avis", 4034, 5.40, "yellow")
    isaac = race_longjump("isaac", 4006, 5.27, "red")
    summer = race_longjump("summer", 4007, 5.84, "blue")
    autumn = race_longjump("autumn", 4008, 5.98, "yellow")
    samantha = race_longjump("samantha", 4009, 4.99, "yellow")
    


except (ValueError, TypeError) as e:
    print(f"Error creating participants: {e}")
    exit(1)


participants_dict = {}
participants_by_race = {
    "100m": [],
    "300m": [],
    "4x100m_relay": [],
    "long_jump": []
}




for participant in [muhammed, jane, terry, ken, bob, alice, priya, daniel, maria, james, chloe, ethan, sophia, hannah,
                   alex, ryan, emily, noah, grace, jack, olivia, ben, sarah, david, lily,
                   michael, ava, jason_relay, mei_relay, carlos, anna, tom, hailee,
                   william, isabella, henry, victoria, oliver, natalie, samuel, julia,
                   ted, jayson, mel, emi, noelle, annabell, grent, oscar, jet,
                   marc, marcus, kyle, mac, avis, isaac, summer, autumn, samantha]:
    participants_dict[participant.name.lower()] = participant
    race_type = participant.get_race_type()
    if race_type in participants_by_race:
        participants_by_race[race_type].append(participant)




print("LEADERBOARD MANAGEMENT SYSTEM")
print("")




logout = False
user = race_100meter("default", 1000, 22, "red")
print(f"Sample athlete: {user.name} (ID: {user.id}, Score: {user.score} {user.get_unit()}, House: {user.house})")



while logout == False:
    print("\nwhat would you like to do?")
    print("1. Record new score")
    print("2. Check your score")
    print("3. Compare scores")
    print("4. Exit")
    choice = input("\nEnter your choice (1-4): ")
    



    if choice == "1":
        try:
            result = register()
            new_name, new_id, new_score, t2, t3, t4, s2, s3, s4, new_house, match = result
            
            if match == "4x100mrelay":
                user = RaceFactory.create_race(match, new_name, new_id, new_score, new_house, 5)
                
                # Create individual runner objects and add them as teammates
                runner1 = race_400mrelay(new_name, new_id, new_score, new_house, 5)
                
                if t2 and s2:
                    runner2 = race_400mrelay(t2, 3129, s2, new_house, 5)
                    user.add_teammate(runner2)
                    participants_dict[t2.lower()] = runner2
                    participants_by_race["4x100m_relay"].append(runner2)
                    
                if t3 and s3:
                    runner3 = race_400mrelay(t3, 3650, s3, new_house, 5)
                    user.add_teammate(runner3)
                    participants_dict[t3.lower()] = runner3
                    participants_by_race["4x100m_relay"].append(runner3)
                    
                if t4 and s4:
                    runner4 = race_400mrelay(t4, 3992, s4, new_house, 5)
                    user.add_teammate(runner4)
                    participants_dict[t4.lower()] = runner4
                    participants_by_race["4x100m_relay"].append(runner4)
                    
                print("\nRelay team registered successfully!")
                print(f"   Team members: {new_name}, {t2}, {t3}, {t4}")
                print(f"   Individual scores: {new_score}s, {s2}s, {s3}s, {s4}s")
            else:
                user = RaceFactory.create_race(match, new_name, new_id, new_score, new_house)
            
            print(f"\nRegistration complete!")
            print(f"   Name: {user.name}")
            print(f"   your ID is: {user.id}")
            print(f"   Event: {user.get_race_type()}")
            print(f"   Score: {user.score} {user.get_unit()}")
            print(f"   House: {user.house}")
            print("\nPlease remember your ID for future reference!")
            
            participants_dict[user.name.lower()] = user
            participants_by_race[user.get_race_type()].append(user)
            
        except (ValueError, TypeError) as e:
            print(f"\nError during registration: {e}")
            continue
    



    elif choice == "2":
        check()
    



    elif choice == "3":
        comparison()
    


    elif choice == "4":
        logout = True
        print("exiting")
    


    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4")
