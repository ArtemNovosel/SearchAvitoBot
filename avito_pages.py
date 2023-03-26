# описываем страницу
from selenium.webdriver.common.by import By
from base_page import BasePage


# создаем класс с константами локаторов
class SearchLocators:
    LOCATOR_AVITO_SEARCH_FIELD = (By.XPATH, '//*[@data-marker="search-form/suggest"]')  # поле поиска
    LOCATOR_AVITO_SEARCH_BUTTON = (By.XPATH, '//*[@class="desktop-9uhrzn"]')  # кнопка найти
    LOCATOR_AVITO_HEADERS = (By.XPATH, '//*[@itemprop="name"]')  # все заголовки объявлений на странице
    LOCATOR_AVITO_PRICES = (By.XPATH, '//*[@itemprop="price"]')  # все цены на странице
    LOCATOR_AVITO_LINKS = (By.XPATH, '//*[@class="iva-item-titleStep-pdebR"]/a')  # все ссылки на объявления на странице


#класс поиска элементов
class SearchHelper(BasePage):
    def search_avito_all(self):
        with open('user_name.txt', "r", encoding='utf8') as f:
            user_name = f.read()
        all_links = self.find_elements(SearchLocators.LOCATOR_AVITO_LINKS)
        all_names = self.find_elements(SearchLocators.LOCATOR_AVITO_LINKS)
        all_prices = self.find_elements(SearchLocators.LOCATOR_AVITO_PRICES)
        itog_list = []
        a = 0
        for x in all_prices:
            with open('dump_list_all.txt', 'r', encoding='utf8') as file:
                data = file.read()
                if all_links[a].get_attribute("href") not in data:
                    with open(f'{user_name}_links.txt', 'a', encoding='utf8') as f:
                        f.write(
                            f'{int(x.get_attribute("content"))} *{all_names[a].text} \n {all_links[a].get_attribute("href")} \n')
                    with open('dump_list_all.txt', 'a', encoding='utf8') as f:
                        f.write(
                            f'{int(x.get_attribute("content"))} *{all_names[a].text}*  {all_links[a].get_attribute("href")} \n')
            a += 1
