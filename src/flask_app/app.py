from flask import Flask
from flask import request
from celery_worker import tasks


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/event', methods=['POST'])
def event():
    job = tasks.event.delay(request.get_json())
    return job.id


if __name__ == '__main__':
    app.run(debug=True)
