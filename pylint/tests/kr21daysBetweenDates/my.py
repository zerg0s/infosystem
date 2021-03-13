from datetime import datetime

dates = []
formattedates = []
for i in range(2):
    x = input()
    dates.append(x)

format_string = '%m-%d-%Y'

for x in dates:
    formatteddate = datetime.strptime(x, format_string)
    formattedates.append(formatteddate)

if formattedates[1]>=formattedates[0]:
    print((formattedates[1]-formattedates[0]).days)
else:
    print('-1')