# python-utils

- aws/rds_utils.py - AWS RDS utility classes

### Using aws/rds_utils

#### Listing RDS manual snapshots 
```python 
from pprint import pprint 
from aws.rds_utils import AWSRDSManualSnapshotsList 

snapshots = AWSRDSManualSnapshotsList('mydb')() 
pprint(snapshots)
```

&nbsp; 

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
  'available')]
$
```


#### Delete RDS manual snapshot 


#### Create a RDS manual snapshot 


#### Purge oldest N RDS manual snapshots 



