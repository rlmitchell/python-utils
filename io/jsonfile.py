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


