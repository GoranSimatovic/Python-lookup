import numpy as np
import random
import time



def timer_and_type(func):
    
    def wrapper(*args, **kwargs):
        
        print('\n********************')
        if isinstance(*args, list):
            print('Sorting python list.')
        elif isinstance(*args, np.ndarray):
            print('Soriting numpy array.')
        print('********************')
        print(f'Process {func} started')


        start_time = time.perf_counter()
        func(*args, **kwargs)
        print(f'Process took {time.perf_counter()-start_time}s and ended.')
    
    return wrapper



@timer_and_type
def inbuilt_list_sorter(a):
    return a.sort()


n = random.randint(20,22)
print(n)


randomlist = random.sample(range(0, 100000), 50000)

inbuilt_list_sorter(randomlist)
inbuilt_list_sorter(np.array(randomlist))
