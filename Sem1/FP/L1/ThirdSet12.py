def isLeapYear(y):
    '''
    Check if the given year is a leap year
    params:
        y-the given year
    output
        True - if y is leap
        False - if y is not leap
    '''
    return (int(y)%4 == 0 and int(y)%100 != 0) or y%400 == 0

def countLeapYears(year1,year2):
    '''
    Counts the leap years between two years
    params:
        year1-the first year
        year2-the second year
    output
        leap years between year1 and year2(without counting them)
    '''
    count=0
    for i in range(year1+1,year2):
        if isLeapYear(i):
            count+=1
    return count

def monthDays(y):
    '''
    The number of days in every month, depending on year
    params:
        y-year given
    output
        a list with the days of every month
    '''
    if isLeapYear(y):
        return [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        return [31,28,31,30,31,30,31,31,30,31,30,31]

def toDays(date1,date2):

    '''
    The days between two dates
    params:
        date1-the first date
        date2-the second date
    output
        the number of days between two dates
    '''
    #add the years between dates
    x=countLeapYears(date1['year'],date2['year'])
    days=x*366+(date2['year']-date1['year']-x-1)*365

    #add days from the birth year
    months=monthDays(date1['year'])
    days+=months[date1['month']-1]-date1['day']+1 #add days from the birth month
    for i in range(date1['month'],12):            #add days from the remaining months
        days+=months[i]

    #add days from the current year
    months=monthDays(date2['year'])     
    days+=date2['day']                      #add days from current month
    for i in range(0,date2['month']-1):     #add days from the previous months of the current year
        days+=months[i]
    return days

l=input('Give your date of birth (day/month/year): ').split("/")
date1={'year':int(l[2]),'month':int(l[1]),'day':int(l[0])}
l=input('Give current date (day/month/year): ').split("/")
date2={'year':int(l[2]),'month':int(l[1]),'day':int(l[0])}

print('Your age in days is: ' + str(toDays(date1,date2)))
