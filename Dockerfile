FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
RUN pip install apscheduler

COPY . .

CMD ["python", "app.py"]

