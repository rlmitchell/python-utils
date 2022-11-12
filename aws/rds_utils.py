
__module__     = 'aws/rds_utils.py'
__description__ = 'AWS RDS utility classes'
__maintainer__ = 'Rob Mitchell <rlmitchell@gmail.com>'
__tested__     = 'Python 3.8.10'
__updated__    = '2022.11.12.1317'


import boto3
from pprint import pprint


class RDSClient:
    def __init__(self, DBIdentifier=None, access_key=None, secret_key=None, region=None):
        if not access_key:
            self.client = boto3.client('rds')
        else:
            self.client = boto3.client('rds', 
                                       region_name = region,
                                       aws_access_key_id = access_key,
                                       aws_secret_access_key = secret_key)

        self.db_identifier = DBIdentifier 

    def get_manual_snapshots(self):
        if self.db_identifier == None:
            return None
        manual_snapshots = []
        for snapshot in self.client.describe_db_snapshots(SnapshotType='manual',DBInstanceIdentifier=self.db_identifier).get('DBSnapshots', None):
            manual_snapshots.append( (snapshot['SnapshotCreateTime'], snapshot['DBSnapshotIdentifier'], snapshot['Status']) )
        manual_snapshots.sort()
        return manual_snapshots

    def get_instance_names(self):
        instance_name_list = []
        instances = self.client.describe_db_instances().get('DBInstances', None)    #MaxRecords defaults to 100
        for instance in instances:
            instance_name_list.append( instance['DBInstanceIdentifier'] )
        return tuple(set(instance_name_list))

    def delete_manual_snapshot(self, snapshot_identifier):
        response = self.client.delete_db_snapshot(DBSnapshotIdentifier=snapshot_identifier)
        return response

    def create_manual_snapshot(self, snapshot_identifier):
        response = self.client.create_db_snapshot( DBInstanceIdentifier=self.db_identifier, DBSnapshotIdentifier=snapshot_identifier)
        return response


class AWSRDSManualSnapshotsList:
    def __init__(self, DBIdentifier, access_key=None, secret_key=None, region=None):
        self.client = RDSClient(DBIdentifier, access_key=access_key, secret_key=secret_key, region=region)

    def __call__(self):
        return self.client.get_manual_snapshots()

    def print(self):
        pprint(get_manual_snapshots())


class AWSRDSManualSnapshotDelete:
    def __init__(self, snapshot_identifier, access_key=None, secret_key=None, region=None):
        self.client = RDSClient(DBIdentifier, access_key=access_key, secret_key=secret_key, region=region)
        self.snapshot_identifier = snapshot_identifier

    def __call__(self):
        return self.delete()

    def delete(self):
        return self.client.delete_manual_snapshot(self.snapshot_identifier)


class AWSRDSManualSnapshotPurger:
    def __init__(self, DBIdentifier, num_keep, access_key=None, secret_key=None, region=None):
        self.client = RDSClient(DBIdentifier, access_key=access_key, secret_key=secret_key, region=region)
        self.number_to_keep = num_keep

    def __call__(self):
        self.purge_snapshots()

    def purge_snapshots(self):
        snapshots = list(self.client.get_manual_snapshots())
        while len(snapshots) > self.number_to_keep:
            del_snapshot = snapshots.pop(0)
            print('delete: ' + str(del_snapshot))
            self.client.delete_manual_snapshot(del_snapshot[1])


class AWSRDSManualSnapshotCreate:
    def __init__(self, DBIdentifier, snapshot_identifier, access_key=None, secret_key=None, region=None):
        self.client = RDSClient(DBIdentifier, access_key=access_key, secret_key=secret_key, region=region)
        self.snapshot_identifier = snapshot_identifier 

    def __call__(self):
        return self.create()

    def create(self):
        return self.client.create_manual_snapshot(self.snapshot_identifier)

