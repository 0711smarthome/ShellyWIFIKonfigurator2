FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir Flask pydbus requests

CMD ["python3", "shelly_configurator.py"]