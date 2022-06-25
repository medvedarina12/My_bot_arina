from telebot import types

from settings import MypyBot, users


#--------------------#
# COMMAND FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(commands=['start'])
def start_message(message):
    MypyBot.send_message(
        message.chat.id,
        """
            Доброго дня,
Вас вітає інтернет магазин прикрас:
ℳedved_biser.uα
Подивитись актуальні новини нашого магазину❤:
/relevant
Ознайомитись з магазином можна за посиланням:
https://www.instagram.com/medved_biser.ua/
Замовити прикраси 🛍 ↓
/by
        """,
        reply_markup=types.ReplyKeyboardRemove()    # убираем клавиатуру если была
    )


@MypyBot.message_handler(commands=['relevant'])
def button_message(message):
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton(
        "Відгуки", 
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTIyMTAyMzk4MzExODAx?igshid=YmMyMTA2M2Y='
    )
    item2=types.InlineKeyboardButton(
        "Ukrainian collection", 
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTA5OTc3ODYyMzkxNTk1?igshid=YmMyMTA2M2Y='
    )
    markup.add(item1, item2)
    MypyBot.send_message(message.chat.id,'💁Актуальні новинки нашого магазина  тут ↓',reply_markup=markup)


@MypyBot.message_handler(commands=['by'])
def button_pmenu(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1=types.KeyboardButton("В інсті")
    item2=types.KeyboardButton("В телеграм боті")
    markup.add(item1, item2)
    MypyBot.send_message(message.chat.id,'Де Вам зручніше оформити замовлення?',reply_markup=markup)


@MypyBot.message_handler(commands=['start_by'])
def button_pmenu(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1=types.KeyboardButton("Так,вже обрала")
    item2=types.KeyboardButton("Ні,потрібен каталог")
    markup.add(item1, item2)
    MypyBot.send_message(message.chat.id,'Ви вже обрали які прикраси хочете замовити?',reply_markup=markup)

 


# отладочная функция для отслеживания пользователей
@MypyBot.message_handler(commands=['users'])
def show_users(message):
    msg = ''
    if not users:
        MypyBot.send_message(message.chat.id, 'no one')
    else:
        print(len(users), users)
        for user in users:
            msg += str(user) + ' '
        MypyBot.send_message(message.chat.id, msg)


#--------------------#
#  HELPER FUNCTIONS  #
#--------------------#




#--------------------#
# REPLYER FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
   print(message.text)


   match message.text:
        case "В інсті": 
            MypyBot.reply_to(message, "Тоді переходь за посиланням https://www.instagram.com/medved_biser.ua/")
        case "В телеграм боті":
            MypyBot.reply_to(message, "Розпочнемо замовлення /start_by")
        case "Так,вже обрала": 
            MypyBot.reply_to(message, "Скиньте фото прикрас які ви хочете замовити")
        case "Ні,потрібен каталог":
            MypyBot.reply_to(message,"Каталог")
        case _:
            if users:
                if users[str(message.chat.id)]['d_checker'] == False \
                    and users[str(message.chat.id)]['d_cnt'] == 0:
                    start_message(message)
            else:
                start_message(message)

#--------------------#
#     ENTRY POINT    #
#--------------------#

if __name__ == "__main__":
    MypyBot.polling()