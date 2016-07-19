from pyopencl.tools import get_gl_sharing_context_properties
import threading
import logging
import pyopencl as cl

class OpCookingQueue(object):
	def __init__(self, op):
		self.root_op = op
		self.op_queues = []
		self._build()

	def cook(self, lock, op):
		return op.cookData(lock)

	def execute(self, frame_range=()):
		print "Executing queues:"
		for queue in self.op_queues:
			print "Executing queue: %s" % [op.path() for op in queue]

			lock = threading.Lock()
			threads = [threading.Thread(target=self.cook, args=(lock,op)) for op in queue]
			
			# Run processes
			for t in threads:
				t.start()

			# Exit the completed processes
			for t in threads:
				t.join()

			# Get process results from the output queue
			#results = [output.get() for p in processes]
			#print "Queue results: %s" % results

	def _build(self):
		'''
		we build actual queue here based on nodes dependencies
		'''
		self.op_queues.insert(0,[self.root_op])
		input_ops_to_cook = [input_op for input_op in self.root_op.inputs() if input_op.needsToCook()]
		while input_ops_to_cook:
			self.op_queues.insert(0, input_ops_to_cook)
			input_ops_to_cook = []
			for op in self.op_queues[0]:
				input_ops_to_cook += [input_op for input_op in op.inputs() if input_op.needsToCook()]

		# print queue start to get idead how it looks and works
		queue_stat = "Builded OpCookingQueue queues stucture is:\n"
		i = 0
		for queue in self.op_queues:
			queue_stat += "Queue %s: %s\n" % (i, [op.path() for op in queue])

			i+=1

		print queue_stat


