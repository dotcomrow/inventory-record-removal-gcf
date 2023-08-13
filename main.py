import json
import base64
from google.cloud import bigquery
from google.cloud.bigquery import Table
import google.cloud.logging
import logging

logClient = google.cloud.logging.Client()
client = bigquery.Client()
logClient.setup_logging()

def main(data, context):
    try:
        obj = json.loads(base64.b64decode(str(data['data'])))
        logging.info("Data: {}".format(obj))
        
        
    except Exception as e:
        logging.error("Error: {}".format(e))