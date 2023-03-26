from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # принимаем драйвр
    def __init__(self, driver):
        self.driver = driver

    # переходим на сайт, возвращаем драйвер
    def otkrivaem_site(self, url):
        return self.driver.get(url)

    # # ищет элеменТ на странице и возвращает ЕГО
    # def find_element(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
    #                                                   message=f"Not find {locator}")

    # ищет элементЫ на странице и возвращает ИХ
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Какие-то элементы не найдены-{locator}')
