# ***************************************************
#           Copyright by Bartłomiej Piekarz
#                         2019
# ***************************************************
#
# Theese functions are used to read and filter a text file

import time
from playsound import playsound


accident_string = "Nowy raport - autor"
nick_string = "Revzik"

log_location = "D:\\Games\\MTA\\MTA\\logs\\console.log"

audio_accident = "audio\\accident.wav"
audio_shoutout = "audio\\shoutout.wav"

event_accident = "accident"
event_shoutout = "shoutout"


def read_lines(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line or (nick_string + ":" in line):
            time.sleep(0.01)
            continue
        elif accident_string in line:
            yield event_accident
        elif nick_string.lower() in line.lower():
            yield event_shoutout


def play_sound(path):
    playsound(path)


if __name__ == '__main__':
    logfile = open(log_location, "r")
    events = read_lines(logfile)
    for event in events:
        print(event)
        if event == event_accident:
            play_sound(audio_accident)
        elif event == event_shoutout:
            play_sound(audio_shoutout)
