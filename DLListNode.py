#doubly linked list to build the queue of the LRU cache
#stores the ip address and domain name as well as points to previous and nex neighbors

class DLListNode:
	def __init__(self, url = None, ip_add = None):
		self.url_ = url
		self.ip_add_ = ip_add
		#don't initialize with any neighbors, the queue does that
		self.next_ = None
		self.prev_ = None

	def get_ip(self):
		return self.ip_add_

	def set_ip(self, ip_add = None):
		self.ip_add_ = ip_add

	def get_url(self):
		return self.url_

	def set_url(self, url = None):
		self.url_ = url

	def get_next(self):
		return self.next_

	#the set next and prev functions need to be a bit special
	def set_next(self, next = None):
		self.next_ = next
		if (next != None):
			next.prev_ = self

	def get_prev(self):
		return self.prev_

	def set_prev(self, prev = None):
		self.prev_ = prev
		if (prev != None):
			prev.next_ = self