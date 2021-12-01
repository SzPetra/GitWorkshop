def is_twodigit_odd(number):
    return len(str(number)) == 2 and number % 2 == 1


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return sudo_mode or writable_by_others or (user == file_owner and writable_by_owner) or (file_group in users_groups and writable_by_group)


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)


def is_sunday(day, weekday_of_first):
    return (weekday_of_first == "M" and day == 7 or day == 14 or day == 21 or day == 28) or (weekday_of_first == "Tu" and day == 6 or day == 13 or day == 20 or day == 27) or (weekday_of_first == "W" and day == 5 or day == 12 or day == 19 or day == 26 or day == 31) or (weekday_of_first == "Th" and day == 4 or day == 11 or day == 18 or day == 25 or day == 30) or (weekday_of_first == "F" and day == 3 or day == 10 or day == 17 or day == 24 or day == 29) or (weekday_of_first == "Sa" and day == 2 or day == 9 or day == 16 or day == 23 or day == 28) or (weekday_of_first == "Su" and day == 1 or day == 8 or day == 15 or day == 22 or day == 27)


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return (rains and wind_scale < 7) or (cloudy and (red_sky or strong_flower_smell or spiders_down or lying_cattle) and wind_scale < 7) or (strong_sunshine and wind_scale < 7)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return want_to and not trouble_sleeping and not after_4pm and (not at_work and (have_30m or have_10m) or at_work and not mad_boss and (have_30m or have_10m))
