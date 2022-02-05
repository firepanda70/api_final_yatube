# REST API для проекта Yatube

### Описание

API для взаимодействия с платформой [Yatube](https://github.com/firepanda70/yatube_project)

### Установка

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/firepanda70/api_final_yatube
cd api_final_yatube
```

- Cоздать и активировать виртуальное окружение:

```
python -m venv env
source venv/bin/activate
python -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

- Выполнить миграции:

```
python manage.py migrate
```

- Запустить проект:

```
python manage.py runserver
```

### Технологии:
- Python 3
- Django
- Django REST Framework
- SQLite3
- Simple-JWT
