def cocktail_sort(items):
    a = items
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - (i + 1)):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
            if items[len(items) - (j + 1)] < items[len(items) - (j + 2)]:
                items[len(items) - (j + 1)], items[len(items) - (j + 2)] = items[len(items) - (j + 2)], items[len(items) - (j+ 1)]
                swapped = True
        if not swapped:
            return items

