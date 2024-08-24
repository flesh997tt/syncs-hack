from person import Person

class Backend:
    def __init__(self, filename: str):
        self.filename = filename
    
    def parse_file(self):
        fobj = open(self.filename)
        rows = fobj.readlines()
        self.people = []
        for row in rows:
            self.people.append(Person(row))
        for person in self.people:
            person.fix_people(self.people)
        fobj.close()

    def save_file(self):
        fobj = open(self.filename, "w")
        for person in self.people:
            print(person.format(),file=fobj)
        fobj.close()

    def add_user(self, name, username, password):
        for person in self.people:
            if username == person.get_username():
                return False
        self.people.append(Person(name + "," + username + "," + password))
        self.save_file()
        return True
    
    def get_people(self):
        return self.people
    
    def find_username(self, username):
        for i in range(len(self.people)):
            if self.people[i].get_username() == username:
                return self.people[i]
        return None

    def login_checker(self, username, password):
        for person in self.people:
            if username == person.get_username():
                if person.check_password(password):
                    return True
                else:
                    return False
        return False