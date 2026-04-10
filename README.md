# ML API для классификации Iris 

Простой REST API для предсказания вида ириса на основе его характеристик. Модель обучена на классическом датасете Iris с использованием Random Forest классификатора. API контейнеризирован с помощью Docker для простого развертывания.

Модель предсказывает один из трех видов ириса:
- **Setosa** (0)
- **Versicolor** (1)  
- **Virginica** (2)

## Технологии

- **Python** 3.11 - язык программирования
- **FastAPI** - веб-фреймворк для создания API
- **Scikit-learn** - библиотека для машинного обучения
- **Docker** - контейнеризация приложения
- **Uvicorn** - ASGI сервер
- **Joblib** - сохранение и загрузка модели

## Структура проекта
ml-fastapi-docker/
├── main.py # FastAPI приложение
├── train.py # Скрипт для обучения модели
├── model.joblib # Сохраненная обученная модель
├── requirements.txt # Python зависимости
├── Dockerfile # Инструкции для сборки Docker образа
└── README.md # Документация проекта


## Установка и запуск

### Локальный запуск

1. **Клонируй репозиторий:**
```bash
git clone <https://github.com/yanekissayabully/dockerXmachinelearning.git>
cd ml-fastapi-docker


bash
pip install -r requirements.txt


bash
python train.py


bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Открой в браузере: http://localhost:8000/docs

Запуск через Docker


bash
docker build -t ml-iris-api .


bash
docker run -d -p 8001:8000 --name ml-iris-container ml-iris-api


bash
docker ps


bash
docker logs ml-iris-container


bash
docker stop ml-iris-container


bash
docker rm ml-iris-container
API Эндпоинты
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
 Примеры использования
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



