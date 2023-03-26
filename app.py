import os  # для работы с консолью
from time import sleep  # только в одном месте))
import telebot  # для работы бота

# импорт токена
with open('token.txt', 'r', encoding='utf8') as f:
    TOKEN = f.read()
bot = telebot.TeleBot(TOKEN)


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
        bot.reply_to(message, 'У вас нет сохраненных ссылок')


# Сохраняем ссылку на поиск если она содержит .avito.ru/ иначе просто реплейсим сообщение
@bot.message_handler(content_types=['text'])
def repitter(message: telebot.types.Message):
    # если в ссылке нет '.avito.ru/' то включаем попугая
    if ".avito.ru/" not in message.text:
        bot.send_message(message.chat.id, message.text)
    else:  # если в сообщении есть .avito.ru/
        # записываем в юзер_лист сообщение
        with open(f'users_data\\{message.chat.first_name}_list.txt', 'w', encoding="utf8") as f:
            f.write(f'{message.text}')
        # запускаем поиск объявлений
        os.system("python -m pytest -v C:\Skillproject\PageObjectProject\\tests.py")
        # читаем файл со ссылками на новые объявления
        with open(f'users_data\\{message.chat.first_name}_links.txt', 'r', encoding="utf8") as file:
            data = file.read()
        # если в файле есть ссылки
        if len(data) > 10:
            bot.send_message(message.chat.id, "Записал📝 \nЯ буду отслеживать новые объявления ТОЛЬКО ПО ЭТОЙ ссылке👀")
            bot.send_message(message.chat.id,
                             "🔊Что бы я проверил новые объявления, \nпришли мне звуковое сообщение 🗣 вежливо попросив об этом")
        # если в файле нет ссылок, то удаляем записанный юзер_лист и юзер_линкс
        else:
            bot.send_message(message.chat.id, "Не могу найти объявлениЙ🕵🏻‍♂")
            os.remove(f'users_data\\{message.chat.first_name}_links.txt')
            os.remove(f'users_data\\{message.chat.first_name}_list.txt')


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['photo', 'document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, f'Nice meme XDD')


# Запускаем выполнение поиска новых сообщений с помощью голосовой команды
# обрабатываются голосовые сообщения
@bot.message_handler(content_types=['voice'])
def repitter(message: telebot.types.Message):
    # записываем имя юзера (запустившего поиск) в файл для последующей работы с ним
    with open("user_name.txt", "w", encoding='utf8') as f:
        f.write(message.chat.first_name)
    # подготавливаем файл с общим дампом ссылок юзера
    with open(f'users_data\\{message.chat.first_name}_dump.txt', 'w', encoding='utf8') as file:
        file.write('*')
    # запускаем файл поиска объявлений на сайте
    os.system("python -m pytest -v C:\Skillproject\PageObjectProject\\tests.py")
    bot.send_message(message.chat.id, 'Проверка прошла!')
    # читаем файл с найденными новыми ссылками
    with open(f'users_data\\{message.chat.first_name}_links.txt', "r", encoding="utf8") as f:
        data = f.read()
        # отправляем данные из файла юзеру
        d = data.split("\n")
        for i in d[:-1]:
            sleep(2)
            print(i)
            bot.send_message(message.chat.id, text=i)


bot.polling(none_stop=True)
