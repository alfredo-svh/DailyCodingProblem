# Daily Coding Problem # 799

# Problem:
# Implement a PrefixMapSum class with the following methods:
#     insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
#     sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
# For example, you should be able to run the following code:
# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3
# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5

import re

# PrefixMapSum class created using a single dictionary.
# insert() -- O(1)
# sum() loops through every key in the dictioary to find prefixes using regex -- O(n)
class PrefixMapSumInefficient:
	def __init__(self) -> None:
		self.map = {}
	
	def insert(self, key, val):
		self.map[key] = val
	
	def sum(self, prefix):
		keys = self.map.keys()
		total = 0

		for k in keys:
			regex = re.search(f"^{prefix}", k)
			if regex.group(0):
				total += self.map[k]

		return total
# -----------------------------------------------------------------------------------

# Helper node class
class Node:
	def __init__(self, letter=None):
		self.letter = letter
		self.children = {}
		self.num = None

# PrefixMapSum class created using a trie-like structure
# insert() -- O(1)
# sum() -- Traverses the trie in average of O(log n) time--more efficiently than the previous implementation
class PrefixMapSum:
	def __init__(self) -> None:
		self.map = Node()
	
	def insert(self, key, val):
		cur_node = self.map

		for i in range(len(key)):
			c = key[i]

			if not c in cur_node.children:
				cur_node.children[c] = Node(c)

			cur_node = cur_node.children[c]

			# The leaves in our trie will be those with num != None
			if i == len(key) - 1:
				cur_node.num = val
	
	def sum(self, prefix):
		def _recursive_sum(cur_node):
			cur_sum = 0
			if cur_node.num != None:
				cur_sum = cur_node.num
			
			for child in cur_node.children.values():
				cur_sum += _recursive_sum(child)

			return cur_sum
			
		# Find the prefix first
		cur_node = self.map
		for c in prefix:
			if c not in cur_node.children:
				print("Error: prefix not in mapsum")
				return 0
			cur_node = cur_node.children[c]
		
		return _recursive_sum(cur_node)


# ----------------------------------------------------------------------------
# Testing

mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
print(mapsum.sum("col") == 3)	# True
mapsum.insert("column", 2)
print(mapsum.sum("col") == 5)	# True
mapsum.insert("collision", 7)
print(mapsum.sum("col") == 12)	# True
mapsum.insert("consonant", 2)
print(mapsum.sum("col") == 12)	# True
