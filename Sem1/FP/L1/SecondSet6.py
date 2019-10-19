def isLeapYear(year):
    return (int(year)%4 == 0 and int(year)%100 != 0) or int(year)%400 == 0

def numberToDate(nr,year):
    months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days=[31]
    if isLeapYear(year):
        days.append(29)
    else:
        days.append(28)
    days=days+[31,30,31,30,31,31,30,31,30,31]
    for i in range(1,len(days)):
        days[i]=days[i-1]+days[i]
    if nr <= 31:
        return str(nr) + ' ' + months[0]
    else:
        i = 0
        while(nr > days[i]):
            i+=1
        return (str(nr-days[i-1]) + ' ' +months[i])
    
year=int(input('Give a year:'))
nr=int(input('Give a day number:'))
print('Your date is: ' + numberToDate(nr,year) + ' ' + str(year))
