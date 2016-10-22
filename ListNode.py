#linked list for hash table of the LRU cache
#because the cache resolves collisions by chaining
#the nodes are meant to store the pointers to DLL Nodes for quick access
#this class can be used for other stuff since it's really just a  basic linked list
from DLListNode import DLListNode

class ListNode:
	def __init__(self, dll_node = None):
		self.dll_node_ = dll_node
		self.next_ = None

	def get_dll_node(self):
		return self.dll_node_

	#this will probably never be used
	def set_dll_node(self, node = None):
		self.dll_node_ = node

	def get_next(self):
		return self.next_

	def set_next(self, next = None):
		self.next_ = next