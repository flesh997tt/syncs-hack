from person import Person

class backend:
    def __init__(self, filename: str):
        self.filename = filename
    
    def parsecalendar(self):
        fobj = open(self.filename)
        rows = fobj.readlines()
        self.people = []
        for row in rows:
            self.people.append(Person(row))
    