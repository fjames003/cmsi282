from random import randint
import time
import sys

       
def is_sorted_list(list):
    return not any(list[i] > list[i + 1] for i in range(len(list) - 1))

def bozosort(list):
    while not is_sorted_list(list):
        first = randint(0, len(list) - 1)
        second = randint(0, len(list) - 1)
        list[first], list[second] = list[second], list[first]
    return list

def bozo_analysis(runs, max_size):
    for i in range(2, max_size + 1):
        
        total_time = 0
        for k in range(runs):
            list = new_list(i)
            total_time += time_it(bozosort, list)
        print("List size: " + str(i) + " took an average of " + str(round(total_time / runs, 4)) + " ms, over " + str(runs) + " runs")

def time_it(function, argument):
    start = time.clock()
    function(argument)
    return (time.clock() - start) * 1000

def new_list(size):
    list = []
    for i in range(size):
            list.append(randint(-sys.maxsize - 1, sys.maxsize))
    return list