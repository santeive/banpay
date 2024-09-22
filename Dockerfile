FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

# collect static files
#RUN mkdir -p /app/staticfiles
#RUN python manage.py collectstatic --noinput

# run migrations
CMD ["python", "manage.py", "migrate"]

# Gunicorn config with 3 workers
ENTRYPOINT [ "gunicorn", "config.wsgi:application", "-b", "0.0.0.0:8000", "--workers", "3"]
