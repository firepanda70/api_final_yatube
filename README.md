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

- Добавьте переменные среды в файл .env:

```
DJANGO_KEY=SECRET
ALLOWED_HOSTS=localhost,127.0.0.1
```

- Выполнить миграции:

```
python manage.py migrate
```

- Загрузите тестовые данные:

```
python manage.py loaddata fixtures.json
# Суперюзер тестовых данных: admin
# Пароль: admin
```

- Запустить проект:

```
python manage.py runserver
```

### Использование:
<p>API не дает вохможности регистрации на платформе. Уже зарегестрированный пользователь может получить JWT-Токен по эндпоинту /api/v1/jwt/create/, после чего добавлять его в заголовках запроса.</p>

#### Некоторые из доступных эндпоинтов:
- /api/v1/posts/ (Методы GET, POST)
- /api/v1/posts/{post_id}/ (Методы GET, PUT, PATCH, DEL)
- /api/v1/posts/{post_id}/comments/ (GET, POST)
- /api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DEL)
- /api/v1/groups/ (Только GET)
- /api/v1/follow/ (GET, POST)

Подробная документация будет доступна по эндпоинту /redoc

### Технологии:

- Python 3
- Django
- Django REST Framework
- SQLite3
- Simple-JWT
