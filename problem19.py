'''
Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def count_sundays():

    count = 0
    index = 0
    current_day = False

    # loop through years
    for year in range(1900, 2001):

        # loop through month
        for month, days in months.items():

            # add leap year calculation
            if year % 4 == 0 and month == "February":
                if year % 100 == 0:
                    if year % 400 == 0:
                        days += 1
                else:        
                    days += 1

            # loop through days
            for day in range(1, days + 1):

                # set Jan 1 1900 to Monday
                if year == 1900 and month == "January" and day == 1:
                    current_day = weekdays[index]
                else:
                    # assign current_day
                    if index == 6:
                        index = 0
                    else:
                        index += 1
                    
                    current_day = weekdays[index]
                
                print("Today is ", day, "of ", month, year, ". Day of week is ", current_day)

                # if sunday and 1st of month
                if current_day == "Sunday" and day == 1 and year >= 1901:

                    # add to sum
                    count += 1

    return count

print("Answer to problem 19: ", count_sundays())