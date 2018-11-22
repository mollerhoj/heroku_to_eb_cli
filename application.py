from flask import Flask
import boto3
import pickle
import datetime
import os
from logging.handlers import RotatingFileHandler
import logging

application = Flask(__name__)
application.debug = True

# Example of logging
log_location = 'info.log'
if os.environ['FLASK_ENV'] == 'production':
    log_location = '/opt/python/log/application.log'

logHandler = RotatingFileHandler(log_location, maxBytes=1000, backupCount=0)
application.logger.addHandler(logHandler)
logHandler.setLevel(logging.DEBUG)
application.logger.setLevel(logging.DEBUG)

@application.route('/log', methods=['GET'])
def log():
    timestring = f"{datetime.datetime.now()}"
    application.logger.info(timestring)
    return timestring

# Example of using S3
s3 = boto3.client('s3')
bucket_name = 'elasticbeanstalk-heroku-to-eb-cli-data'
identifier = "data"
@application.route('/save', methods=['GET'])
def save():
    timestring = f"{datetime.datetime.now()}"
    data = pickle.dumps(timestring)
    s3.put_object(Body=data, Bucket=bucket_name, Key=identifier)
    return timestring

@application.route('/load', methods=['GET'])
def load():
    data = s3.get_object(Bucket=bucket_name, Key=identifier)
    timestring = pickle.loads(data['Body'].read())
    return timestring

# Default
@application.route('/', methods=['GET'])
def hello():
    return 'Hello world'

if __name__ == '__main__':
    application.run()
