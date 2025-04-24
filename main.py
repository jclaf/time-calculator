def add_time(start, duration, day=None):
    # Liste des jours pour l'indexation
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_hour = int(start.split(" ")[0].split(":")[0])
    start_minute = int(start.split(" ")[0].split(":")[1])
    start_format = start.split(" ")[1]

    print("test start: ",start_hour,start_minute,start_format)
    
    # Convert start time to 24-hour format for easier calculation
    if start_format == "PM" and start_hour != 12:
        start_hour += 12
    if start_format == "AM" and start_hour == 12:
        start_hour = 0

    duration_hour = int(duration.split(" ")[0].split(":")[0])
    duration_minute = int(duration.split(" ")[0].split(":")[1])
    
    print("test duration: ", duration_hour, duration_minute)
    
    # check if minute more than 60 and convert to hour if minute > 60
    new_time_minute = start_minute + duration_minute
    if new_time_minute >= 60:
        new_time_minute-=60
        start_hour +=1
    
    countHours = (start_hour+duration_hour)%12
    countDay = (start_hour+duration_hour)//24
    remaining = (start_hour+duration_hour)%24

    # new_time_hour = countHours if countHours!=0 else 12
    # new_time_format = "PM" if remaining>=12 else start_format

    # Conversion en format 12h
    if remaining == 0:
        new_time_hour = 12
        new_time_format = "AM"
    elif 1 <= remaining < 12:
        new_time_hour = remaining
        new_time_format = "AM"
    elif remaining == 12:
        new_time_hour = 12
        new_time_format = "PM"
    else:  # remaining > 12
        new_time_hour = remaining - 12
        new_time_format = "PM"    

    if day:
        day_index = week.index(day.capitalize())
        new_index = (day_index+countDay)%7
        new_day_name = week[new_index]
        day_name = f', {new_day_name}'
    else:
        day_name = ''

    if countDay == 0 :
        new_day = ''
    elif countDay == 1:
        new_day = f' (next day)'
    else:
        new_day = f' ({countDay} days later)'

    print("test new time :", new_time_hour, new_time_minute,new_time_format)
    
    new_time = f"{new_time_hour}:{new_time_minute:02d} {new_time_format}{day_name}{new_day}"
    
    print(new_time)
    return new_time


if __name__ == "__main__":
    add_time('8:16 PM', '466:02')
