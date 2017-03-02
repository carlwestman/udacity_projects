
# How many days old am i given my birthday and todays date

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

def part_year_compensation(y, m, d, part=2):
    # Calculates compensation for part years
    # y = year ie. 2001
    # m = month ie 2
    # d = date ie 24
    # part = 1 or 2, where 1 is days before date and 2 is days after date
    days_per_month_commom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate number of days from beginning of m to end of year
    i = m # Start from month after birthday
    days = days_per_month_commom[m-1] - d
    while i < 12:
        days += days_per_month_commom[i]
        i += 1
    # Compensate for leap year if is leap year and m <= 2
    if is_leap_year(y) and m <= 2:
        days += 1

    # If dates before, recalc by subtracting from total year days
    if part == 1:
        if is_leap_year(y):
            days = 366 - days
        else:
            days = 365 - days

    return days

def daysBetweenDates(y1, m1, d1, y2, m2, d2):

    #Validate input, y2, m2, d2 must be after y1, m1, d1 and must be within date range



    # Calc days of whole years, ie. excluding first and last year
    y = y1 + 1
    full_year_days = 0
    while y < y2:
        if is_leap_year(y):
            full_year_days += 366 # days in leap year
        else: #days in common year
            full_year_days += 365
        y += 1

    # adjust for part years
    first_year_days = part_year_compensation(y1, m1, d1, 2)
    last_year_days = part_year_compensation(y2, m2, d2, 1)

    total_days = full_year_days + first_year_days + last_year_days

    return total_days


### Unit Tests
def test_is_leap_year(ys, trace=False):
    results = []
    for y in ys:
        if trace == True:
            print("#Test for "+str(y[0])+": "+str(is_leap_year(y[0])))
            print("#Expected for "+str(y[0])+": "+str(y[1]))
            print("Passed:"+str(is_leap_year(y[0])==y[1]))
            print("#")
        results.append(is_leap_year(y[0])==y[1])
    print("### All test for 'is_loop_year' passed:"+str(False not in results))

def test_part_year_compensation(dates_to_test, trace=False):
    results = []
    for d in dates_to_test:
        if trace == True:
            print("#Test for "+str(d[0])+"-"+str(d[1])+"-"+str(d[2])+" "+str(d[3])+": days = "+str(part_year_compensation(d[0],d[1],d[2],d[3])))
            print("#Expected: days = "+str(d[4]))
            print(d[4]==part_year_compensation(d[0],d[1],d[2],d[3]))
            print("#")
        results.append(d[4]==part_year_compensation(d[0],d[1],d[2],d[3]))
    print("### All test for 'part_year_compensation' passed:"+str(False not in results))

### Test Data
years_to_test = [[2000,True],
                 [2001,False],
                 [2002,False],
                 [2004,True],
                 [1936,True],
                 [1973,False],
                 [1964,True],
                 [1582,False]]

dates_to_test = [[2013, 1, 2, 1, 2],
                 [1976, 12, 31, 1, 366],
                 [2013, 1, 2, 2, 363],
                 [1976, 12, 31, 2, 0],
                 [1976, 1, 2, 1, 2],
                 [2013, 12, 31, 1, 365],
                 [1976, 1, 2, 2, 364],
                 [2013, 12, 31, 2, 0]]

dates_to_test_2 = [[1986, 2, 8, 2017, 2, 28]]

### Run Tests
test_is_leap_year(years_to_test, False)
test_part_year_compensation(dates_to_test, False)

print(daysBetweenDates(1986, 2, 8, 2017, 2, 28))