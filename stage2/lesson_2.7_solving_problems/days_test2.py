

def is_leap_year(year):
    # if (year is not divisible by 4) then (it is a common year)
    # else if (year is not divisible by 100) then (it is a leap year)
    # else if (year is not divisible by 400) then (it is a common year)
    # else (it is a leap year)

    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_per_month[1] = 29
    days = days_per_month[month-1]
    return days

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""

    num_days = days_in_month(year, month)

    if day < num_days:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def increment_date(yn, mn, dn, yt, mt, dt):
    if yn < yt:
        return True
    elif yn == yt and mn < mt:
        return True
    elif yn == yt and mn == mt and dn < dt:
        return True
    else:
        return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):

    assert not increment_date(y2, m2, d2, y1, m1, d1)


    yn, mn, dn = (y1, m1, d1)
    days = 0
    while increment_date(yn, mn, dn, y2, m2, d2):
        days += 1
        yn, mn, dn = nextDay(yn, mn, dn)
    return days


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 366),
                  ((2012, 9, 1, 2012, 9, 4), 3)]
    print("#########################")
    print("### Testing daysBetweenDates")
    print("#########################")
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed: expected: "+str(answer)+" received: "+str(result))
        else:
            print("Test case passed!")
    print("")

def test_increment():
    test_cases = [((2012, 9, 30, 2012, 10, 30), True),
                  ((2012, 1, 1, 2013, 1, 1), True),
                  ((2012, 9, 1, 2012, 9, 4), True),
                  ((2012, 9, 1, 2012, 9, 1), False),
                  ((2013, 9, 1, 2012, 9, 1), False)]
    print("#########################")
    print("### Testing increment_date")
    print("#########################")
    for (args, answer) in test_cases:
        result = increment_date(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")
    print("")

def test_days_in_month():
    test_cases = [((2016,2), 29),
                  ((1908,2), 29),
                  ((1976,2), 29),
                  ((2016,1), 31),
                  ((1908,1), 31),
                  ((1976,1), 31),
                  ((1975,3), 31),
                  ((1981,4), 30),
                  ((1995,5), 31),
                  ((1995,6), 30),
                  ((1995,7), 31),
                  ((1995,8), 31),
                  ((1995,9), 30),
                  ((1995,10), 31),
                  ((1995,11), 30),
                  ((1995,12), 31)
                  ]
    print("#########################")
    print("### Testing days_in_month")
    print("#########################")
    for (args, answer) in test_cases:
        result = days_in_month(*args)
        if result != answer:
            print("Test with data:", args, "failed: expected: " + str(answer) + " received: " + str(result))
        else:
            print("Test case passed!")
    print("")
test_increment()
test_days_in_month()
test()
