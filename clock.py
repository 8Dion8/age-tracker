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
    

    os.system("clear")
    print(f"{years_passed} years\n{days_passed} days\n{hours_passed} hours\n{minutes_passed} minutes\n{seconds_passed} seconds\n{milliseconds_passed} milliseconds \n...have passed in your life.")

if __name__ == "__main__":
    while True:
        update_years()
        time.sleep(0.01)