FROM python:3.10.1-alpine
WORKDIR '/user/app'
COPY requirements.txt .
RUN apk add --update git
RUN pip install -r requirements.txt
COPY . .
RUN python setup.py install
ENV FLASK_APP='flask_app.app'
EXPOSE 5000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
