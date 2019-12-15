# ***************************************************
#           Copyright by Bartłomiej Piekarz
#                         2019
# ***************************************************
#
# Theese functions are used to read and filter a text file

import time


class FileReader:

    accident_string = ''
    nick_string = ''

    log_location = ''

    audio_accident = ''
    audio_mention = ''

    event_accident = 'accident'
    event_mention = 'shoutout'

    def read_lines(self, file):
        file.seek(0, 2)
        try:
            line = file.readline()
            if not line or (self.nick_string + ":" in line):
                time.sleep(0.01)
            elif self.accident_string in line:
                yield self.event_accident
            elif self.nick_string.lower() in line.lower():
                yield self.event_mention
        except Exception as e:
            print('ERROR - ' + str(e))
