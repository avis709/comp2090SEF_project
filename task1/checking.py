from classes import race_rec, race_100meter, race_300meter, race_400mrelay, race_longjump, RaceFactory
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
                    print("\nTeammates:")
                    for i, teammate in enumerate(user.teammates, 1):
                        print(f"   {i}. {teammate.name} - Score: {teammate.score} {teammate.get_unit()}")
                print("")
        except ValueError:
            print("Invalid ID format. Please enter numbers only.")
