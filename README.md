# API YaTube
API для проекта [YaTube](https://github.com/FlowHack/yatube)

## ***Технологии***
- Python 3.8
- Django
- Django REST Framework
- Django REST Framework SimpleJWT

## ***Запуск при помощи Python 3.8.****
Создайте виртуальное окружение, установите зависимости
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Выполните миграции, создайте суперпользователя, соберите статику
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py migrate
python manage.py collectstatic
```
Запустите сервер
```bash
python manage.py runserver
```

## ***Документация***
После запуска документация доступна по адресу
```
http://127.0.0.1:8000/redoc
```
