import numpy as np
import random

# Binary search example
# - assumtions are that the list is sorted and the searched number is unique


def binary_src(x, input_list, array_start=0):

    array_len = len(input_list)
    split_index = int(array_len/2)
    split_element = input_list[split_index]

    if array_len == 1:
        if input_list[0] == x:
            return array_start
        else:
            print(f'Looked for: {x} - No index found!\n')
            return 

    if split_element == x:
        return array_start+split_index
    elif split_element > x:
        return binary_src(x, input_list[:split_index], array_start)
    elif split_element < x:
        return binary_src(x, input_list[split_index:], array_start + split_index)


def quick_test_binary(n): # my cheap unit test :)

    array_min = 0
    array_max = 15
    array_lenght = 10
    for i in range(n):

        array = random.sample(
            range(array_min, array_max,),
            array_lenght
        )

        array.sort()  # the array is sorted
        n_that_is_searched = np.random.randint(array_min, array_lenght)

        print(array)
        index_is = binary_src(n_that_is_searched, array)

        if index_is != None:
            print(f'Looked for: {n_that_is_searched}, found {array[index_is]} at position {index_is}\n')




if __name__ == '__main__':

    if True:
        print('Checking many ..')
        quick_test_binary(50)

