# Daily Coding Problem # 810

# Problem:
# In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".
# Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
# For example, given the following tree:
#        1
#     /     \
#   2         3
#  / \       / \
# 4   5     6   7
# You should return [1, 3, 2, 4, 5, 6, 7].

class Node:
	def __init__(self, val: int, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def boustrophedon(tree: Node):
	if not tree:
		return []

	cur_level = [tree]
	next_level = []
	res_list = []

	left_right = True

	while cur_level:
		cur_node = cur_level.pop()
		res_list.append(cur_node.val)

		if left_right:
			if cur_node.left:
				next_level.append(cur_node.left)
			if cur_node.right:
				next_level.append(cur_node.right)
		else:
			if cur_node.right:
				next_level.append(cur_node.right)
			if cur_node.left:
				next_level.append(cur_node.left)

		if not cur_level:
			cur_level = next_level
			next_level = []
			left_right = not left_right

	return res_list


# ----------------------------------------------------------------------------
# Testing

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(boustrophedon(tree) == [1, 3, 2, 4, 5, 6, 7])		# True

tree = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10), Node(11))), Node(3, Node(6, Node(12), Node(13)), Node(7, Node(14), Node(15))))
print(boustrophedon(tree) == [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8])		# True

