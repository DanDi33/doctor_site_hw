FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "doctor_site_hw.wsgi:application", "--bind", "0.0.0.0:8000"]