FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# app.main 모듈의 app 객체를 실행한다고 가정
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]