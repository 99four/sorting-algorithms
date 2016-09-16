import datetime as datetime
import matplotlib.pyplot as plt
import random

data_set = []
data_set_sizes = []
bubble_times = []
select_sort_times = []

def generate_random_array(size):
    array = range(0, size)
    random.shuffle(array)
    return array

def swap(array, first_el, second_el):
    tmp = array[first_el]
    array[first_el] = array[second_el]
    array[second_el] = tmp

def get_smallest_index(start_index, numbers):
    min_index = start_index
    min = numbers[start_index]
    for i in range(start_index, len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
            min_index = i
    return min_index

def select_sort(numbers):
    for i in range(0, len(numbers)):
        smallest_index = get_smallest_index(i, numbers)
        swap(numbers, i, smallest_index)
    return numbers

def bubble_sort(numbers):
    for j in range(0, len(numbers)):
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                swap(numbers, i-1, i)
    return numbers

def milis(dt):
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms

def initialize_arrays(iterations, size):
    for i in range(1, iterations + 1):
        data_set.append(generate_random_array(i*size))
        data_set_sizes.append(i*size)
    return data_set

def perform_sort_operations(sort_algorithm, times_array):
    for data in data_set:
        time_start = datetime.datetime.now()
        sort_algorithm(data)
        time_end = datetime.datetime.now()
        times_array.append(milis(time_end - time_start))

parameters = [
    [bubble_sort, bubble_times, 'bubble sort', 'y'],
    [select_sort, select_sort_times, 'selection sort', 'g']
]

initialize_arrays(30, 30)

for sort_alg, sort_times, label, color in parameters:
    perform_sort_operations(sort_alg, sort_times)
    plt.plot(data_set_sizes, sort_times, '-gD', color=color, label=label)

legend = plt.legend(loc='upper center', shadow=True)
plt.xlabel('data set size')
plt.ylabel('time [ms]')
plt.show()
