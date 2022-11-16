
__module__     = ''
__description__ = ''
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__tested__     = 'Python 3.8.10'
__updated__    = '2022.11.12.1317'


import boto3


class SESClient:
    def __init__(self, aws_credentials={}):
        self.client = boto3.client('ses',
                                   region_name = aws_credentials['region'],
                                   aws_access_key_id = aws_credentials['aws_access_key_id'],
                                   aws_secret_access_key = aws_credentials['aws_secret_access_key'])

    def get_sent(self):
        return self.client.get_send_quota()['SentLast24Hours']

    def over_threshold(self, threshold=0):
        threshold = int(threshold)
        return int(self.get_sent()) > threshold


