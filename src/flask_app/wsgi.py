"""
Sample data:
{
  "data": {
    "id": "95.0",
    "meta": {
      "type": "attribute_change",
      "entity_id": 758,
      "new_value": "This is the newest description ever!!",
      "old_value": "This is the old description!",
      "entity_type": "Asset",
      "attribute_name": "description",
      "field_data_type": "text"
    },
    "user": {
      "id": 113,
      "type": "HumanUser"
    },
    "entity": {
      "id": 758,
      "type": "Asset"
    },
    "project": {
      "id": 65,
      "type": "Project"
    },
    "operation": "update",
    "created_at": "2019-07-12 21:14:36.598835",
    "event_type": "Shotgun_Asset_Change",
    "session_uuid": "07473c00-a4ea-11e9-b3b8-0242ac110006",
    "attribute_name": "description",
    "event_log_entry_id": 248249
  }
}
"""


import socket
from flask import Flask
from flask import request
from celery_worker import tasks


app = Flask(__name__)


@app.route('/')
def index():
    return f'Hello World! {socket.gethostname()}'


@app.route('/event', methods=['POST'])
def event():
    job = tasks.event.delay({
        'data': request.get_json(),
        'hostname': {socket.gethostname()}})

    return job.id


if __name__ == '__main__':
    app.run(debug=True)
