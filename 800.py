# Daily Coding Problem # 800

# Problem:
# Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form.
# For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.


class Node:
	def __init__(self, val: int, nxt=None) -> None:
		self.val = val
		self.next = nxt
	
	def __str__(self) -> str:
		nxt = self.next
		lst_str = f"{self.val}"

		while nxt:
			lst_str += f" -> {nxt.val}"
			nxt = nxt.next
		
		return lst_str
	
	def alternate(self):
		# linked-list of length 1
		if not self.next:
			return

		prev = self
		cur = self.next

		while cur:
			nxt = cur.next
			if prev.val > cur.val:
				prev.val, cur.val = (cur.val, prev.val)

			if not nxt:
				break

			if cur.val < nxt.val:
				cur.val, nxt.val = (nxt.val, cur.val)
			
			prev = nxt
			cur = nxt.next

# ----------------------------------------------------------------------------
# Testing

ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
ll.alternate()
print(f"{ll}" == "1 -> 3 -> 2 -> 5 -> 4")			# True

ll = Node(1)
ll.alternate()
print(f"{ll}" == "1")	# True

ll = Node(1, Node(2))
ll.alternate()
print(f"{ll}" == "1 -> 2")		# True

ll = Node(2, Node(1))
ll.alternate()
print(f"{ll}" == "1 -> 2")		# True

ll = Node(9, Node(6, Node(8, Node(3, Node(7)))))
ll.alternate()
print(f"{ll}" == "6 -> 9 -> 3 -> 8 -> 7")			# True

ll = Node(6, Node(9, Node(3, Node(8, Node(7)))))
ll.alternate()
print(f"{ll}" == "6 -> 9 -> 3 -> 8 -> 7")			# True