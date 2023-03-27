from avito_pages import SearchHelper


def test_search(browser):
    # читаем имя юзера
    with open('user_name.txt', "r", encoding='utf8') as f:
        user_name = f.read()
    # очищаем файл ссылок юзера
    with open(f'users_data\\{user_name}_links.txt', 'w', encoding='utf8') as ff:
        ff.write(" ")
    # инициализируем поиск по url из файла юзера
    with open(f'users_data\\{user_name}_list.txt', 'r', encoding='utf8') as file:
        url = file.read()
    avito_main_page = SearchHelper(browser)  # запускаем браузер
    avito_main_page.otkrivaem_site(url)  # открываем url
    avito_main_page.search_all()  # запускаем сортировку ссылок на странице
