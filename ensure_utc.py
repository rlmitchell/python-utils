__module__     = 'ensure_utc.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.9'
__version__    = '2021.04.01.1209'


import time


class EnsureUTC:
   def __init__(self):
      if time.tzname[0] != 'UTC':
         raise Exception('<EnsureUTC>: System is not set to UTC.')

   def __str__(self):
      return time.tzname[0]


if __name__ == '__main__':
	print( EnsureUTC() )
