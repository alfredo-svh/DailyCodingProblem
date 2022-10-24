# Daily Coding Problem # 809

# Problem:
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.


def is_valid(s):
	open_stack = []

	if not s or len(s) % 2 == 1:
		return False

	for c in s:
		if c == "(":
			open_stack.append("(")

		elif c == ")":
			if not open_stack or open_stack.pop() != "(":
				return False

		elif c == "{":
			open_stack.append("{")

		elif c == "}":
			if not open_stack or open_stack.pop() != "{":
				return False

		elif c == "[":
			open_stack.append("[")

		elif c == "]":
			if not open_stack or open_stack.pop() != "[":
				return False
			
		else:
			# Non-bracket character
			return False
	
	if open_stack:
		return False
	
	return True


# ----------------------------------------------------------------------------
# Testing

print(is_valid("([])[]({})"))	# True
print(is_valid("([)]"))			# False
print(is_valid("((()"))			# False