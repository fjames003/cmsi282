def has_subset_sum(register, amount):
	register.sort()
	if amount == 0:
		return True

	flipped = False
	if amount < 0:
		amount = abs(amount)
		flipped = True


	neg_nums, pos_nums = all_one_sign(register, 'neg'), all_one_sign(register, 'pos')
	## pos_memo = [[False for x in range(amount + 1)] for x in range(len(pos_nums) + 1)]
	pos_dic = {}
	for x in range((amount + 1) * -1, amount + 1):
		for y in range(len(pos_nums) + 1):
			if str(x) not in pos_dic:
				pos_dic[str(x)] = {}
			pos_dic[str(x)][str(y)] = False
	neg_memo = [[False for x in range(amount + 1)] for x in range(len(neg_nums) + 1)]

	build_table(neg_memo, neg_nums, amount, 1)

	for col in range(-1 * (amount + 1), amount + 1):
		if pos_nums[0] == col or neg_memo[len(neg_nums)][col]:
			pos_dic['1'][str(col)] = True
		elif col > pos_nums[0] and neg_memo[len(neg_nums)][col - pos_nums[0]]:
			pos_dic['1'][str(col)] = True
		elif col < pos_nums[0]:
			pos_dic['1'][str(col)] = neg_memo[len(neg_nums)][abs(col) - pos_nums[0]]
		else:
			pos_dic['1'][str(col)] = False

	build_dic(pos_dic, pos_nums, amount, 2)


	if flipped:
		return neg_memo[len(neg_nums)][amount]
	else:
		return pos_dic[str(len(pos_nums))][str(amount)]
	
def build_table(table, numbers, amount, row_start):
	for row in range(row_start, len(numbers) + 1):
			for col in range(1, amount + 1):
				if numbers[row - 1] == col or table[row - 1][col]:
					table[row][col] = True
				elif col > numbers[row - 1] and table[row - 1][col - numbers[row - 1]]:
					table[row][col] = True
				else:
					table[row][col] = False
	return table

def build_dic(dictionary, numbers, amount, row_start):
	for row in range(row_start, len(numbers) + 1):
			for col in range(-1 * (amount + 1), amount + 1):
				if numbers[row - 1] == col or dictionary[str(row - 1)][str(col)]:
					dictionary[str(row)][str(col)] = True
				elif col > numbers[row - 1] and dictionary[str(row - 1)][str(col - numbers[row - 1])]:
					dictionary[str(row)][str(col)] = True
				else:
					dictionary[str(row)][str(col)] = False
	return dictionary

def all_one_sign(sequence, sign):
	result = []
	for x in sequence:
		if sign == 'neg':
			if x < 0:
				result.append(abs(x))
		elif sign == 'pos':
			if x > 0:
				result.append(x)
		else:
			return result
	return result


my_list = [-3,-1,1,2]

print(has_subset_sum(my_list, 2), " : True --> 2")
print(has_subset_sum(my_list, -2), " : True --> -2")
print(has_subset_sum(my_list, 0), " : True --> 0")
print(has_subset_sum(my_list, 3), " : True --> 3")
print(has_subset_sum(my_list, -3), " : True --> -3")
print(has_subset_sum(my_list, -4), " : True --> -4")