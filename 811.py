# Daily Coding Problem # 811

# Problem:
# Given a list of words, return the shortest unique prefix of each word. For example, given the list:
#     dog
#     cat
#     apple
#     apricot
#     fish
# Return the list:
#     d
#     c
#     app
#     apr
#     f


class Node:
	def __init__(self, letter=None):
		self.letter = letter
		self.children = {}
		self.leaf = False

	def insert(self, word):
		if not word:
			return
		
		cur_node = self

		for i in range(len(word)):
			c = word[i]

			if not c in cur_node.children:
				cur_node.children[c] = Node(c)

			cur_node = cur_node.children[c]

			# The leaves in our trie will be those with num != None
			if i == len(word) - 1:
				cur_node.leaf = True
	
	def search(self, word):
		cur_node = self
		cur_prefix = ""
		unique_prefix = ""

		for c in word:
			if c not in cur_node.children:
				return cur_prefix
			
			if len(cur_node.children) > 1:
				unique_prefix = cur_prefix + c

			cur_prefix += c
			cur_node = cur_node.children[c]
			
		
		return unique_prefix

def shortest_unique_prefix(words):
	trie = Node()
	res_list = []

	for word in words:
		trie.insert(word)

	for word in words:
		res_list.append(trie.search(word))
	
	return res_list

# ----------------------------------------------------------------------------
# Testing

words = ["dog", "cat", "apple", "apricot", "fish"]
print(shortest_unique_prefix(words) == ["d", "c", "app", "apr", "f"])	# True