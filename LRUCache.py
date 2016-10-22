#LRU cache
from LRUQueue import LRUQueue
from LRUHash import LRUHash
from DLListNode import DLListNode

class LRUCache:
	def __init__(self, size = 0):
		self.q_ = LRUQueue()
		self.hash_ = LRUHash(size)
		self.max_size_ = size
		self.cur_size_ = 0

		#for debugging
		self.hits_ = 0
		self.misses_ = 0

	def query(self, url = None):
		#gets ip from url if it is stored here
		if (url == None):
			print("No URL provided")
			return None

		'''
		saves some work, but will only ever be used once in a cache's lifetime
		if (self.cur_size_ == 0):
			self.misses_ = self.misses_ + 1
			return None
		'''

		ipNode = self.hash_.retrieve(url)
		if (ipNode == None):
			self.misses_ = self.misses_ + 1
			return None
		else:
			self.hits_ = self.hits_ + 1
			#move the hit to the back of the queue, it is now most recently used
			self.q_.restack(ipNode)
			return ipNode.get_ip()


	def add(self, url = None, ip_add = None):
		#adds a url and IP address to the cache
		if (url == None or ip_add == None):
			print("Incomplete information, needs URL and IP")
			return

		if (self.cur_size_ == self.max_size_):
			#if cache if full, we must remove the LRU node first
			lruNode = self.q_.dequeue()

			if (self.hash_.remove(lruNode.get_url()) == None):
				print("Error removing entry")
				return
			self.cur_size_ = self.cur_size_ - 1

		newNode = self.q_.enqueue(url, ip_add)
		self.hash_.insert(newNode)
		self.cur_size_ = self.cur_size_ + 1

	def print_stats(self):
		print("Hits: " + self.hits_ + "\nMisses: " + self.misses_)
		
	def run_thru(self):
		#prints everything on the queue
		self.q_.run_thru()
