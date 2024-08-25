from calendars import Calendars

class Person:
    def __init__(self, data):
        clean_data = data.strip('\n').split(',')
        self.name = clean_data[0]
        self.username = clean_data[1]
        self.password = clean_data[2]
        if len(clean_data) > 3 and clean_data[3] != "None":
            self.calendar = Calendars(clean_data[3])
        else:
            self.calendar = None
        if len(clean_data) > 4:
            self.friends = clean_data[4:]
        else:
            self.friends = []

    def fix_people(self, all_people):
        for person in all_people:
            if person.get_username() in self.friends:
                self.friends[self.friends.index(person.get_username())] = person

    def is_busy(self):
        return self.calendar.is_busy()
    
    def online_friends(self):
        ls = []
        for friend in self.friends:
            ls.append((friend.get_name(), not friend.is_busy()))
        return ls
    
    def format(self):
        string = self.name 
        string += ","
        string += self.username 
        string += ","
        string += self.password
        string += ","
        if self.calendar is not None:
            string += self.calendar.url
        else:
            string += "None"
        for friend in self.friends:
            string += ","
            string += friend
        return string

    def change_ics(self, url):
        self.calendar = Calendars(url)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.name = username

    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
    
    def check_password(self, password):
        return password == self.password
    
    def is_friend(self, username):
        return username in self.friends
    
    def get_friends(self):
        return self.friends

    def is_friend(self, friend):
        for person in self.friends:
            if friend == person:
                return True
        return False

    def add_friend(self, friend):
        if self.is_friend(friend):
            return False
        self.friends.append(friend)
        return True

    def __eq__(self, other):
        return self.username == other.username