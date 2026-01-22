FROM python:3.11-slim

WORKDIR /app

# Копиране на requirements и инсталиране на зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копиране на приложението
COPY . .

# Команда по подразбиране
CMD ["python", "strategy_pattern.py"]
