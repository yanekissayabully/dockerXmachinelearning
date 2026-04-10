# ML API для классификации Iris 🌸

Простой REST API для предсказания вида ириса на основе его характеристик. Модель обучена на классическом датасете Iris с использованием Random Forest классификатора. API контейнеризирован с помощью Docker для простого развертывания.

## 🎯 О проекте

Проект демонстрирует полный цикл разработки и развертывания ML сервиса:
1. Обучение модели классификации (Random Forest)
2. Создание REST API с помощью FastAPI
3. Контейнеризация приложения с Docker
4. Тестирование API через Swagger, cURL и Postman

Модель предсказывает один из трех видов ириса:
- **Setosa** (0)
- **Versicolor** (1)  
- **Virginica** (2)

## 🛠 Технологии

- **Python** 3.11 - язык программирования
- **FastAPI** - веб-фреймворк для создания API
- **Scikit-learn** - библиотека для машинного обучения
- **Docker** - контейнеризация приложения
- **Uvicorn** - ASGI сервер
- **Joblib** - сохранение и загрузка модели

## 📁 Структура проекта
ml-fastapi-docker/
├── main.py # FastAPI приложение
├── train.py # Скрипт для обучения модели
├── model.joblib # Сохраненная обученная модель
├── requirements.txt # Python зависимости
├── Dockerfile # Инструкции для сборки Docker образа
└── README.md # Документация проекта


## 📦 Предварительные требования

- **Python** 3.11 или выше
- **Docker** (для запуска в контейнере)
- **Git** (опционально)

## 🚀 Установка и запуск

### Локальный запуск

1. **Клонируй репозиторий:**
```bash
git clone <your-repo-url>
cd ml-fastapi-docker
Установи зависимости:

bash
pip install -r requirements.txt
Обучи модель:

bash
python train.py
Запусти API сервер:

bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Открой в браузере: http://localhost:8000/docs

Запуск через Docker
Собери Docker образ:

bash
docker build -t ml-iris-api .
Запусти контейнер:

bash
docker run -d -p 8001:8000 --name ml-iris-container ml-iris-api
Проверь, что контейнер работает:

bash
docker ps
Посмотри логи:

bash
docker logs ml-iris-container
Останови контейнер:

bash
docker stop ml-iris-container
Удали контейнер:

bash
docker rm ml-iris-container
📡 API Эндпоинты
GET /
Проверка работоспособности API.

Ответ:

json
{
    "message": "ML API is running",
    "status": "active"
}
GET /health
Проверка состояния модели.

Ответ:

json
{
    "status": "healthy",
    "model_loaded": true
}
POST /predict
Предсказание вида ириса на основе входных параметров.

Заголовки:

Content-Type: application/json

Тело запроса:

json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
Параметры:

Параметр	Тип	Описание	Диапазон
sepal_length	float	Длина чашелистика	4.0 - 8.0
sepal_width	float	Ширина чашелистика	2.0 - 4.5
petal_length	float	Длина лепестка	1.0 - 7.0
petal_width	float	Ширина лепестка	0.1 - 2.5
Ответ:

json
{
    "prediction": 0,
    "class_name": "setosa",
    "probabilities": {
        "setosa": 0.98,
        "versicolor": 0.01,
        "virginica": 0.01
    }
}
📝 Примеры использования
cURL
GET запрос:

bash
curl http://localhost:8001/
POST запрос (Windows PowerShell):

powershell
curl -X POST "http://localhost:8001/predict" `
  -H "Content-Type: application/json" `
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
POST запрос (Linux/Mac):

bash
curl -X POST "http://localhost:8001/predict" \
  -H "Content-Type:application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
Python
python
import requests

# URL твоего API
url = "http://localhost:8001/predict"

# Данные для предсказания
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# Отправка POST запроса
response = requests.post(url, json=data)

# Вывод результата
if response.status_code == 200:
    result = response.json()
    print(f"Предсказанный класс: {result['class_name']}")
    print(f"Вероятности: {result['probabilities']}")
else:
    print(f"Ошибка: {response.status_code}")
Postman
Создай новый запрос

Выбери метод POST

Введи URL: http://localhost:8001/predict

Перейди во вкладку Body → raw → JSON

Вставь JSON данные:

json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
Нажми Send

🧪 Тестирование
Тестовые примеры
Пример 1 - Setosa:

json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
Пример 2 - Versicolor:

json
{
    "sepal_length": 6.5,
    "sepal_width": 2.8,
    "petal_length": 4.6,
    "petal_width": 1.5
}
Пример 3 - Virginica:

json
{
    "sepal_length": 7.2,
    "sepal_width": 3.0,
    "petal_length": 6.0,
    "petal_width": 2.2
}
Проверка через Swagger UI
Запусти API

Открой браузер по адресу: http://localhost:8000/docs

Нажми на эндпоинт POST /predict

Нажми Try it out

Введи тестовые данные

Нажми Execute

⚠️ Возможные ошибки и их решение
Ошибка: "Port is already allocated"
Решение:

bash
# Проверь, какой процесс использует порт
netstat -ano | findstr :8000

# Останови конфликтующий контейнер
docker stop <container_name>
docker rm <container_name>

# Или используй другой порт
docker run -d -p 8001:8000 --name ml-iris-container ml-iris-api
Ошибка: "No module named 'numpy._core'"
Решение: Переобучи модель с совместимыми версиями:

bash
pip install scikit-learn==1.3.0 numpy==1.24.3
python train.py
docker build --no-cache -t ml-iris-api .
Ошибка: "Container name already in use"
Решение:

bash
# Удали существующий контейнер
docker rm ml-iris-container

# Или используй другое имя
docker run -d -p 8000:8000 --name ml-iris-container-new ml-iris-api
Ошибка: "Model not loaded"
Решение:

bash
# Проверь, существует ли файл модели
ls model.joblib

# Если нет - обучи модель
python train.py

# Пересобери Docker образ
docker build --no-cache -t ml-iris-api .
📄 Лицензия
Этот проект создан в учебных целях для демонстрации контейнеризации ML приложений.

👥 Автор
[Твое имя]

🙏 Благодарности
Scikit-learn за датасет Iris

FastAPI за отличный фреймворк

Docker за удобную контейнеризацию

🔗 Полезные ссылки
FastAPI документация

Scikit-learn документация

Docker документация

Uvicorn документация

📞 Поддержка
Если у тебя возникли проблемы:

Проверь логи контейнера: docker logs ml-iris-container

Проверь, что модель существует: ls model.joblib

Убедись, что порт свободен: netstat -ano | findstr :8000

Пересобери образ с флагом --no-cache

Happy Coding! 🚀
