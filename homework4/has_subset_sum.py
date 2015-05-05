
def has_subset_sum(sequence, amount):
	
	if amount == 0:
		return True

	sequence.sort()

	neg_sum = sum_of_nums(sequence, 'neg')
	pos_sum = sum_of_nums(sequence, 'pos')

	if amount > pos_sum or amount < neg_sum:
		return False

	memo = [[False for x in range(abs(neg_sum) + pos_sum + 1)] for x in range(len(sequence) + 1)]
	for row in  range(1, len(sequence) + 1):
		for col in range(0, abs(neg_sum) + pos_sum + 1):
			
			if sequence[row - 1] == neg_sum + col or memo[row - 1][col]:
				memo[row][col] = True
			elif memo[row - 1][(col - sequence[row - 1]) % (abs(neg_sum) + pos_sum)]:
				memo[row][col] = True
			else:
				memo[row][col] = False

	return memo[len(sequence)][amount + abs(neg_sum)]


def sum_of_nums(sequence, sign):
	result = 0
	if sign == 'neg':
		for x in sequence:
			if x < 0:
				result += x
	elif sign == 'pos':
		for x in sequence:
			if x > 0:
				result += x
	else:
		raise ValueError("Sign must be 'pos' or 'neg'")
	return result