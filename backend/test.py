from calendars import Calendars

cal1 = Calendars("https://timetable.sydney.edu.au/even/rest/calendar/ical/3ae555b9-f109-407a-bc8b-c63a7b5547f5")

print(cal1.is_busy())