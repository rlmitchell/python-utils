
__module__     = 'aws/'
__description__ = ''
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__tested__     = 'Python 3.8.10'
__updated__    = '2022.11.12.1317'


import boto3
from aws.rds_client import RDSClient
from pprint import pprint


class AWSRDSManualSnapshotsList:
    def __init__(self, db_identifier, access_key=None, secret_key=None, region=None):
        self.client = RDSClient(db_identifier=db_identifier, access_key=access_key, secret_key=secret_key, region=region)

    def __call__(self):
        return self.client.get_manual_snapshots()


