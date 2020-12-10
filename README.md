# Скрепер объявление с сайта Auto.ru
Помогает собрать данные с сайта Auto.ru.

# Requirements
Перечень всех зависимостей в `requirements.txt`
```
appnope==0.1.0
attrs==19.3.0
autoscraper==1.1.10
backcall==0.2.0
beautifulsoup4==4.9.3
bleach==3.1.5
...
```

# Использование

# Config
Скрепере настроивается через конфиг - `settings.json`.
    Параметры в конфиге:
    `max_page` - максимальная страница, до который будет скрепить приложение.
    `page_sleep_time` - задержка после скрепинга странице поиска. Нужна, чтобы обойти throttling. Без задержке могут *забанить*, но сам не проверял.
    `item_sleep_time` - задержка после скрепинга странице объявления с деталями. Нужна, чтобы обойти throttling. Без задержке могут **забанить**, но сам не проверял.
    `df_name` - настройка названия output csv файла.