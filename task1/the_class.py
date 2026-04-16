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
