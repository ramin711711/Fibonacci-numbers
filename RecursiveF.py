import time

import sys
sys.set_int_max_str_digits(100000000)


def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n - 1) + recur_fib(n - 2)

start_time = time.time()

while input('Quit? (Y/N)').lower() != 'y':
    
    inp = int(input('Which fibonacci element do you want to get? '))
    start_time1 = time.time()


    cur_num = recur_fib(inp)
    
    print(cur_num)

    end_time1 = time.time()
    timer_time1 = end_time1 - start_time1
    print(f"Execution time: {timer_time1:.6f} seconds")

for i in range(1000000):
    pass

end_time = time.time()

timer_time = end_time - start_time
print(f"Total execution time: {timer_time:.6f} seconds")
