# Daily Coding Problem # 797

# Problem:
# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
# Example:
# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
# [a, b] < [c, d]
# If a < c OR a==c AND b < d.



def isPrime(n):
	k = 3
	while k*k <= n:
		if n % k == 0:
			return False
		k += 2
	
	return True


def two_primes(n):
	# n is even number >= 4

	if n == 4:
		return (2, 2)
	
	for i in range(3, n//2 + 1, 2):
		num1 = i
		num2 = n - i
		
		if isPrime(num1):
			if num1 == num2 or isPrime(num2):
				return (num1, num2)


# ----------------------------------------------------------------------------
# Testing

print(two_primes(4) == (2, 2))		# True
print(two_primes(6) == (3, 3))		# True
print(two_primes(8) == (3, 5))		# True
print(two_primes(10) == (3, 7))		# True
print(two_primes(12) == (5, 7))		# True
print(two_primes(14) == (3, 11))	# True
print(two_primes(16) == (3, 13))	# True