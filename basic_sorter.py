import numpy as np
import random
import time


def timer_and_type(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        print(f'Process took {time.perf_counter()-start_time}s and ended.')

    return wrapper


@timer_and_type
def do_sorting(func, n_trials, array_size):
    print(f'\nStarting {func.__name__.upper()} process:')
    for i in range(n_trials):
        func(np.random.uniform(0, 1, array_size))
# no checking, only execution


def brute_force_sorter(a_list):

    n = len(a_list)
    assert n > 1, 'How about a longer list?'
    temp_list = list(a_list).copy()
    new_list = []

    for i in range(n):
        smallest = temp_list[0]

        for i in temp_list[1:]:
            if smallest > i:
                smallest = i

        temp_list.remove(smallest)
        new_list.append(smallest)

    return new_list


def inbuilt_sorter(a_list):
    assert len(a_list) > 1, 'How about a longer list?'

    return sorted(a_list)


def bubble_sorter(a_list):

    sorting_length = len(a_list)-1  # out of bounds with i+1 approach
    assert sorting_length > 0, 'How about a longer list?'

    needs_sorting = True
    while needs_sorting:
        seen_change = False  # if sorted quicker than in 'sorting_length' steps

        for i in range(sorting_length):
            if a_list[i+1] < a_list[i]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                if i > 0:
                    seen_change = True  # check again after every swap except first pair

        sorting_length -= 1
        needs_sorting = seen_change

    return a_list


def quick_sorter(a_list):
    if len(a_list) > 1:
        return quick_sorter([x for x in a_list if x < a_list[-1]])\
            + [x for x in a_list if x == a_list[-1]]\
            + quick_sorter([x for x in a_list if x > a_list[-1]])
    else:
        return a_list


if __name__ == '__main__':

    test_singles = False
    test_multiples = True

    if test_singles:
        randomlist = random.sample(range(0, 20), 15)
        #randomlist = np.random.uniform(0, 1, 10)

        print(randomlist)

        print(brute_force_sorter(randomlist))
        print(inbuilt_sorter(randomlist))
        print(inbuilt_sorter(np.array(randomlist)))
        print(bubble_sorter(randomlist))
        print(quick_sorter(randomlist))

    N_trials = 1000
    array_size = 1000

    list_of_sorters = [inbuilt_sorter, quick_sorter,
                       bubble_sorter, brute_force_sorter]

    print(f'Running {N_trials} sorting trials!\n')
    if test_multiples:
        for sorter in list_of_sorters:
            do_sorting(sorter, N_trials, array_size)
