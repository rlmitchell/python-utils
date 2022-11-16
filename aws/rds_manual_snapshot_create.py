
__module__     = ''
__description__ = ''
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__tested__     = 'Python 3.8.10'
__updated__    = '2022.11.12.1317'


from aws.rds_client import RDSClient


class AWSRDSManualSnapshotCreate:
    def __init__(self, db_identifier=None, snapshot_identifier=None, aws_credentials={}):
        self.client = RDSClient(db_identifier=db_identifier, aws_credentials=aws_credentials)
        self.snapshot_identifier = snapshot_identifier 

    def __call__(self):
        return self.create()

    def create(self):
        return self.client.create_manual_snapshot(self.snapshot_identifier)



