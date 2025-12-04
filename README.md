# CoinMarketCap mini pipeline

Курс: Data Collection & Preparation  
Тема: Сбор данных с динамического сайта, очистка и загрузка в SQLite, автоматизация через Airflow.

## Описание

Мы берём данные с сайта [https://coinmarketcap.com/](https://coinmarketcap.com/).  
Собираем топ 150 криптовалют, чистим данные и сохраняем их в базу `SQLite` в таблицу `crypto`.

Пайплайн состоит из трёх шагов:

1. `scraper.py` — сбор данных с помощью Selenium  
2. `cleaner.py` — очистка и приведение типов (Pandas)  
3. `loader.py` — загрузка данных в SQLite (`data/marketcap.db`)

Все три шага объединены в один DAG `coinmarketcap_pipeline` в Apache Airflow.

## Структура проекта

coinmarketcap_pipeline/
│   README.md                 
│   requirements.txt          
│   Dockerfile                 
│   docker-compose.yml         
│
├── dags/
│   └── airflow_dag.py         
│
├── src/
│   ├── scraper.py             
│   ├── cleaner.py             
│   └── loader.py              
│
└── data/
    └── marketcap.db           