# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Копируем файлы в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Flask
EXPOSE 5000

# Запускаем Flask приложение
CMD ["python", "log_receiver.py"]
