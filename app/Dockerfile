FROM python:3.6

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY get_sys_time.py .

EXPOSE 8000
CMD ["python", "get_sys_time.py", "runserver", "0.0.0.0:8000"]
