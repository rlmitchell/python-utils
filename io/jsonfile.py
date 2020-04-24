
"""
__module__      = 'jsonfile.py'
__author__      = 'Rob Mitchell <rlmitchell@gmail.com>,<rob.mitchell@objectstream.com>'
__updated__     = '2020.04.23'
__version__     = '0.0.1'
__status__      = 'development'
"""

import json

class JSON(object):
	def __init__(self,filename):
		self.filename = filename

	def load(self):
		with open(self.filename) as fp:
			return json.load(fh)

	def save(self,data):
		with open(self.filename,'w') as fp:
			json.dump(data,fp,indent=4)


