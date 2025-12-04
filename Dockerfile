FROM apache/airflow:2.8.1-python3.8

# сначала ставим системные пакеты как root
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       wget \
       unzip \
       gnupg \
    && rm -rf /var/lib/apt/lists/*

# переключаемся на airflow ПЕРЕД pip install
USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
