class Time(object):
    """Represents the time of day.

    attributes: hour,minute,second
    """

def print_time(time):
    '''Prints the tiem in hour:minute:second format.

    time: Time object

    return: none
    '''
    print "%d:%.2d:%.2d" %(time.hour, time.minute,time.second)

def is_after(t1,t2):
    '''Returns true if t1 is later than t2, false otherwise.

    t1,t2: Time object

    return: none
    '''
    n1 = t1.hour+t1.minute/60.0+t1.second/3600.0
    n2 = t2.hour+t2.minute/60.0+t2.second/3600.0
    return n1>n2


if __name__ == '__main__':
    time1 = Time()
    time1.hour = 2
    time1.minute=34
    time1.second = 3

    time2 = Time()
    time2.hour = 1
    time2.minute = 34
    time2.second = 2

    print is_after(time1,time2)