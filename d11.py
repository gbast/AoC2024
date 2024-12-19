from collections import deque
import numpy as np
import timeit
from multiprocessing import Pool, cpu_count
from functools import cache
from typing import List

    
@cache
def parse_stone(stone: int):
    lenc = len(str(stone))
    if stone == 0:
        return [1]
    elif lenc % 2 == 0:
        return split_1(stone)
    else:
        return [stone * 2024]

@cache
def split_1(stone: int) : #math version isnted of string split (more or less same performance)
    lenc = len(str(stone))
    half_len = lenc // 2
    return [stone // (10 ** half_len),  stone % (10 ** half_len)]

#test too slow
def blinker(n_iter):
    stones = dict(enumerate(map(int,input_data)))
    cntstones=len(stones)
   # print(stones,cntstones)
    iter = 0
    
    start_time = timeit.default_timer()
    for _ in range(0,n_iter):
        ls=len(stones)
        for i in range(0,ls) :
            stone=stones[i]
            #print(iter, stone)
            if stone == 0:
                stones[i]= 1
            elif stone == 1:
                stones[i]=2024
            else:             
                lenc = len(str(stone))  
                if lenc % 2 == 0:
                    half_len = lenc // 2
                    stones[i] = stone // (10 ** half_len)  # Get the left half
                    stones[cntstones] = stone % (10 ** half_len) 
                    cntstones +=1

                else:
                    stones[i] *= 2024
        iter += 1
    
        elapsed = timeit.default_timer() - start_time
        print(f"{iter}: {elapsed:.6f} secondi - stones {cntstones}")

    return len(stones)
#test too slow
def blinker2(n_iter):
    stones = list(map(int, input_data))  # Use a list instead of a dict
    cntstones = len(stones)
  #  print(stones, cntstones)
    
    start_time = timeit.default_timer()
    
    for iter in range(n_iter):
        new_stones = []  # To store new stones
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif stone == 1:
                new_stones.append(2024)
            else:
                lenc = len(str(stone))
                if lenc % 2 == 0:
                    half_len = lenc // 2
                    new_stones.append(stone // (10 ** half_len))  # Get the left half
                    new_stones.append(stone % (10 ** half_len))  # Get the right half
                else:
                    new_stones.append(stone * 2024)
        
        stones = new_stones  # Update stones with the new list
        cntstones = len(stones)  # Update the count of stones
        
        elapsed = timeit.default_timer() - start_time
       # print(f"{iter + 1}: {elapsed:.6f} seconds - stones {cntstones}")

    return len(stones)
#test too slow
def blinker3(n_iter):
    stones = list(map(int, input_data))  # Use a list instead of a dict
    cntstones = len(stones)
    
    start_time = timeit.default_timer()
    
    for iter in range(n_iter):
        new_stones = []  #  new stones
        for stone in stones:
           
            result = parse_stone(stone)
            new_stones.extend(result)  

        stones = new_stones[:]
        cntstones = len(stones)  
        
        elapsed = timeit.default_timer() - start_time
        print(f"{iter}: {elapsed:.6f} secondi - stones {cntstones}")
    return len(stones)
#test too slow
def process_stones(stones):

    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif stone == 1:
            new_stones.append(2024)
        else:
            lenc = len(str(stone))
            if lenc % 2 == 0:
                half_len = lenc // 2
                new_stones.append(stone // (10 ** half_len))  # Left 
                new_stones.append(stone % (10 ** half_len))   # Right 
            else:
                new_stones.append(stone * 2024)

    return np.array(new_stones)  # Convert 
#test too slow
def blinker_numpy(n_iter):
    stones = np.array(list(map(int, input_data)))  # Convert np array
    cntstones = len(stones)
   # print(stones, cntstones)

    start_time = timeit.default_timer()

    for iter in range(n_iter):
        stones = process_stones(stones)  # Process stones
        cntstones = len(stones)

        elapsed = timeit.default_timer() - start_time
        #print(f"{iter + 1}: {elapsed:.6f} seconds - stones {cntstones}")

    return len(stones)
#test too slow
def blinker_numpy2(n_iter):
    stones = np.array(list(map(int, input_data)))  # Convert 
    cntstones = len(stones)
    print(stones, cntstones)

    start_time = timeit.default_timer()

    for iter in range(n_iter):
        # Create masks for conditions
        digit_counts = np.array([len(str(stone)) for stone in stones])
        

        # Create masks
        mask_zero = (stones == 0)
        mask_one = (stones == 1)
        mask_odd = (digit_counts % 2 != 0) & ~mask_zero & ~mask_one
        mask_even = (digit_counts % 2 == 0) & ~mask_zero & ~mask_one
        # Estimate the output size
        # Zeros contribute 1 element, Ones contribute 1 element, Odd contribute 1 element each, Even contribute 2 elements each
        output_size = np.sum(mask_zero) + np.sum(mask_one) + np.sum(mask_odd) + 2 * np.sum(mask_even)

        # Initialize new_stones 
        new_stones = np.empty(output_size, dtype=stones.dtype)

        index = 0

        # Handle 0
        new_stones[index:index + np.sum(mask_zero)] = 1
        index += np.sum(mask_zero)

        # Handle 1
        new_stones[index:index + np.sum(mask_one)] = 2024 * stones[mask_one]
        index += np.sum(mask_one)

        # Handle odd1
        new_stones[index:index + np.sum(mask_odd)] = 2024 * stones[mask_odd]
        index += np.sum(mask_odd)

        # Handle even
        for stone in stones[mask_even]:
            half_len = len(str(stone)) // 2
            left_half = stone // (10 ** half_len)
            right_half = stone % (10 ** half_len)
            new_stones[index] = left_half
            new_stones[index + 1] = right_half
            index += 2


        stones = new_stones
        cntstones = len(stones)

        elapsed = timeit.default_timer() - start_time
        #print(f"{iter + 1}: {elapsed:.6f} seconds - stones {cntstones}")

    return len(stones)


#Best solution using Dict with complexity O(1) instead O(n) for the others
def add_stone(stones_dict: dict, stone: int, count: int = 1):
    stones_dict[stone] = stones_dict.get(stone, 0) + count
  
def blinker3dict(n_iter, stonedict):

    for iter in range(n_iter):
        new_stonedict = dict()
        for stone,count in stonedict.items():
           
            result = parse_stone(stone)
            for res in result:
                
                add_stone(new_stonedict,res, count)  
         

        stonedict.clear()
        stonedict=dict(new_stonedict)

        #print(f"#{iter+1} - {sum(stonedict.values())}")

    return sum(stonedict.values())




if __name__ == '__main__':
    #part 1
    """
    start_time = timeit.default_timer()
    final_stones =blinker_numpy2(35)
    sts = np.array(list(map(int, input_data)))  # Convert input data to a NumPy array
    #final_stones = process_stones(sts, iterations=25)
    elapsed = timeit.default_timer() - start_time
    print(f" final_stones {final_stones}: {elapsed:.6f} secondi")
    start_time = timeit.default_timer()
    final_stones =blinker_numpy(35)
    sts = np.array(list(map(int, input_data)))  # Convert input data to a NumPy array
    #final_stones = process_stones(sts, iterations=25)
    elapsed = timeit.default_timer() - start_time
    print(f" final_stones {final_stones}: {elapsed:.6f} secondi")
    start_time = timeit.default_timer()
    final_stones =blinker2(35)
    sts = np.array(list(map(int, input_data)))  # Convert input data to a NumPy array
    #final_stones = process_stones(sts, iterations=25)
    elapsed = timeit.default_timer() - start_time
    print(f" final_stones {final_stones}: {elapsed:.6f} secondi")
    start_time = timeit.default_timer()
    final_stones =blinker(35)
    sts = np.array(list(map(int, input_data)))  # Convert input data to a NumPy array
    #final_stones = process_stones(sts, iterations=25)
    elapsed = timeit.default_timer() - start_time
    print(f" final_stones {final_stones}: {elapsed:.6f} secondi")

    start_time = timeit.default_timer()
    
    final_stones =blinker3(35)
    sts = np.array(list(map(int, input_data)))  # Convert input data to a NumPy array
    #final_stones = process_stones(sts, iterations=25)
    elapsed = timeit.default_timer() - start_time
    print(f" final_stones {final_stones}: {elapsed:.6f} secondi")
    """
with open("d11.txt", "r") as file:
    line = file.readline()
input_data = list(map(int, line.split())) 
print(input_data)
stonedict = dict()
for stone in input_data:
    add_stone(stonedict, stone)
print(stonedict)
for stone in stonedict:
    print(stone,":",stonedict[stone])
start_time = timeit.default_timer()
res=blinker3dict(25,stonedict)
elapsed = timeit.default_timer() - start_time
print(f"part1: {res} in {elapsed:.6f} seconds")
start_time = timeit.default_timer()
stonedict = dict()
for stone in input_data:
    add_stone(stonedict, stone)
res=blinker3dict(75,stonedict)
elapsed = timeit.default_timer() - start_time
print(f"part2: {res} in {elapsed:.6f} seconds")

start_time = timeit.default_timer()
stonedict = dict()
for stone in input_data:
    add_stone(stonedict, stone)
res=blinker3dict(1000,stonedict)
elapsed = timeit.default_timer() - start_time
print(f"part for joke 1000: {res} in {elapsed:.6f} seconds")