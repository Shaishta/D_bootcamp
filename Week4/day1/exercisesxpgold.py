#Exercises XP Gold
#Exercise 1 : Hello World-I Love Python
#print("Hello World\n"*4 + "I love python\n"*4)

#Exercise 2 : What Is The Season ?
month = input("Input the month: ")
day = int(input("Input the day: "))

if month in ('December', 'January', 'February'):
	season = 'winter'
elif month in ('March', 'April', 'May'):
	season = 'spring'
elif month in ('June', 'July', 'August'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 3):
	season = 'spring'
elif (month == 'June') and (day > 6):
	season = 'summer'
elif (month == 'September') and (day > 9):
	season = 'autumn'
elif (month == 'December') and (day > 12):
	season = 'winter'

print("Season is",season)
