import logging

logger = logging.getLogger(__name__)

class OpDataCache():
	'''
	Implements simplest possible cache for cooked op data
	'''
	def __init__(self, maxsize=None):
		self.__max_size__ = maxsize
		self.__data_dict__ = {}

	def putData(self, node, data_index, data):
		logger.debug("Putting data %s of node %s with index %s into cache" % (data.__cls__, node.path(), data_index))
		key = (node.uuid(), data_index)
		self.__data_dict__[key] = data

	def getData(self, node, data_index):
		logger.debug("Getting data of node %s with index %s from cache" % (node.path(), data_index))
		key = (node.uuid(), data_index)
		if key not in self.__data_dict__:
			logger.error("Cache miss for data of node %s with index %s" % (node.path(), data_index))
		return self.__data_dict__[key]