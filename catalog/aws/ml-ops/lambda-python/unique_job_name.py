"""Return a unique job name by concatenating the JobName variable with the current timestamp."""
from datetime import datetime


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "JobName": event["JobName"] + "-" + datetime.today().strftime("%y%m%d%H%M%S"),
    }
