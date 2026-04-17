from classes import race_rec
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

