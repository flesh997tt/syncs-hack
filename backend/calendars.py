from ics import Calendar
import requests

class Calendars:
    def __init__(self, url):
        # self.ics_path = Path(filename)
        # with self.ics_path.open() as f:
        #     self.calendar = icalendar.Calendar.from_ical(f.read())
        self.url = url

    
    def is_busy(self):
        cal = Calendar(requests.get(self.url).text)
        timetable = cal.timeline
        current_events = timetable.now()
        for event in current_events:
            return True
        return False