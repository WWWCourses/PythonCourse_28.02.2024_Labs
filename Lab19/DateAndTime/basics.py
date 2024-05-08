# import datetime

# now = datetime.datetime.now()
# print(type(now))


# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# microsecond = now.microsecond

# print("Year:", year)
# print("Month:", month)
# print("Day:", day)
# print("Hour:", hour)
# print("Minute:", minute)
# print("Second:", second)
# print("Microsecond:", microsecond)

# -------------------------------- strftime() -------------------------------- #
import datetime

# now = datetime.datetime.now()
# formated_now_string = now.strftime('%d.%m.%Y; %H:%M:%S')
# print(formated_now_string) # 'DD.MM.YYYY' (08.05.2024)


# # TASK: calculate user age, given his birthdate
# birthday_string = '08.05.1990'
# birtdate1 = datetime.datetime.strptime(birthday_string, '%d.%m.%Y')
# birtdate2 = datetime.datetime(year=1990,month=5,day=8)

# current_year =  datetime.datetime.now().year
# print(f'User age is: {current_year - birtdate1.year}')


# --------------------------------- timedelta -------------------------------- #
# import datetime

# birtdate = datetime.datetime.strptime('08.05.1990', '%d.%m.%Y')
# now = datetime.datetime.now()
# td = now - birtdate
# print(type(td))
# print(td.days)