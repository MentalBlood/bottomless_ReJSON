from .. import Call
from ..common import *
from .. import RedisInterface


class DeleteCall(Call):

	@property
	def root_key(self):
		return self.args[0]

	@property
	def path(self):
		return self.args[1]

	def getCorrect(self, db):
		return DeleteCall((self.method_name, (self.root_key, self.path)))
	
	# def getAdditionalCalls(self, db):

	# 	if self.root_key == 'index':
	# 		return []
		
	# 	indexes_calls = []
		
	# 	r = RedisInterface.RedisInterface(db, self.path, root_key=self.root_key)
	# 	r.addToIndexes(self.value, indexes_calls)
		
	# 	return indexes_calls
	
	def getPreparedArgs(self):
		return (self.root_key, composeRejsonPath(self.path))



import sys
sys.modules[__name__] = DeleteCall