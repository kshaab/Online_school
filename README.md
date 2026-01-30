# Online School

### Проект образовательной платформы, разработанный на **Django**.  

### Проект в разработке.

## Содержание 

- [Использование](#использование)
- [Структура проекта](#структура-проекта)
- [Зависимости](#зависимости)
- [Celery](#celery-)
- [Docker](#docker-docker-compose)
- [Технологии](#технологии)
- [Тестирование](#тестирование)
- [Автор](#автор)


## Использование
Клонируйте репозиторий: 
```bash
git clone https://github.com/kshaab/Online_school
cd online_school
```
Установите зависимости и активируйте виртуальное окружение: 
poetry install
poetry shell

Примените миграции: 
python manage.py migrate

Запустите сервер разработки: 
python manage.py runserver


## Структура проекта

### online_school/
Основные настройки проекта и конфигурация Django. 

### lms/
Приложение обучающих материалов – курсы и уроки.

### users/
Приложение пользователей и платежей. 

## Зависимости
Управление зависимостями осуществляется через Poetry (pyproject.toml).
Основные зависимости:
- Django 5.x
- Celery 5.x
- PostgreSQL
- Redis (для Celery)

## Celery 
Проект использует Celery + Celery Beat для фоновых задач:
- Асинхронная рассылка уведомлений пользователям о новых материалах курсов.
- Фоновая проверка пользователей по дате последнего входа и автоматическая блокировка после месяца без активности.

## Docker (Docker Compose)

Клонируйте проект ([инструкция](#использование)).

1. Сборка и запуск контейнеров:
```bash
docker-compose up --build
```
2. Запуска проекта в фоне: 
```bash
docker-compose up -d
```
3. Проверка работы сервисов: 

a) Проверка всех сервисов:
```bash
docker-compose ps
```
Ожидаемый вывод сервисов: 
- web (Django),
- db (PostgreSQL),
- redis,
- celery,
- celery_beat.

б) Веб-сервис:

Запустите команду: 
```bash
docker-compose exec web python manage.py migrate
```
Проверьте доступность приложения в браузере:
```arduino
http://localhost:8000
```
в) PostgreSQL:

Используйте команду для подключения:
```bash
psql -h localhost -U <username> -d <database> 
```
Тестовая команда: 
```sql
SELECT 1;
```

г) Redis:

Выполните команду: 
```bash
docker-compose exec redis redis-cli ping
```
Ответ должен содержать 
```nginx
PONG
```

д) Celery:
Запуск логов воркеров:
```bash
docker-compose logs celery
```
В логах не должно содержаться ошибок.
4. Остановка проекта: 
```bash 
docker-compose down
```

## Тестирование
Запуск тестов:
```bash
poetry run python manage.py test
```

Запуска теста отдельного приложения(пример): 
```bash
poetry run python manage.py test lms
```

## Технологии
- Python 3.13

- Django 5.x

- PostgreSQL

- Redis 

- Docker

## Автор
[Ксения](https://github.com/kshaab)