FROM python:3.7-stretch

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY *.py /app/
COPY tests/ /app/tests/

WORKDIR /app

CMD ["python", "./github_poller.py"]
