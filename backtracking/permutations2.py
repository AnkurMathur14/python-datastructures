"""
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nPr = n!/(n - r)! = n!/(n - n)! = n! (r = n because we have to take all n elements in the arrangement)
T: O(n!)
"""


def _permutations2(start, nums, result):
    # Note here pointer should not be required to go the last element. i.e.
    # no need to process the last element because the single element can not be
    # arranged further
    if start == len(nums) - 1:
        result.append(nums.copy())
        return

    myhash = set()
    for i in range(start, len(nums)):
        if nums[i] not in myhash:
            myhash.add(nums[i])     # This has to be before swap
            nums[i], nums[start] = nums[start], nums[i]
            _permutations2(start + 1, nums, result)
            nums[i], nums[start] = nums[start], nums[i]


def permutation2(nums):
    result = []
    start = 0
    _permutations2(start, nums, result)
    return result


def main():
    print(permutation2([2, 2, 1, 1]))   # [[2, 2, 1, 1], [2, 1, 2, 1], [2, 1, 1, 2], [1, 2, 2, 1], [1, 2, 1, 2], [1, 1, 2, 2]]
    print(permutation2([1, 2, 3]))      # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    return True


if __name__ == '__main__':
    main()
