import datetime
from datetime import datetime, timedelta, time

appointments = [(datetime(2017, 9, 7, 9, 30), 
           datetime(2017, 9, 7, 12, 30)), 
           (datetime(2017, 9, 7, 13, 30), 
           datetime(2017, 9, 7, 14, 0))]

hours = (datetime(2017, 9, 7, 9, 0), datetime(2017, 9, 7, 17, 0))


def get_slots(hours, appointments, duration=timedelta(hours=1)):
    """A function to get available timeslot after deducting the appointment time
    
    Arguments:
        hours tuple -- (range_start_time, range_end_time)
        appointments List(tuple) -- reserved appointments
    
    Keyword Arguments:
        duration {[type]} -- [description] (default: {timedelta(hours=1)})
    
    Returns:
        List[object] -- available timeslot 
    """
    time_slot_list = []
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
        assert start <= end, "Cannot attend all appointments"
        while start + duration <= end:
            time_slot_list.append({"start": start, "end": duration+start})
            start += duration

    return time_slot_list

def check_time_in_range(start, end, target_start, target_end):
    """Return true if x is in the range [start, end]"""
    if start <= target_start <= target_end <= end:
        return True
    return False

def check_crashing_time(timeslot_list, target_start, target_end):
    timeslot_list = concat_timeslot(timeslot_list)
    for i in range(len(timeslot_list)):
        timeslot = timeslot_list[i]
        start = timeslot['start'].time()
        end = timeslot['end'].time()
        if check_time_in_range(start, end, target_start, target_end) is True:
            return False
    return True

def combine_formatted_date_time(target_time, date):
    formatted_time = get_format_time(target_time)
    date = datetime.strptime(date, '%Y-%m-%d').date()
    result = (datetime.combine(date,formatted_time))    
    return result

def get_working_hours(target_date):
    current_date = target_date
    start = datetime.strptime('0900','%H%M').time()
    end = datetime.strptime('1700','%H%M').time()
    return (datetime.combine(current_date, start), datetime.combine(current_date, end))      

def get_format_time(target_time):
    split_time = target_time.split(':')
    return time(int(split_time[0]),int(split_time[1]))

def concat_timeslot(timeslot_list):
    concat_timeslot_list = []
    for i in range(len(timeslot_list)):
        timeslot = timeslot_list[i]
        start = timeslot['start']
        end = timeslot['end']
        j = i+1 
        for j in range(len(timeslot_list)):
            next_timeslot = timeslot_list[j]
            next_timeslot_start = next_timeslot['start']
            next_timeslot_end = next_timeslot['end']
            if end == next_timeslot_start:
                end = next_timeslot_end
                i = i+1
        if i != len(timeslot_list):
            concat_timeslot_list.append({"start": start, "end": end})
            
    return concat_timeslot_list