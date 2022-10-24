# Daily Coding Problem # 807

# Problem:
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring(s: str, k: int):
	if not s or k < 1:
		return ""
		
	longest_substr = ""
	cur_substr = ""
	cur_chars = {}
	cur_distinct = 0
	
	for c in s:
		cur_substr = cur_substr + c
		if not c in cur_chars:
			cur_chars[c] = 0
			
		if cur_chars[c] == 0:
			cur_distinct += 1
			cur_chars[c] = 1
		
		if cur_distinct > k:
			if len(cur_substr) > len(longest_substr):
				longest_substr = cur_substr[:-1]
			
			# shorten substring
			while cur_distinct > k:
				to_remove = cur_substr[0]
				cur_chars[to_remove] -= 1
				if cur_chars[to_remove] == 0:
					cur_distinct -= 1
				cur_substr = cur_substr[1:]
			
	if len(cur_substr) > len(longest_substr) and cur_distinct <= k:
		return cur_substr
		
	return longest_substr


# ----------------------------------------------------------------------------
# Testing

print(longest_substring("abcba", 2) == "bcb")	# True
print(longest_substring("abc", 3) == "abc")		# True
print(longest_substring("a", 2) == "a")			# True