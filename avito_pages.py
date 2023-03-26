# описываем страницу
from selenium.webdriver.common.by import By
from base_page import BasePage


# создаем класс с константами локаторов
class SearchLocators:
    # LOCATOR_AVITO_SEARCH_FIELD = (By.XPATH, '//*[@data-marker="search-form/suggest"]')  # поле поиска
    # LOCATOR_AVITO_SEARCH_BUTTON = (By.XPATH, '//*[@class="desktop-9uhrzn"]')  # кнопка найти
    LOCATOR_AVITO_HEADERS = (By.XPATH, '//*[@itemprop="name"]')  # все заголовки объявлений на странице
    LOCATOR_AVITO_PRICES = (By.XPATH, '//*[@itemprop="price"]')  # все цены на странице
    LOCATOR_AVITO_LINKS = (By.XPATH, '//*[@class="iva-item-titleStep-pdebR"]/a')  # все ссылки на объявления на странице


# класс поиска элементов
class SearchHelper(BasePage):
    def search_all(self):
        # читаем имя юзера запустившего поиск
        with open('user_name.txt', "r", encoding='utf8') as f:
            user_name = f.read()
        # собираем локатооры на странице
        all_links = self.find_elements(SearchLocators.LOCATOR_AVITO_LINKS)
        all_names = self.find_elements(SearchLocators.LOCATOR_AVITO_LINKS)
        all_prices = self.find_elements(SearchLocators.LOCATOR_AVITO_PRICES)
        a = 0
        for x in all_prices:
            # читаем файл с дампом общих ссылок юзера
            with open(f'users_data\\{user_name}_dump.txt', 'r', encoding='utf8') as file:
                data = file.read()
                # если найденная ссылка отсутствует в дампе записываем ее туда и в юзер_линкс
                if all_links[a].get_attribute("href") not in data:
                    with open(f'users_data\\{user_name}_links.txt', 'a', encoding='utf8') as f:
                        f.write(
                            f'{int(x.get_attribute("content"))} *{all_names[a].text} \n {all_links[a].get_attribute("href")} \n')
                    with open(f'users_data\\{user_name}_dump.txt', 'a', encoding='utf8') as f:
                        f.write(
                            f'{int(x.get_attribute("content"))} *{all_names[a].text}*  {all_links[a].get_attribute("href")} \n')
            a += 1
