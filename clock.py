import os
import datetime
import time

def center_output(text: str) -> str:
    text_lines = text.split('\n')
    output_lines = []

    terminal_width  = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines
    lines_printed = len(text_lines)
    vertical_centering = (terminal_height - lines_printed) // 2 - 1

    output_lines.append("\n"*vertical_centering)

    for line in text_lines:
        output_lines.append(line.center(terminal_width))

    output = "\n".join(output_lines)

    return output



def update_years():
    birth_date = datetime.datetime(2005, 12, 15, 15, 15)
    date_now = datetime.datetime.now()

    time_passed = date_now - birth_date
    seconds_passed = time_passed.total_seconds()

    years_passed        = str(int( seconds_passed / 60 / 60 / 24 / 365 )).rjust(2)
    days_passed         = str(int( seconds_passed / 60 / 60 / 24 % 365 )).rjust(3)
    hours_passed        = str(int( seconds_passed / 60 / 60      % 24  )).rjust(2)
    minutes_passed      = str(int( seconds_passed / 60           % 60  )).rjust(2)
    milliseconds_passed = str(int( seconds_passed % 60 * 1000    % 1000)).rjust(3)
    seconds_passed      = str(int( seconds_passed % 60                 )).rjust(2)


    os.system("clear")

    text = f"""{years_passed} years
{days_passed} days
{hours_passed} hours
{minutes_passed} minutes
{seconds_passed} seconds
{milliseconds_passed} milliseconds
have passed in your life."""

    output_text = center_output(text)
    print(output_text)

if __name__ == "__main__":
    while True:
        update_years()
        time.sleep(0.01)