#Queue using the DLL
from DLListNode import DLListNode

class LRUQueue:
	def __init__(self):
		#front_ and rear_ will be head nodes
		self.front_ = DLListNode(None)
		self.rear_ = DLListNode(None)
		self.front_.set_next(self.rear_)

	def enqueue(self, url = None, ip_add = None):
		#enqueue will always be possible, the LRU class handles the size
		newNode = DLListNode(url, ip_add)
		rearNode = self.rear_.get_prev()
		rearNode.set_next(newNode)
		self.rear_.set_prev(newNode)
		#the pointer to new node is needed for hashing
		return newNode

	def dequeue(self):
		#pops one off from the front
		retNode = None
		if (self.front_.get_next() != self.rear_):
			retNode = self.front_.get_next()
			self.front_.set_next(retNode.get_next())
			retNode.set_next(None)
			retNode.set_prev(None)
		else:
			print("Queue is empty")
		return retNode

	def restack(self, hereNode):
		#places hereNode to the front, regardless of location of hereNode
		prevNode = hereNode.get_prev()
		prevNode.set_next(hereNode.get_next())
		#prev and next node are at worst the head nodes, so they are never None
		rearNode = self.rear_.get_prev()
		rearNode.set_next(hereNode)
		self.rear_.set_prev(hereNode)

	def run_thru(self):
		#prints the contents of the queue, used for debugging
		current = self.front_.get_next()
		while (current != self.rear_):
			print(current.get_url() + ":" + current.get_ip())
			current = current.get_next()
