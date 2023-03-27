# запускает поиск объявлений
import os


def poisk():
    os.system("python -m pytest -v C:\Skillproject\SearchAvitoBot\\search.py")  # путь до файла


# удаляет файлы юзера
def delete_user_files(name):
    os.remove(f'users_data\\{name}_links.txt')
    os.remove(f'users_data\\{name}_list.txt')
    os.remove(f'users_data\\{name}_dump.txt')


# создает файлы юзера для последующей работы с ними
def write_files_users(name):
    # записываем имя юзера (запустившего поиск) в файл для последующей работы с ним
    with open("user_name.txt", "w", encoding='utf8') as f:
        f.write(name)
    # подготавливаем файл с общим дампом ссылок юзера
    with open(f'users_data\\{name}_dump.txt', 'a', encoding='utf8') as file:
        file.write('*')
