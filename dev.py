import datetime
import time
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Endri angali endri!")
            break
        time.sleep(1)
alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
set_alarm(alarm_time)
