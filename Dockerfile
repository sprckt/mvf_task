FROM python:3.7-stretch

COPY requirements.txt /app/requirements.txt
COPY tests/ /app/tests/

RUN pip install -r /app/requirements.txt
COPY *.py /app/

WORKDIR /app

RUN ls -lha

CMD ["python", "./github_poller.py"]
