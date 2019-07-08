import hashlib
import hmac
import logging
import os
import json
from urllib.parse import parse_qs

from docbot import commander


logger = logging.getLogger()
logger.setLevel(logging.WARNING)

''' Get the encrypted Signing Secret.'''
waanimals_slack_signing_secret = os.environ['SLACK_SIGNING_SECRET']

''' Get Environment.'''
environment = os.environ['STAGE']


''' Verify the POST request. '''


def verify_slack_request(slack_signature=None, slack_request_timestamp=None, request_body=None):
    ''' Form the basestring as stated in the Slack API docs. We need to make a bytestring. '''
    basestring = f"v0:{slack_request_timestamp}:{request_body}".encode('utf-8')

    ''' Make the Signing Secret a bytestring too. '''
    slack_signing_secret = bytes(waanimals_slack_signing_secret, 'utf-8')

    ''' Create a new HMAC "signature", and return the string presentation. '''
    my_signature = 'v0=' + \
        hmac.new(slack_signing_secret, basestring, hashlib.sha256).hexdigest()

    ''' Compare the the Slack provided signature to ours.
    If they are equal, the request should be verified successfully.
    Log the unsuccessful requests for further analysis
    (along with another relevant info about the request). '''
    if hmac.compare_digest(my_signature, slack_signature):
        return True
    else:
        logger.warning(f"Verification failed. my_signature: {my_signature}")
        return False


''' Process the POST request from API Gateway proxy integration. '''


def post(event, context):
    try:
        ''' Only perform validation on non testing environments '''
        if environment != "test":
            ''' Incoming data from Slack is application/x-www-form-urlencoded and UTF-8. '''
            ''' Capture the necessary data. '''
            slack_signature = event['headers']['X-Slack-Signature']
            slack_request_timestamp = event['headers']['X-Slack-Request-Timestamp']
            ''' Verify the request. '''
            if not verify_slack_request(slack_signature, slack_request_timestamp, event['body']):
                logger.info('Bad request.')
                response = {
                    "statusCode": 400,
                    "body": ''
                }
                return response

        ''' Ready Request Body '''
        body = parse_qs(event['body'])
        ''' Parse and handle command '''
        if body['command'][0] == "/docbot":
            command_response = commander.command_parse("/docbot", "")
        else:
            command_response = commander.command_parse(body['command'][0], body['text'][0])
        response = {
            "statusCode": 200,
            "body": json.dumps(command_response)
        }
        return response

    except Exception as e:
        ''' Just a stub. Please make this better in real use :) '''
        logger.error(f"ERROR: {e}")
        response = {
            "statusCode": 200,
            "body": ''
        }
        return response
