#LRU hash table using ListNodes
from ListNode import ListNode
from DLListNode import DLListNode

class LRUHash:
	def __init__(self, size = 0):
		#triple the size to avoid collisions
		self.size_ = size

		#these are all head nodes
		self.table_ = [ListNode() for i in range(size * 3)]

	def insert(self, dll_node = None):
		#always call retrieve() before insert, or else duplicates may be occur
		if (dll_node ==  None):
			print("Did not enter a DLL node")
			return
		url = dll_node.get_url()
		if (url == None):
			print("Did not enter a url")
			return

		#basic hashing stuff
		index = hash(url) % (self.size_ * 3)
		current = self.table_[index]

		#usually shouldn't go into else, so the insert should be pretty fast
		if (current.get_next() == None):
			current.set_next(ListNode(dll_node))
		else:
			while (current.get_next() != None):
				current = current.get_next()
			current.set_next(ListNode(dll_node))

	def retrieve(self, url = None):
		#returns dll_node with that url
		#returns None if not found
		if (url ==  None):
			print("Did not enter a url")
			return

		index = hash(url) % (self.size_ * 3)
		current = self.table_[index].get_next()

		if (current == None):
			return None
		currDLL = current.get_dll_node()
		while (currDLL.get_url() != url):
			current = current.get_next()

			if (current == None):
				return None
			currDLL = current.get_dll_node()
		return currDLL

	def remove(self, url):
		#should be called only when cache is full
		#returns the dll_node that was removed correctly
		#under the lru cache, it should never return None
		if (url ==  None):
			print("Did not get a url")
			return

		index = hash(url) % (self.size_ * 3)
		previous = self.table_[index]

		if (previous.get_next() == None):
			print("Error: URL not found in hash")
			return None

		current = previous.get_next()
		currDLL = current.get_dll_node()

		while (currDLL.get_url() != url):
			previous = current
			current = current.get_next()

			if (current == None):
				print("Error: URL not found in list")
				return None
			currDLL = current.get_dll_node()

		#simply skip over that node to delete it using the garbage collector
		previous.set_next(current.get_next())
		return currDLL
