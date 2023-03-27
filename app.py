from time import sleep  # только в одном месте))
import telebot  # для работы бота

from working_with_files import *  # работа с файлами

# импорт токена
with open('token.txt', 'r', encoding='utf8') as f:
    TOKEN = f.read()
bot = telebot.TeleBot(TOKEN)

bot.send_message(chat_id="404173737", text='Запуск бота')


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    if message.text == "/help":
        bot.reply_to(message,
                     f"👋🏽 {message.chat.first_name}! \nЭтот бот может отслеживать 👀 свежие объявления на сайте AVITO за тебя 👍🏻 и скидывать их тебе в чат. \n\nПришли мне ссылку 👩🏼‍💻 на сайт АВИТО начинающуюся на 'https://www.avito.ru/...... ' С НАСТРОЕНЫМИ ПАРАМЕТРАМИ ПОИСКА НА САЙТЕ🔗 \n‼️ОБЯЗАТЕЛЬНО УКАЖИ СОРТИРОВКУ - ПО ДАТЕ‼️ категирия товара, цена, город, и тд, чем более конкретны будут настроены параметры на сайте авито, тем точнее будет поиск🔍")
    else:
        bot.send_message(message.chat.id,
                         f"👋🏽 {message.chat.first_name}! \nЭтот бот может отслеживать 👀‍ свежие объявления на сайте AVITO за тебя 👍🏻 и скидывать их тебе в чат. \n\nПришли мне ссылку 👩🏼‍💻 на сайт АВИТО начинающуюся на 'https://www.avito.ru/...... ' С НАСТРОЕНЫМИ ПАРАМЕТРАМИ ПОИСКА НА САЙТЕ🔗 \n‼️ОБЯЗАТЕЛЬНО УКАЖИ СОРТИРОВКУ - ПО ДАТЕ‼️ категирия товара, цена, город, и тд, чем более конкретны будут настроены параметры на сайте авито, тем точнее будет поиск🔍")


# проверяем наличие уже запомненной ссылки на поиск
@bot.message_handler(commands=['values'])
def handle_start_help(message: telebot.types.Message):
    # если можеи открыть юзер_лист, то посылаем содержимое
    try:
        with open(f'users_data\\{message.chat.first_name}_list.txt', 'r', encoding='utf8') as f:
            link = f.read()
        bot.send_message(message.chat.id, link)
    except:
        bot.reply_to(message, 'У вас нет сохраненной ссылки')


# удаляем данные юзера по запросу /delete
@bot.message_handler(commands=['delete'])
def handle_start_help(message: telebot.types.Message):
    delete_user_files(message.chat.first_name)
    bot.reply_to(message, "я удалил все ссылки🔥")


# Сохраняем ссылку на поиск если она содержит .avito.ru/ иначе просто реплейсим сообщение
@bot.message_handler(content_types=['text'])
def repitter(message: telebot.types.Message):
    # если в ссылке нет '.avito.ru/' то включаем попугая
    if ".avito.ru/" not in message.text:
        bot.send_message(message.chat.id, message.text)
    else:  # если в сообщении есть .avito.ru/
        bot.send_message(message.chat.id, 'Дай мне немного времени⏳')
        # записываем в юзер_лист сообщение
        with open(f'users_data\\{message.chat.first_name}_list.txt', 'w', encoding="utf8") as f:
            f.write(f'{message.text}')
            # создаем файлы юзера для последующей работы с ними
        write_files_users(message.chat.first_name)
        # запускаем поиск объявлений
        poisk()
        # проверяем файл со ссылками на новые объявления
        try:
            with open(f'users_data\\{message.chat.first_name}_links.txt', 'r', encoding="utf8") as file:
                data = file.read()
            # если в файле есть ссылки
            if len(data) > 10:
                bot.send_message(message.chat.id,
                                 "Записал📝 \nЯ буду отслеживать новые объявления ТОЛЬКО ПО ЭТОЙ ссылке👀")
                bot.send_message(message.chat.id,
                                 "🔊Что бы я проверил новые объявления, \nпришли мне звуковое сообщение 🗣 вежливо попросив об этом")
            # если в файле нет ссылок, то удаляем записанный юзер_лист и юзер_линкс
            else:
                bot.send_message(message.chat.id, "Не могу найти объявлениЙ🕵🏻‍♂")
                delete_user_files(name=message.chat.first_name)
        except:  # если файла нет
            bot.send_message(message.chat.id, "Не могу найти объявлениЙ🕵🏻‍♂")


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['photo', 'document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, f'Nice 🤩')


# Запускаем выполнение поиска новых сообщений с помощью голосовой команды
# обрабатываются голосовые сообщения
@bot.message_handler(content_types=['voice'])
def repitter(message: telebot.types.Message):
    # записываем юзер_найм в файл для последующей работы с ним
    with open("user_name.txt", "w", encoding='utf8') as f:
        f.write(message.chat.first_name)
    try:
        with open(f'users_data\\{message.chat.first_name}_list.txt', 'r', encoding='utf8') as f:
            f.read()
        bot.send_message(message.chat.id, 'Дай мне немного времени⏳')
        # запускаем файл поиска объявлений на сайте
        poisk()
        bot.send_message(message.chat.id, 'Проверка прошла!')
        # читаем файл с найденными новыми ссылками
        with open(f'users_data\\{message.chat.first_name}_links.txt', "r", encoding="utf8") as f:
            data = f.read()
            if len(data) > 30:
                # отправляем данные из файла юзеру
                d = data.split("\n")
                for i in d[:-1]:
                    sleep(2)
                    print(i)
                    bot.send_message(message.chat.id, text=i)
                bot.send_message(message.chat.id, 'Это всё👐')
            else:
                bot.send_message(message.chat.id, 'Не нашел 👁новых👁 объявлений')

    except:
        bot.reply_to(message, "🌐Нету ссылки для поиска🤔")


bot.polling(none_stop=True)
