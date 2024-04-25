import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    start_date = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted_date = start_date + datetime.timedelta(days=days, seconds=seconds)
    shifted_day = shifted_date.day
    shifted_second = shifted_date.second
    
    return (shifted_day, shifted_second)

print(shift_time(days, seconds))