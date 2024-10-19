from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        nextnum = target - num
        if nextnum in num_dict:
            return [num_dict[nextnum], i]
        num_dict[num] = i
    return [] 
if __name__ == "__main__":
    # 테스트 케이스
    nums = [3,3]
    target = 6
    
    # 함수 호출
    result = twoSum(nums, target)
    
    # 결과 출력
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")