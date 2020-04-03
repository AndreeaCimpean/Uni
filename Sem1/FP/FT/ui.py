import datetime

s = "21.02"
format = "%d.%m"
d = datetime.datetime.strptime(s, format)
print(d)