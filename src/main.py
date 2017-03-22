from icalendar import Calendar, Event
import datetime
from pytz import UTC # timezone
import dateutil.parser # Hacky format guesser, returning datetime objects

import scheduler



"""
Assumptions:
Duration is in minutes
"""
def iCal_from_times_list(times_list, project_name, duration, priority=5):
    cal = Calendar()
    cal.add('prodid', 'cranki')
    cal.add('version', '0.1')
    for count,time in enumerate(times_list):
        event = Event()
        event.add('summary', project_name)
        event.add('dtstart', dateutil.parser(time))
        event.add('dtend', dateutil.parser.parse(time) + datetime.timedelta(0,0,0,0,60))
        event.add('dtstamp', datetime.datetime.now())
        event['uid'] = dateutil.parser(time).isoformat() + '@' + project_name + '/cranki'
        event.add('priority', priority)
        cal.add_component(event) 

    f = open('schedule.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
