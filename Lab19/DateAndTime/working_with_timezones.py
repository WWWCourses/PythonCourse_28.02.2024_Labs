from datetime import datetime
import pytz
from zoneinfo import ZoneInfo

# # Get local current time:
# current = datetime.now()

# # Get the timezone object for New York and London
# tz_NY = pytz.timezone('America/New_York')
# tz_London = pytz.timezone('Europe/London')

# # Get the current time in New York
# current_NY = datetime.now(tz_NY)
# # Get the current time in London
# current_London = datetime.now(tz_London)

# # Format the times as a string and print it
# print("Local time:", current.strftime("%H:%M:%S"))
# print("NY time:", current_NY.strftime("%H:%M:%S"))
# print("London time:", current_London.strftime("%H:%M:%S"))



# # TASK: show time in London for 09.05.2024, 12:00:00 BG time
# tz_London = ZoneInfo('Europe/London')
# tz_Sofia = ZoneInfo('Europe/Sofia')

# sofia_datetime = datetime(2024, 5, 9, 12, 0, 0, tzinfo=tz_Sofia)
# print(sofia_datetime)

# london_datetime = sofia_datetime.astimezone(tz_London)
# print(london_datetime)
