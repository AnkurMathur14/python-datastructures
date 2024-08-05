"""
Permutation : Arranging elements in different possible ways.

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


T: O(n!)
If there are 3 open positions to arrange these numbers.
__ __ __
Pos 1 has n possibilities. When position 1 is filled, position 2 has n-1 possibilities.
Once position 2 is filled, position 3 has n -2 possibilities.
second last position will have (2) possibilities and last position will just have 1 possibility
i.e n * (n - 1) * (n -2)  ........ 1
This is same as O(n!)

nPr since we are arranging all n elements in a different ways then r == n
nPr = n!/(n-n)! = n!/0! = n!

permutation == Arranging
combination = selection of certain elements from a set of elements
"""


def _permutations(start, nums, result):
    # Note here pointer should not be required to go the last element. i.e.
    # no need to process the last element because the single element can not be
    # arranged further
    if start == len(nums) - 1:
        result.append(nums.copy())
        return

    for i in range(start, len(nums)):
        nums[i], nums[start] = nums[start], nums[i]
        _permutations(start + 1, nums, result)
        nums[i], nums[start] = nums[start], nums[i]


def permutation(nums):
    result = []
    start = 0
    _permutations(start, nums, result)
    return result


def main():
    print(permutation([]))  # [[]]
    print(permutation([1]))  # [[1]]
    print(permutation([1, 2]))  # [[1, 2], [2, 1]]
    print(permutation([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    return True


if __name__ == '__main__':
    main()
