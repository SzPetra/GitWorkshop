def is_twodigit_odd(number):
    if len(str(number)) == 2:
        if number % 2 == 1:
            return True
        else:
            return False
    return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if sudo_mode:
        return True
    elif writable_by_others:
        return True
    elif user == file_owner:
        if writable_by_owner:
            return True
    elif file_group in users_groups:
        if writable_by_group:
            return True
    return False


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
            return False
        else:
            return True
        return True
    else:
        return False


def is_sunday(day, weekday_of_first):
    if weekday_of_first == "M":
        if day == 1:
            return False
        elif day == 7:
            return True
        elif day == 14:
            return True
        elif day == 21:
            return True
        elif day == 28:
            return True
    elif weekday_of_first == "Tu":
        if day == 1:
            return False
        elif day == 6:
            return True
        elif day == 13:
            return True
        elif day == 20:
            return True
        elif day == 27:
            return True
    elif weekday_of_first == "W":
        if day == 1:
            return False
        elif day == 5:
            return True
        elif day == 12:
            return True
        elif day == 19:
            return True
        elif day == 26:
            return True
    elif weekday_of_first == "Th":
        if day == 1:
            return False
        elif day == 4:
            return True
        elif day == 11:
            return True
        elif day == 18:
            return True
        elif day == 25:
            return True
    elif weekday_of_first == "F":
        if day == 1:
            return False
        elif day == 3:
            return True
        elif day == 10:
            return True
        elif day == 17:
            return True
        elif day == 24:
            return True
        elif day == 31:
            return True
    elif weekday_of_first == "Sa":
        if day == 1:
            return False
        elif day == 2:
            return True
        elif day == 9:
            return True
        elif day == 16:
            return True
        elif day == 23:
            return True
        elif day == 30:
            return True
    else:
        if day == 1:
            return True
        elif day == 8:
            return True
        elif day == 15:
            return True
        elif day == 22:
            return True
        elif day == 29:
            return True
    return False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if rains:
        if wind_scale < 7:
            return True
    elif cloudy:
        if wind_scale < 7:
            if red_sky:
                return True
            if strong_flower_smell:
                return True
            if spiders_down:
                return True
            if lying_cattle:
                return True
    elif strong_sunshine:
        if wind_scale < 7:
            return True
    return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to:
        if trouble_sleeping:
            return False
        if after_4pm:
            return False
        else:
            if not at_work:
                if have_30m:
                    return True
                elif have_10m:
                    return True
            elif at_work:
                if not mad_boss:
                    if have_30m:
                        return True
                    elif have_10m:
                        return True
    return False
