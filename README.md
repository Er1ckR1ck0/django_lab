# Как делалась данная лабораторная работа
### Шаг 1. Создаём проект
```bash
uv init
uv venv
uv add django
pip install django
django-admin startproject mysite
```
После создания проекта, как только мы инициализировали её в нашей директории. Далее мы начинаем работать с менеджером проекта через модуль `manager.py`
```bash
python mysite/manage.py startapp polls
```
### Шаг 2. Редактируем models.py
После создания polls (названием данной директории может быть иным) мы видим файл `models.py`
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    content = models.TextField()
    data_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
```
### Шаг 3. Создание миграции
Остаётся обычный запуск следующих команд
```bash
python mysite/manage.py makemigrations
python mysite/manage.py migrate
```
#### Вывод программы:
```bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```