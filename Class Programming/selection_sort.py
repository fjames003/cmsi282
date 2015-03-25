
def selection_sort(a):
    for i in range(0, len(a) -1):
        min_index = a.index(min(a[i:]))
        a[i], a[min_index] = a[min_index], a[i]
    return a

my_list = [20,54,16,36,99,11,74,88]

print my_list
print(selection_sort(my_list))