FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' webuser
RUN mkdir -p /app/staticfiles && chown -R webuser:webuser /app
USER webuser

CMD ["gunicorn", "movies_project.wsgi:application", "--bind", "0.0.0.0:8000"]