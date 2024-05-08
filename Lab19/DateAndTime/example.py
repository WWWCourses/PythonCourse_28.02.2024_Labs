from datetime import datetime

# TASK: print today day as weekday name
now = datetime.now()
# print(now.strftime('%A'))
print(now.weekday())