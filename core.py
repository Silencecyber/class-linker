from datetime import datetime
from datetime import timedelta
import  constants

def define_ODD_or_EVEN_week(date):
    def odd_week(listmain):
        list_odd = []
        i = 0
        counter = 7
        while i < len(listmain):
            while i < counter:
                list_odd.append(listmain[i])
                i += 1
            i += 7
            counter += 14
        return list_odd

    start = datetime.strptime(constants.START_DATE, "%d-%m-%Y")
    end = datetime.strptime(constants.END_DATE, "%d-%m-%Y")
    date_generated = [start + timedelta(days=x) for x in range(0, (end - start).days)]
    odd_week = odd_week(date_generated)
    odd_week_str = []
    for odd in odd_week:
        odd_week_str.append(odd.strftime("%d-%m-%Y"))
    date_time = date.strftime("%d-%m-%Y")
    if date_time in odd_week_str:
        return 'ODD'
    else:
        return 'EVEN'


def Monday(check_today=False):
    if check_today:
        time_now = datetime.now()
        odd_or_even_week = define_ODD_or_EVEN_week(time_now)
        day = str(datetime.today().strftime('%A'))
        text = f'Today is {day} and an {odd_or_even_week}\n'
        if define_ODD_or_EVEN_week(time_now) == 'ODD':
            return text+constants.MONDAY['ODD']
        else:
            return text+constants.MONDAY['EVEN']
    else:
        return constants.MONDAY['ODD'] + '\n' + constants.MONDAY['EVEN']


def Tuesday(check_today=False):
    if check_today:
        time_now = datetime.now()
        odd_or_even_week = define_ODD_or_EVEN_week(time_now)
        day = str(datetime.today().strftime('%A'))
        text = f'Today is {day} and an {odd_or_even_week}\n'
        if define_ODD_or_EVEN_week(time_now) == 'ODD':
            return text+constants.TUESDAY['ODD']
        else:
            return text+constants.TUESDAY['EVEN']
    else:
        return constants.TUESDAY['ODD'] + '\n' + constants.TUESDAY['EVEN']

def Wednesday(check_today=False):
    if check_today:
        time_now = datetime.now()
        odd_or_even_week = define_ODD_or_EVEN_week(time_now)
        day = str(datetime.today().strftime('%A'))
        text = f'Today is {day} and an {odd_or_even_week}\n'
        if define_ODD_or_EVEN_week(time_now) == 'ODD':

            return text+constants.WEDNESDAY['ODD']
        else:
            return text+constants.WEDNESDAY['EVEN']
    else:
        return constants.WEDNESDAY['ODD'] + '\n' + constants.WEDNESDAY['EVEN']

def Thursday(check_today=False):
    if check_today:
        time_now = datetime.now()
        odd_or_even_week = define_ODD_or_EVEN_week(time_now)
        day = str(datetime.today().strftime('%A'))
        text = f'Today is {day} and an {odd_or_even_week}\n'
        if define_ODD_or_EVEN_week(time_now) == 'ODD':

            return text+constants.THURSDAY['ODD']
        else:
            return text+constants.THURSDAY['EVEN']
    else:
        return constants.THURSDAY['ODD'] + '\n' + constants.THURSDAY['EVEN']

def Friday(check_today=False):
    if check_today:
        time_now = datetime.now()
        odd_or_even_week = define_ODD_or_EVEN_week(time_now)
        day = str(datetime.today().strftime('%A'))
        text = f'Today is {day} and an {odd_or_even_week}\n'
        if define_ODD_or_EVEN_week(time_now) == 'ODD':
            return text+constants.FRIDAY['ODD']
        else:
            return text+constants.FRIDAY['EVEN']
    else:
        return constants.FRIDAY['ODD'] + '\n' + constants.FRIDAY['EVEN']

def Saturday():
    return constants.SATURDAY



