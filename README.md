# @SearchAvitoBot - рабочий бот в телеге.

Данный бот мониторит новые объявления (на известном сайте объявлений) по ссылке с настроенными параметрами поиска

app.py - тело бота

base_page.py - методы работы со страницей

avito_pages.py - описана работа на конкретной странице(локаторы, поиск по ним)

conftest.py - инициализация сессии/настройки вебдрайвера

chromedriver.exe - драйвер работы с браузером Google Chrome Версия 111

working_with_files.py - работа с файлами

Для запуска бота необходим token.txt с токеном в корне проекта 

Видео

https://user-images.githubusercontent.com/122513124/229030276-352faaed-f115-4d78-9aee-149c04dd6053.mp4

https://user-images.githubusercontent.com/122513124/229030526-74181914-379a-42bf-a02d-f39dbbcd5a43.mp4

![Screenshot_27](https://user-images.githubusercontent.com/122513124/227905154-88e99d3d-c9d4-49ef-9e5e-3828dc98a9bf.jpg)

Настраиваем параметры поиска на сайте. Для получения только новых объявлений ставим сортировку ПО ДАТЕ. Чем конкретнее будут параметры тем точнее будет поиск.

![Screenshot_28](https://user-images.githubusercontent.com/122513124/227906264-02b4f5bb-3738-4968-b2de-20c06b91d173.jpg)

Копируем ссылку на страницу

![Screenshot_29](https://user-images.githubusercontent.com/122513124/227906629-31f5b93f-c260-4f68-832c-df90ba53f5a6.jpg)

Отправляем ссылку боту

![Screenshot_30](https://user-images.githubusercontent.com/122513124/227906734-b91d7882-00e5-436f-8780-fa5d502ce04e.jpg)

Бот будет мониторить новые объявления с только с этого момента. Для получения новых объявлений нужно попросить об этом бота голосом.

![Screenshot_31](https://user-images.githubusercontent.com/122513124/227907597-4f5eda1f-197d-47fe-af9f-b21f6d1bc778.jpg)
