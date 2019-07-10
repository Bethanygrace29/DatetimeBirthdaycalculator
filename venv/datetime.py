
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime

t = timedelta(days=365)
today = datetime.date.today()  # type: date

time = str(t.today - t.birthday)


def daystobday(string, name):
    print("What is your name?")
    name = input([string])
    input(string(name))
    print("When is your birthday in 4 digits")
    print (name, 'Your birthday is in', time, 'days')

    return daystobday()
