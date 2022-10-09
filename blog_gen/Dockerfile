FROM python:alpine3.16

WORKDIR /usr/src/api

COPY Pipfile ./

RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv install

COPY . .

EXPOSE 5000

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]