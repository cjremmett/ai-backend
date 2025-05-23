FROM python:3.13
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
WORKDIR /code/app
CMD ["uvicorn", "main:socket_app", "--host", "0.0.0.0", "--port", "3101"]