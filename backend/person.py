from calendar import Calendars

class Person:
    def __init__(self, data):
        clean_data = data.split(',')
        self.name = clean_data[0]
        self.username = clean_data[1]
        self.password = clean_data[2]
        self.calendar = Calendars(clean_data[3])

    def is_busy(self):
        return self.calendar.is_busy()