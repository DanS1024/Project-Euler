months = [31,28,31,30,31,30,31,31,30,31,30,31]

def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

weekday, month, year = 1, 0, 1900
count = 0
while year <= 2000:
    if weekday == 0 and year >= 1901:
        count += 1
    if month == 1 and leapYear(year):
        weekday = (weekday + 29) % 7
    else:
        weekday = (weekday + months[month]) % 7
    month += 1
    if month == 12:
        month = 0
        year += 1

print(count)