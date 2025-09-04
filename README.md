Python virtual environment
```
python3 -m venv .venv
. ./.venv/bin/activate
```
---
Redis для линукса
```
sudo apt update && sudo apt install redis-server -y
sudo systemctl enable redis-server
sudo systemctl start redis-server
```
---
Установка библиотек
```
pip install -r requirements.txt
```