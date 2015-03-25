
def insertion_sort(items):
	for i in range(0, len(items)):
		current = items[i]
		j = i
		while j > 0 and current < items[j - 1]:
			items[j] = items[j - 1]
			j -= 1
		items[j] = current
	return items
