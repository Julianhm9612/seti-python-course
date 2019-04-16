# own modules
import mMath
from mMath import substract

mMath.sum(1, 2)
substract(3, 1)

# third party modules
# pip https://pypi.org/
# pip install colorama
from colorama import Fore, Style, init

init(convert=True)
print(Fore.RED + 'Hello World!' + Style.RESET_ALL)

# python modules
import datetime
from datetime import timedelta, date

print(datetime.date.today())
print(timedelta(minutes=70)) # minutes to hours
print(date.today())