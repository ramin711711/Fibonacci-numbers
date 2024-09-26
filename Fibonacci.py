import time

import sys
sys.set_int_max_str_digits(100000000)

start_time = time.time()


while input('Quit? (Y/N)').lower() != 'y':
    
    

    inp = int(input('Which fibonacci element do you want to get? '))
    start_time1 = time.time()

    cur_num = 0
    previous_num = 1

    for i in range(inp):
        previous_num, cur_num = cur_num, previous_num + cur_num ###
    
    print(cur_num)

    end_time1 = time.time()
    timer_time1 = end_time1 - start_time1
    print(f"Execution time: {timer_time1:.6f} seconds")

for i in range(1000000):
    pass

end_time = time.time()

timer_time = end_time - start_time
print(f"Total execution time: {timer_time:.6f} seconds")





# import time
# import sys

# sys.set_int_max_str_digits(100000000)

# start_time = time.time()
# fib_nums = {}

# while input('Quit? (Y/N)').lower() != 'y':
#     inp = int(input('Which Fibonacci element do you want to get? '))
#     start_time1 = time.time()

#     cur_num = 0
#     previous_num = 1
#     fib_nums = {}

#     for i in range(inp):
#         if i % 3 == 0: 
#             fib_nums[i] = (f'Previous num =  {previous_num}, Current num =  {cur_num}')  
#         previous_num, cur_num = cur_num, previous_num + cur_num

#     print(cur_num)


#     print("Fibonacci numbers every 3rd:", fib_nums)


#     end_time1 = time.time()
#     timer_time1 = end_time1 - start_time1
#     print(f"Execution time: {timer_time1:.6f} seconds")

# for i in range(1000000):
#     pass

# end_time = time.time()


# timer_time = end_time - start_time
# print(f"Total execution time: {timer_time:.6f} seconds")
