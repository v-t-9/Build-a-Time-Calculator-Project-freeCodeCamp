def add_time(start, duration, start_week = ""):

    time = { "13": "1", "14": "2", "15": "3", "16": "4", "17": "5", "18": "6", 
            "19": "7", "20": "8", "21": "9", "22": "10", "23": "11" ,
            "00": "12", "12":"12" }
    weeks = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_time = ""
    days = 0
    
    if duration == "0:00":
        return start
    duration_hours = int(duration[:duration.find(":")])
    duration_min = int(duration[duration.find(":")+1:])
    start_hours = int(start[:start.find(":")])
    start_min = int(start[start.find(":")+1:start.find(":")+3]) 
    
    while duration_hours >= 24:
        days += 1
        duration_hours -= 24
   
    
    minutes = start_min + duration_min
    total_hours = start_hours + duration_hours
  

    if total_hours < 12:
        if "AM" in start:
            new_time = f"{str(total_hours)}:{minutes} AM"
        else:
            new_time = f"{str(total_hours)}:{minutes} PM"
  
    if  minutes > 60:
        total_hours += 1
        minutes -= 60
    minutes = str(minutes)
    if len(minutes) == 1:
        minutes = "0" + minutes
    

    if total_hours >= 12:
        new_time = f"{time[str(total_hours)]}:{minutes}"
        if "AM" in start:
            new_time += " PM"
        else:
            new_time += " AM"
   
 


    #calculate weeks
    days2 = days
    if days > 7:
        week = days
       
        while week >7:
            week = week / 7
        days = week - int(week)
        days = int(days*7)
        week = int(week)
      
    duration_hours = int(duration[:duration.find(":")])
    start_hours = int(start[:start.find(":")])
    
    if start_week != "":
        day_ind = weeks.index(start_week.capitalize())
        res_w = weeks[day_ind:] + weeks[:day_ind]
        day_res = res_w[days]
        if "AM" in start and ( int(start_hours + duration_hours) >= 24 and int(start_hours + duration_hours< 48)):
            new_time += f", {day_res} (next day)"
        elif ("PM" in start and "AM" in new_time) and total_hours >= 12:
            day_res = res_w[days +1 ]
            new_time += f", {day_res} ({days2+1} days later)"

        else:
            new_time += f", {start_week}"
    else:
       
     
        if "AM" in start and ( int(start_hours + duration_hours) >= 24 and int(start_hours + duration_hours< 48)):
            new_time += f" (next day)"
        elif "PM" in start and int(start_hours + duration_hours) >=12 and int(start_hours + duration_hours) <24:
            new_time += f" (next day)"
        elif ("PM" in start and "AM" in new_time) and total_hours >= 12:
            new_time += f" ({days2+1} days later)"
        elif "AM" in start and total_hours >24:
            new_time += f" ({days2} days later)"
       


    return new_time

if __name__ == "__main__":
    

    print(add_time('3:00 PM', '3:10'))
    # # Returns: 6:10 PM

    print(add_time('11:30 AM', '2:32', 'Monday'))
    # # Returns: 2:02 PM, Monday

    print(add_time('11:43 AM', '00:20'))
    # # # Returns: 12:03 PM

    print(add_time('10:10 PM', '3:30'))
    # # # Returns: 1:40 AM (next day)

    print(add_time('11:43 PM', '24:20', 'tueSday'))
    # # # Returns: 12:03 AM, Thursday (2 days later)

    print(add_time('6:30 PM', '205:12'))
    # # Returns: 7:42 AM (9 days later)

    print(add_time('2:59 AM', '24:00', 'saturDay'))
    # 2:59 AM, Sunday (next day)'

    print(add_time('11:59 PM', '24:05', 'Wednesday'))
    # '12:04 AM, Friday (2 days later)'

    print(add_time('8:16 PM', '466:02', 'tuesday'))
    # '6:18 AM, Monday (20 days later)'

    #8. Expected adding 0:00 to return the initial time.

    print(add_time('2:59 AM', '24:00'))
    # '2:59 AM (next day)'
