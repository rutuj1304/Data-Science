from datetime import date
from datetime import datetime
from datetime import time

today = date.today()
print("Todays Date: ",today)

today = date.today()

#dd/mm/yy
d1 = today.strftime("%d/%m/%y")
print("Today's Date: ",d1)

#text month,day,year
d2 = today.strftime("%B %d,%Y")
print("Today's Date: ",d2)

# mm / dd / yy
d3 = today.strftime("%m/%d/%y")
print("Today's Date: ",d3)

now = datetime.now()
print("Current Time: ",now)

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time => ",dt_string)

