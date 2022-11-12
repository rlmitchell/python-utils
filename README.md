# python-utils

- aws/rds_utils.py - AWS RDS utility classes

### Using aws/rds_utils

&nbsp;

#### Create a RDS manual snapshot 

```python
from pprint import pprint 
from aws.rds_utils import AWSRDSManualSnapshotCreate

response = AWSRDSManualSnapshotCreate('mydb','mydb-20221112-1626')()
pprint(response)

```

Output:
```bash
$ python3 example-creating-manual-snapshot.py 
{'DBSnapshot': {'AllocatedStorage': 40,
                'AvailabilityZone': 'us-east-1d',
                'DBInstanceIdentifier': 'mydb',
                'DBSnapshotArn': 'arn:aws:rds:us-east-1:253112801469:snapshot:mydb-20221112-1626',
                'DBSnapshotIdentifier': 'mydb-20221112-1626',
                'DbiResourceId': 'db-JKZYPYF5GOPBY3UN5JBENVDKYE',
                'Encrypted': True,
                'Engine': 'mariadb',
                'EngineVersion': '10.5.13',
                'IAMDatabaseAuthenticationEnabled': False,
                'InstanceCreateTime': datetime.datetime(2021, 12, 1, 22, 25, 40, 787000, tzinfo=tzutc()),
                'KmsKeyId': 'arn:aws:kms:us-east-1:253112801469:key/e5df-2a20-485-a1e-292179c',
                'LicenseModel': 'general-public-license',
                'MasterUsername': 'root',
                'OptionGroupName': 'default:mariadb-10-5',
                'PercentProgress': 0,
                'Port': 3306,
                'ProcessorFeatures': [],
                'SnapshotType': 'manual',
                'Status': 'creating',
                'StorageType': 'gp2',
                'VpcId': 'vpc-0bdbbea1'},
 'ResponseMetadata': {'HTTPHeaders': {'content-length': '1618',
                                      'content-type': 'text/xml',
                                      'date': 'Sat, 12 Nov 2022 22:26:37 GMT',
                                      'strict-transport-security': 'max-age=31536000',
                                      'x-amzn-requestid': '3dbd0523-3d54-4cd7-aa1a-80374dc77f81'},
                      'HTTPStatusCode': 200,
                      'RequestId': '3dbd0523-3d54-4cd7-aa1a-80374dc77f81',
                      'RetryAttempts': 0}}
$ 
```

&nbsp;

#### Listing RDS manual snapshots 

example-listing-manual-snapshots.py
```python 
from pprint import pprint 
from aws.rds_utils import AWSRDSManualSnapshotsList 

snapshots = AWSRDSManualSnapshotsList('mydb')() 
pprint(snapshots)
```

Output:
```bash
$ python example-listing-manual-snapshots.py 
[(datetime.datetime(2022, 11, 12, 18, 47, 49, 922000, tzinfo=tzutc()),
  'mydb-20221112d',
  'available'),
 (datetime.datetime(2022, 11, 12, 22, 11, 48, 712000, tzinfo=tzutc()),
  'mydb-20221112-1611',
  'available'),
 (datetime.datetime(2022, 11, 12, 22, 15, 49, 792000, tzinfo=tzutc()),
  'mydb-20221112-1614',
  'available'),
 (datetime.datetime(2022, 11, 12, 22, 27, 12, 901000, tzinfo=tzutc()),
  'mydb-20221112-1626',
  'available')]
$
```


#### Delete RDS manual snapshot 




#### Purge oldest N RDS manual snapshots 



