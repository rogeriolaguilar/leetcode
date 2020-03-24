"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import time
import random

class BruteForceSolution:
  def twoSum(self, nums: [int], target: int):
    size = len(nums)
    i = size - 1
    j = size - 1
    for n in nums:
      i = (i + 1) % size
      for m in nums:
        j = (j + 1) % size
        if n != m and n + m == target:
          return [i, j]


class OtherBruteForceSolution:
  def twoSum(self, nums: [int], target: int):
    last_index = len(nums) - 1
    i = 0
    while i <= last_index:
      j = 0
      while j <= last_index:
        if i != j and nums[i] + nums[j] == target:
          return [i, j]
        j += 1
      i += 1

class TwoPassHashSolution:
  def twoSum(self, nums: [int], target: int):
    table = {}
    last_index = len(nums) - 1

    start_time = time.clock()
    for i, v in enumerate(nums):
      table[v] = i
    print("Two-pass Hash Table: time to create Hash Table", (time.clock() - start_time) * 1000, 'miliseconds')

    j = 0
    while j <= last_index: 
      # look for the complement in the table
      complement = target - nums[j]
      if complement != nums[j] and (complement in table.keys()):
        return [j, table[complement]] 
      j += 1

    
class OnePassHashSolution:
  def twoSum(self, nums, target):
    seen = {}
    for i, v in enumerate(nums):
      remaining = target - v
      if remaining in seen:
        return [seen[remaining], i]
      seen[v] = i
    return []



def run_test(nums, target):
  start_time = time.clock()
  print('>> Brute force solucion:', BruteForceSolution().twoSum(nums, target), '-' , (time.clock() - start_time) * 1000, 'miliseconds')

  start_time = time.clock()
  print('>> Other Brute force solucion:', OtherBruteForceSolution().twoSum(nums, target), '-' , (time.clock() - start_time) * 1000, 'miliseconds')

  start_time = time.clock()
  print('>> Two-pass Hash Table solucion:', TwoPassHashSolution().twoSum(nums, target), '-' , (time.clock() - start_time) * 1000, 'miliseconds')

  start_time = time.clock()
  print('>> One-pass Hash Table solucion:', OnePassHashSolution().twoSum(nums, target), '-' , (time.clock() - start_time) * 1000, 'miliseconds')



print("Simple test - List: [2,7,11,15]. Target: 22. Expected result: [1,3]")

nums = [2,7,11,15]
target = 22
run_test(nums, target)

print()
print("Testing with big list")

start_time = time.clock()
nums = []
list_size = 10 * 1000 * 1000
for n in range(list_size):
  nums += [n * random.randint(1, 3)]
print("Time to create list:", time.clock()-start_time)


target = 2342527
print(f"List size: {list_size}. Target: {target}")
run_test(nums, target)

"""
Simple test - List: [2,7,11,15]. Target: 22. Expected result: [1,3]
>> Brute force solucion: [1, 3] - 0.007999999999994123 miliseconds
>> Other Brute force solucion: [1, 3] - 0.0049999999999980616 miliseconds
Two-pass Hash Table: time to create Hash Table 0.0030000000000030003 miliseconds
>> Two-pass Hash Table solucion: [1, 3] - 0.011999999999998123 miliseconds
>> One-pass Hash Table solucion: [1, 3] - 0.0030000000000030003 miliseconds

Testing with big list
Time to create list: 10.181505
List size: 10000000. Target: 2342527
>> Brute force solucion: [3, 1171259] - 3407.3399999999997 miliseconds
>> Other Brute force solucion: [3, 1171259] - 3578.3950000000004 miliseconds
Two-pass Hash Table: time to create Hash Table 1829.9310000000019 miliseconds
>> Two-pass Hash Table solucion: [3, 1171259] - 2032.2819999999986 miliseconds
>> One-pass Hash Table solucion: [468505, 468506] - 134.5729999999996 miliseconds
"""