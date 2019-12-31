import logging
import threading

from pyopencl.tools import get_gl_sharing_context_properties
import pyopencl as cl

logger = logging.getLogger(__name__)

class OpCookingQueue(object):
	def __init__(self, op):
		self.root_op = op
		self.op_queues = [] # queue of queues
		self._build()

	def cook(self, lock, op):
		op.signals.opCookingStarted.emit()
		if not op.cookData(lock, context={}):
			op.signals.opCookingFailed.emit()
		else:
			op.signals.opCookingDone.emit()

	def execute(self, frame_range=(), blocking=True):
		for queue in self.op_queues:
			logger.debug("Executing queue: %s" % [op.path() for op in queue])

			lock = threading.Lock()
			threads = [threading.Thread(target=self.cook, args=(lock,op)) for op in queue]
			
			# Run processes
			for t in threads:
				t.start()

			if blocking:
				# Exit the completed processes
				for t in threads:
					t.join()

	def _build(self):
		'''
		we build actual queue here based on nodes dependencies
		'''
		self.op_queues.insert(0,[self.root_op])
		input_ops_to_cook = [input_op for input_op in self.root_op.inputs() if input_op and input_op.needsToCook()]
		while input_ops_to_cook:
			self.op_queues.insert(0, input_ops_to_cook)
			input_ops_to_cook = []
			for op in self.op_queues[0]:
				input_ops_to_cook += [input_op for input_op in op.inputs() if input_op and input_op.needsToCook()]

		# print queue start to get idead how it looks and works
		queue_stat = "Builded OpCookingQueue queues stucture is:\n"
		i = 0
		for queue in self.op_queues:
			queue_stat += "Queue %s: %s\n" % (i, [op.path() for op in queue])

			i+=1

		logger.debug(queue_stat)


