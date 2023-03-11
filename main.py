import time
import constants
import core
import telebot
import datetime
import  threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sqlite3

print('Bot started...')
bot = telebot.TeleBot(constants.API_KEY)
db_subs = {}
def main():
    def footer_buttons():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        today_button = KeyboardButton(text='Today')
        specific_day_button = KeyboardButton(text='By day')
        subscribe_button = KeyboardButton(text='Subscription')
        more_button=KeyboardButton(text='More')

        keyboard.add(today_button, specific_day_button, subscribe_button,more_button)
        return keyboard


    @bot.message_handler(commands=['start'])
    def start(message):
        intro = "Hi,this bot will help you  to manage universtity lesson-links\nYou can click any days you want to check or subscribe for automatical sending messages."
        bot.send_message(message.chat.id, intro, reply_markup=footer_buttons())
        db_data=(str(message.chat.id),False)

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS subscribers(
                        id text,
                        subscriber boolean
        )""")
        connection.commit()
        def user_creating(data_to_db):
            cursor.execute(f'INSERT INTO subscribers VALUES {data_to_db}')
            connection.commit()
        user_creating(db_data)
        connection.close()


    def specific_days_buttons():
        markup = InlineKeyboardMarkup()
        markup.row_width = 5
        monday_button = InlineKeyboardButton("Mon", callback_data="MONDAY")
        tuesday_button = InlineKeyboardButton("Tue", callback_data="TUESDAY")
        wednesday_button = InlineKeyboardButton("Wed", callback_data="WEDNESDAY")
        thursday_button = InlineKeyboardButton("Thu", callback_data="THURSDAY")
        friday_button = InlineKeyboardButton("Fri", callback_data="FRIDAY")
        saturday_button = InlineKeyboardButton("Sat", callback_data="SATURDAY")

        markup.add(monday_button, tuesday_button, wednesday_button, thursday_button, friday_button, saturday_button)
        return markup


    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "MONDAY":
            text = core.Monday()
            bot.send_message(call.message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)
        if call.data == "TUESDAY":
            text = core.Tuesday()
            bot.send_message(call.message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)
        if call.data == "WEDNESDAY":
            text = core.Wednesday()
            bot.send_message(call.message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)
        if call.data == "THURSDAY":
            text = core.Thursday()
            bot.send_message(call.message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)
        if call.data == "FRIDAY":
            text = core.Friday()
            bot.send_message(call.message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)
        if call.data == "SATURDAY":
            text = core.Saturday()
            bot.send_message(call.message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)


    @bot.message_handler(func=lambda message: message.text == "Today")
    def message_handler(message):
        text = ""
        day = str(datetime.datetime.today().strftime('%A'))
        if day == 'Monday':
            text = core.Monday(check_today=True)
        if day == 'Tuesday':
            text = core.Tuesday(check_today=True)
        if day == 'Wednesday':
            text = core.Wednesday(check_today=True)
        if day == 'Thursday':
            text = core.Thursday(check_today=True)
        if day == 'Friday':
            text = core.Friday(check_today=True)
        if day == 'Saturday':
            text = core.Saturday()
        if day == "Sunday":
            text = "It looks like today is a weekend"

        bot.send_message(message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)


    @bot.message_handler(func=lambda message: message.text == "By day")
    def message_handler(message):
        text = "Which day do you want to see?"
        bot.send_message(message.chat.id, text, reply_markup=specific_days_buttons())

    @bot.message_handler(func=lambda message: message.text == "id")
    def message_handler(message):
        text = "Our chat id is: " + str(message.chat.id)
        bot.send_message(message.chat.id, text)
    
    @bot.message_handler(func=lambda message: message.text == "More")
    def message_handler(message):
        text = constants.EMAILS
        bot.send_message(message.chat.id, text, reply_markup=footer_buttons(),parse_mode='Markdown',disable_web_page_preview=True)    
    
    @bot.message_handler(func=lambda message: message.text == "time")
    def message_handler(message):
        now = datetime.datetime.now()
        text = f"Time on the server: {now.strftime('%H:%M:%S')}"
 
        bot.send_message(message.chat.id, text, reply_markup=footer_buttons())    


    @bot.message_handler(func=lambda message: message.text == "Subscription")
    def message_handler(message):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        def state_changing(chat_id):
            cursor.execute(f"SELECT subscriber FROM subscribers WHERE id='{chat_id}'")
            state = cursor.fetchall()[0][0]
            if state == True:
                cursor.execute(f"UPDATE subscribers SET subscriber=False WHERE id='{chat_id}'")
                connection.commit()
                return 'You have unsubscribed!'
            if state == False:
                cursor.execute(f"UPDATE subscribers SET subscriber=True WHERE id='{chat_id}'")
                connection.commit()
                return 'You have subscribed!'
            else:
                cursor.execute(f'INSERT INTO subscribers VALUES ({chat_id},True)')
                connection.commit()
                return 'You have subscribed!'

        text=state_changing(message.chat.id)
        bot.send_message(message.chat.id, text, reply_markup=footer_buttons())
        connection.close()


    

    @bot.message_handler(func=lambda message: message.text.lower() in constants.THANKS)
    def message_handler(message):
        text = "My pleasure, bro 😉"
        bot.send_message(message.chat.id, text, reply_markup=footer_buttons())


    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        bot.send_message(message.chat.id, "I have no idea what do you want :(")
        sti = open('bear.webp', 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=footer_buttons())
        bot.send_message(message.chat.id, "You can try buttons below 🤔")
        sti.close()



    bot.infinity_polling()

def auto():
    def footer_buttons():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        today_button = KeyboardButton(text='Today')
        specific_day_button = KeyboardButton(text='By day')
        subscribe_button = KeyboardButton(text='More')
        keyboard.add(today_button, specific_day_button, subscribe_button)
        return keyboard

    def check_subscribers():
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT id FROM subscribers WHERE subscriber=True")
        return cur.fetchall()
    while True:
        text = ''
        time_now = datetime.datetime.now()
        day = str(time_now.today().strftime('%A'))

        if time_now.strftime('%H') == constants.HOUR and time_now.strftime('%M') == constants.MINUTE:
            if day == 'Monday':
                text = core.Monday(check_today=True)
            if day == 'Tuesday':
                text = core.Tuesday(check_today=True)
            if day == 'Wednesday':
                text = core.Wednesday(check_today=True)
            if day == 'Thursday':
                text = core.Thursday(check_today=True)
            if day == 'Friday':
                text = core.Friday(check_today=True)
            if day == 'Saturday':
                text = core.Saturday()
            if day == "Sunday":
                text = "It looks like today is a weekend"

            subscribers=check_subscribers()
            subscribers.extend(constants.SUBSCRIBERS)
            for subscriber in subscribers:
                bot.send_message(subscriber[0], text, reply_markup=footer_buttons(), parse_mode='Markdown',disable_web_page_preview=True)
            time.sleep(60)



t1=threading.Thread(target=main)
t2=threading.Thread(target=auto)
t1.start()
t2.start()
