
def bubble_sort(items):
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - (i + 1)):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            return items

my_list = [20,54,16,36,99,11,74,88]

print my_list
print(bubble_sort(my_list))