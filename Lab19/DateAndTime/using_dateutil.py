from datetime import datetime
from dateutil.relativedelta import relativedelta

# User's birthdate
date1 = datetime(year=2000, month=1, day=30)
date2 = datetime(year=2010, month=5, day=29)


# Calculate the age difference in years, days, and minutes
date_difference = relativedelta(date2, date1)
print(date_difference)

print(date_difference.years)
print(date_difference.months)
print(date_difference.days)

