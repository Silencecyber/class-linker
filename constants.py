# api key
API_KEY = '5103838295:AAHwdmZVNQNzrsdGWUKhp5n8L2Qz-4ZA-Ug'

# start of the year  and the end of the study year
# start date must be on MONDAY, if it's not, assign  that MONDAY date  which is before  start study day!
START_DATE = "30-01-2023"
END_DATE = "26-06-2023"

# Time when the bot will send automatic messages about your current schedule.
HOUR = "04"
MINUTE = "45"

FREE_TIME = "Free time 😌"
# schedule
MONDAY = {
    'EVEN': f'\nMonday *EVEN* schedule\n'
            f'(8:00-9:35) [Math](https://us04web.zoom.us/)\n'
            f'(9:50-11:25) [Physic](https://us04web.zoom.us/)\n'
            f'(11:50-13:25) [History](https://us04web.zoom.us/)\n'
            f'(13:40-15:15) [Biology](https://us04web.zoom.us/)',
    'ODD': f'Monday *ODD* schedule\n'
           f'(8:00-9:35) [Biology](https://us04web.zoom.us/)\n'
           f'(9:50-11:25) [History](https://us04web.zoom.us/)\n'
           f'(11:50-13:25) [Physic](https://us04web.zoom.us/)\n'
           f'(13:40-15:15) [Math](https://us04web.zoom.us/)'
}
TUESDAY = {
    'EVEN': f'\nTuesday *EVEN* schedule \n'
            f'(8:00-9:35) {FREE_TIME}\n'
            f'(9:50-11:25) [Philosophy](https://us04web.zoom.us/)\n'
            f'(11:50-13:25) [Music]()\n'
            f'(13:40-15:15) [English](https://us04web.zoom.us/)\n',
    'ODD': f'Tuesday *ODD* schedule\n'
           f'(8:00-9:35) {FREE_TIME}\n'
           f'(9:50-11:25) [Chinese](https://meet.google.com/)\n'
           f'(11:50-13:25) [Biology]()\n'
           f'(13:40-15:15) [Math](https://meet.google.com/)'
}
WEDNESDAY = {
    'EVEN': f'\nWednesday *EVEN* schedule \n'
            f'(8:00-9:35) [History](https://meet.google.com/)\n'
            f'(9:50-11:25) {FREE_TIME}\n'
            f'(11:50-13:25) {FREE_TIME}\n'
            f'(13:40-15:15) {FREE_TIME}',
    'ODD': f'Wednesday *ODD* schedule\n'
           f'(8:00-9:35) [Math](https://meet.google.com/)\n'
           f'(9:50-11:25)[Physic](https://meet.google.com/)\n'
           f'(11:50-13:25) {FREE_TIME}\n'
           f'(13:40-15:15) {FREE_TIME}',
}
THURSDAY = {
    'EVEN': f'\nThursday *EVEN* schedule \n'
            f'(8:00-9:35) [Bilogy](https://meet.google.com/)\n'
            f'(9:50-11:25) [Math](https://meet.google.com/)\n'
            f'(11:50-13:25) [History](https://meet.google.com/)\n'
            f'(13:40-15:15) {FREE_TIME}',
    'ODD': f'Thursday *ODD* schedule\n'
           f'(8:00-9:35) [Physic]()\n'
           f'(9:50-11:25) [Math]()\n'
           f'(11:50-13:25) [English]()\n'
           f'(13:40-15:15) {FREE_TIME}',
}
FRIDAY = {
    'EVEN': f'\nFriday *EVEN* schedule \n'
            f'(8:00-9:35) {FREE_TIME}\n'
            f'(9:50-11:25) {FREE_TIME}\n'
            f'(11:50-13:25) {FREE_TIME}\n'
            f'(13:40-15:15) {FREE_TIME}',
    'ODD': f'Friday *ODD* schedule\n'
           f'(8:00-9:35) {FREE_TIME}\n'
           f'(9:50-11:25) {FREE_TIME}\n'
           f'(11:50-13:25) {FREE_TIME}\n'
           f'(13:40-15:15) {FREE_TIME}',
}
SATURDAY = "No data!"

EMAILS = """
[Math classroom](https://classroom.google.com/)
[Physic classroom](https://classroom.google.com/)
Bob's email -  bob@gmail.com
Max's email - max@gmail.com
John's email - john@ukr.net
"""

# static subscribers (without database communication)
SUBSCRIBERS = [('693608785',)]
# THANKS
THANKS = ["thanks", "thank you", "thx", "дякую", "пасиба", "спасибо", "пасеба", "пасип", "спс"]
