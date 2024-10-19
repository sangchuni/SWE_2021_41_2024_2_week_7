from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        nextnum = target - num
        if nextnum in num_dict:
            return [num_dict[nextnum], i]
        num_dict[num] = i
    return [] 
