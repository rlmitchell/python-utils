
__module__     = 'aws/'
__description__ = ''
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__tested__     = 'Python 3.8.10'
__updated__    = '2022.11.12.1317'


import boto3
from aws.rds_client import RDSClient


class AWSRDSManualSnapshotsList:
    def __init__(self, db_identifier, aws_credentials={}):
        self.client = RDSClient(db_identifier=db_identifier, aws_credentials=aws_credentials)

    def __call__(self):
        return self.client.get_manual_snapshots()


