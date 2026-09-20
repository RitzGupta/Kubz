FROM python:3.12-slim

WORKDIR /usr/src/app

# Requirements first, so dependency layers cache across code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "./app.py"]
