# python-utils

clone repo to your $PYTHONPATH

&nbsp;





#### aws - create a RDS manual snapshot 

```python
from pprint import pprint 
from aws.rds_utils import AWSRDSManualSnapshotCreate

response = AWSRDSManualSnapshotCreate('mydb','mydb-20221112-1626')()
pprint(response['ResponseMetadata'])

```

Output:
```bash
$ python3 example-creating-manual-snapshot.py 
{'HTTPHeaders': {'content-length': '1618',
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

#### aws - listing RDS manual snapshots 

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

&nbsp;

#### aws - delete RDS manual snapshot 

```python
from pprint import pprint 
from aws.rds_utils import AWSRDSManualSnapshotDelete

response = AWSRDSManualSnapshotDelete('mydb-20221112d')()
pprint(response['ResponseMetadata'])
```

Output:
```bash
$ python3 example-deleting-manual-snapshot.py 
{'HTTPHeaders': {'content-length': '1771',
                 'content-type': 'text/xml',
                 'date': 'Sat, 12 Nov 2022 22:41:56 GMT',
                 'strict-transport-security': 'max-age=31536000',
                 'x-amzn-requestid': 'a9e85504-71b0-4342-b452-8d005089514c'},
 'HTTPStatusCode': 200,
 'RequestId': 'a9e85504-71b0-4342-b452-8d005089514c',
 'RetryAttempts': 0}}
$ 
```

&nbsp;

#### aws - purge oldest N RDS manual snapshots 

```python
from pprint import pprint 
from aws.rds_utils import AWSRDSManualSnapshotPurger

AWSRDSManualSnapshotPurger('mydb', num_keep=1)()
```

Output:
```bash
$ python3 example-purging-manual-snapshots.py 
delete: (datetime.datetime(2022, 11, 12, 22, 11, 48, 712000, tzinfo=tzutc()), 'mydb-20221112-1611', 'available')
delete: (datetime.datetime(2022, 11, 12, 22, 15, 49, 792000, tzinfo=tzutc()), 'mydb-20221112-1614', 'available')
$
```



