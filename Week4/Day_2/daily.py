#Daily Challenge: Happy Birthday
import datetime

from datetime import datetime
"""taking input from user and converting it to datetime object"""

birthday = input("What is your Date of Birth? ex. dd/mm/yyyy")
birthday_convert_to_date = datetime.strptime(birthday, "%d/%m/%Y")
"""specifying the current date"""
current_date = datetime.now()
"""age"""
age = int(current_date.year - birthday_convert_to_date.year)
age_to_string = str(age)
last_digit_age = int(age_to_string[-1])
candles = 'i' * last_digit_age

cake = f'''  ___{candles}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~'''
print(cake)

if birthday_convert_to_date.year % 4 == 0:
    print(cake * 2)
