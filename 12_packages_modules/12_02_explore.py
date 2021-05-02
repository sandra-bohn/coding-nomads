'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''

from datetime import datetime, date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)
print(date.today())