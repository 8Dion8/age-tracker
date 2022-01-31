import os
import datetime
import time
import sys


#hours_passed = time_passed.hours
#minutes_passed = time_passed.minutes
#seconds_passed = time_passed.seconds




def update_years():
    birth_date = datetime.datetime(2005, 12, 15)#, 12, 15)
    date_now = datetime.datetime.now()

    time_passed = date_now - birth_date


    seconds_passed = time_passed.total_seconds()
    years_passed = int(seconds_passed/60/60/24/365)
    days_passed = int((seconds_passed/60/60/24)%365)
    hours_passed = int(days_passed%24)
    minutes_passed = int(seconds_passed/60%60)
    milliseconds_passed = str(int(seconds_passed%60*1000%1000)).zfill(3)
    seconds_passed = int(seconds_passed%60)
    
    terminal_width  = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines
    lines_printed = 7
    vertical_centering = (terminal_height - lines_printed) // 2

    os.system("clear")
    print("\n"*vertical_centering)
    print(f"{years_passed} years".center(terminal_width))
    print(f"{days_passed} days".center(terminal_width))
    print(f"{hours_passed} hours".center(terminal_width))
    print(f"{minutes_passed} minutes".center(terminal_width))
    print(f"{seconds_passed} seconds".center(terminal_width))
    print(f"{milliseconds_passed} milliseconds".center(terminal_width))
    print("...have passed in your life.".center(terminal_width))

if __name__ == "__main__":
    while True:
        update_years()
        time.sleep(0.01)