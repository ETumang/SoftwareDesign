import datetime

def print_weekday():
    '''Prints the current day of the week.

    return: none
    '''

    i = datetime.date.today().weekday()
    if (i ==0):
        print "Monday"
    elif(i==1):
        print "Tuesday"
    elif(i==2):
        print "Wednesday"
    elif(i==3):
        print "Thursday"
    elif(i==4):
        print "Friday"
    elif(i==5):
        print "Saturday"
    elif(i==6):
        print "Sunday"


def time_until_birthday(birthday):
    '''Prints the age of a person with birthday birthday, and the number of days until their next birthday.

    birthday: Date object
    return: none
    '''

    today = datetime.date.today()
    d = today-birthday
    years = d.days/365
    months = (d.days%365)/30
    days = (d.days%365)%30
    print "You are %d years, %d months, and %d days old." %(years,months,days)

    next = birthday.replace(year= today.year)

    diff = next-today
    if diff.days <0:
        next = next.replace(year = next.year+1)
        diff = next-today

    print "It will be %d months and %d days until your next birthday." %(diff.days/31, diff.days%31)


def double_day(birthday1,birthday2):
    '''
    Calculates the day upon which two people with birthdays birthday1 and birthday2 will be 1/2 and twice each other's ages.

    birthday1, birthday2: Date object
    return: Date object
    '''

    if birthday1>birthday2:
        double_day = birthday1+(birthday1-birthday2)
    else:
        double_day = birthday2+ (birthday2-birthday1)

    return double_day



if __name__ == "__main__":

   b = datetime.date(1996,12,22)
   
   b2 = datetime.date(1946,12,17)

   print (double_day(b,b2))
 
 