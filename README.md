# DNS_Cache
Python 3 Simulation of a DNS cache

This is mostly a practice in using LRU cache and DNS lookups in Python.  The LRU cache is composed of a queue and hash table.  The queue is composed of doubly linked list nodes and the hash table regualr linked list nodes.  

The doubly linked list nodes contain the domain name and its corresponding IP address.  The queue uses this DLL because the cache needs to be able to move its most recently used node to the rear of the queue so that any dequeue called is always the least recently used node.
Enqueuing, dequeuing, and restacking are all O(1) opertaions

The hash table is 3 times the maximum size of the cache just to avoid collisions.  However, if there are collisions, the hash table resolves them by chaining linked list nodes.  The linked list nodes in the hash table contain pointers to DLL nodes in the queue since the whole point of a cache is O(1) access.  This also eliminates the need to dequeue just to reach a certain node or the need to iterate through the queue to find a certain node (which is O(N)).
The table's highest probability of collision is .3 and insert, retrieve, and remove usually take O(1) time.

The DNS Server uses this cache to store domain names and IP_addresses, the original assignment only required the cache be a file on the system and of infinite size, which I thought was unrealistic for a cache (but it's okay because caching was not the focus of the original project).
