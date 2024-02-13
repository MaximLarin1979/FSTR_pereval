Описание проекта:
API мобильного приложения Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework.

Задача:
Создать REST API для мобильного приложения для туристов, должны быть реализованы возможности для добавления информации о перевале с заданными параметрами, просмотра детальной информации о перевале, редактирование данных перевала, а также вывод списка перевалов, добавленных конкретным пользователем с идентификацией по его адресу электронной почты.

Технологии, используемые в процессе реализации проекта:
Python
Django
Pycharm
Postgres
Swagger

Документация OpenAPI на Swagger: https://github.com/MaximLarin1979/FSTR_pereval/tree/master/swagger_documentation
Схема OpenAPI на YAML: https://github.com/MaximLarin1979/FSTR_pereval/blob/master/static/openapi-schema.yaml

Классы/методы:
1. Класс: SubmitDataApi	Метод: submit_data_create	Тип HTTP-запроса: POST /submitData	Действие: Добавление перевала
2. Класс: SubmitDataApi	Метод: submit_data_partial_update	Тип HTTP-запроса: PATCH /submitData/{id}/	Действие: Редактирование перевала
3. Класс: SubmitDataApi	Метод: submit_data_retrieve	Тип HTTP-запроса: GET /submitData/{id}/	Действие: Извлечение данных о перевале
4. Класс: SubmitDataApi	Метод: submit_data_user_email_list	Тип HTTP-запроса: GET /submitData/user__email={email}	Действие: Извлечение списка перевалов пользователя

Инструкция по установке:
1. Клонируете репозиторий git clone https://github.com/MaximLarin1979/FSTR_pereval.git
2. Уставливаете зависимости
3. Наслаждаетесь результатом
Необходимые библиотеки указаны в файле https://github.com/MaximLarin1979/FSTR_pereval/blob/master/requirements.txt

Лицензия:
Лицензия не требуется. Проект может быль использован без ограничений.

Деплой на хостинге timeweb.cloud:
https://2510750-yo82697.twc1.net/api/v1/submitData

Автор:
Максим Ларин
https://github.com/MaximLarin1979
