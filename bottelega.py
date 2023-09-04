import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
# Обработка команды старт
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # Добавляем клавиратуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")
    item3 = types.KeyboardButton("Диас")
    item4 = types.KeyboardButton("Животное")
    item5 = types.KeyboardButton("Фото")
    item6 = types.KeyboardButton("Видео")
    item7 = types.KeyboardButton("Музыка")
    item8 = types.KeyboardButton("Синглтон")
    markup.add(item1, item2, item3, item4,item5,item6,item7,item8)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, я первый прототипный бот будущего миллионера.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
# Создаем список
kairat = ['мангуст','панда','осел','кот','мясо']
# Обработка сообщение
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Диас':
            bot.send_message(message.chat.id, 'Гений')
        elif message.text == 'Животное':
            bot.send_message(message.chat.id, str(random.choice(kairat)))
        elif message.text == 'Фото':
            photo = open('static/exc.jpg','rb')
            bot.send_photo(message.chat.id,photo)
        elif message.text == 'Видео':
            video = open('static/video.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        elif message.text == 'Музыка':
            music = open('static/XXXTENTACTION - Changes.mp3', 'rb')
            bot.send_audio(message.chat.id, music)
        elif message.text == 'Синглтон':
            bot.send_message(message.chat.id,'Singleton.Синглтон – это шаблон, который ограничивает создание экземпляра '
                                             'класса одним объектом. С помощью декоратора ты можешь определить класс как'
                                             ' синглтон. Таким образом класс либо возвращает существующий экземпляр '
                                             'класса, либо создает новый экземпляр. Этот декоратор можно добавить к '
                                             'любому объявлению класса, и он обеспечит создание не более одного '
                                             'экземпляра. Любые последующие вызовы вернут уже существующий экземпляр.')
        # Создаем инлайновую клавиратуру
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# Обработка инлайновой клавиратуры
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # Убираем встроенные кнопки
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?",
                reply_markup=None)

            # Добавляем уведомление
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))

# Запускаем
bot.polling(none_stop=True)