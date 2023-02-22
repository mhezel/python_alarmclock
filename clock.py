from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[2H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #integer division
        seconds_left = time_left % 60 #remainder

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")


minutes = int(input("How many minutes: "))
seconds = int(input("How many seconds: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)

