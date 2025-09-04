Python virtual environment
```
python3 -m venv .venv
. ./.venv/bin/activate
```
---
Установка библиотек
```
pip install -r requirements.txt
```
---
Создаем файл ```.env``` и туда копируем все из ```.env.example```, заменяя токен на токен бота
---
Запуск бота:
```
python ./src/main.py
```