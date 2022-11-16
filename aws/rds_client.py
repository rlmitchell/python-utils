
__module__     = 'aws/rds_client.py'
__description__ = ''
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__tested__     = 'Python 3.8.10'
__updated__    = '2022.11.12.1317'


import boto3
from datetime import datetime


class RDSClient:
    def __init__(self, db_identifier=None, aws_credentials={}):
        self.db_identifier = db_identifier 
        self.client = boto3.client('rds', 
                                   region_name = aws_credentials['region'],
                                   aws_access_key_id = aws_credentials['aws_access_key_id'],
                                   aws_secret_access_key = aws_credentials['aws_secret_access_key'])


    def get_manual_snapshots(self):
        if self.db_identifier == None:
            return None

        manual_snapshots = []
        for snapshot in self.client.describe_db_snapshots(SnapshotType='manual',DBInstanceIdentifier=self.db_identifier).get('DBSnapshots', None):
            if snapshot.get('SnapshotCreateTime',None):
                manual_snapshots.append( (snapshot['SnapshotCreateTime'], snapshot['DBSnapshotIdentifier'], snapshot['Status']) )
 
        manual_snapshots.sort()
        return manual_snapshots

    def get_instance_names(self):
        instance_name_list = [instance['DBInstanceIdentifier'] for instance in self.client.describe_db_instances().get('DBInstances', None)]
        return tuple(set(instance_name_list))

    def delete_manual_snapshot(self, snapshot_identifier):
        if self.db_identifier == None:
            return None

        response = self.client.delete_db_snapshot(DBSnapshotIdentifier=snapshot_identifier)
        return response

    def create_manual_snapshot(self, snapshot_identifier):
        if self.db_identifier == None:
            return None

        response = self.client.create_db_snapshot( DBInstanceIdentifier=self.db_identifier, DBSnapshotIdentifier=snapshot_identifier)
        return response

