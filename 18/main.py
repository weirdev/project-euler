DAYS_IN_1900 = 366
DAYS_BY_MONTH_BASE = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    # 1 Jan 1900 was a Monday
    day_of_week = 1
    day_of_week += DAYS_IN_1900
    day_of_week %= 7

    sundays = 0
    # Now its 1 Jan 1901
    for yr in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:
                sundays += 1
            day_of_week += DAYS_BY_MONTH_BASE[month]
            if month == 1 and is_leap_year(yr):
                day_of_week += 1
            day_of_week %= 7

    print(sundays)


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    main()
