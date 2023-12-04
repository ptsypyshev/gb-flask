# Задание

Объедините студентов в команды по 2-5 человек в сессионных залах.

Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

# Страница с документацией
http://localhost:8000/docs

# Запросы, для CRUD операций
## Пользователи
### Создание
curl -X 'POST' 'http://localhost:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string123;ABC"
}'

### Чтение (получение)
curl -X 'GET' 'http://localhost:8000/users/1' \
  -H 'accept: application/json'  

curl -X 'GET' 'http://localhost:8000/users/' \
  -H 'accept: application/json'

### Обновление (редактирование)
curl -X 'PUT' 'http://localhost:8000/users/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string123;XYZ"
}'

### Удаление
curl -X 'DELETE' 'http://localhost:8000/users/?id=1' \
  -H 'accept: application/json'

## Товары
### Создание
curl -X 'POST' 'http://localhost:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "price": 1
}'

### Чтение (получение)
curl -X 'GET' 'http://localhost:8000/items/1' \
  -H 'accept: application/json'

curl -X 'GET' 'http://localhost:8000/items/' \
  -H 'accept: application/json'

### Обновление (редактирование)
curl -X 'PUT' 'http://localhost:8000/items/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Test",
  "description": "Test",
  "price": 5
}'

### Удаление
curl -X 'DELETE' 'http://localhost:8000/items/?id=1' \
  -H 'accept: application/json'

## Заказы
### Создание
curl -X 'POST' 'http://localhost:8000/orders/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": 2,
  "item_id": 2,
  "status": 3
}'

### Чтение (получение)
curl -X 'GET' 'http://localhost:8000/orders/1' \
  -H 'accept: application/json'

curl -X 'GET' 'http://localhost:8000/orders/' \
  -H 'accept: application/json'

### Обновление (редактирование)
curl -X 'PUT' 'http://localhost:8000/orders/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": 1,
  "item_id": 1,
  "status": 1
}'

### Удаление
curl -X 'DELETE' 'http://localhost:8000/orders/?id=1' \
  -H 'accept: application/json'