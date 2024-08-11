"""
2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.
A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.
Two subsets are different if and only if the chosen indices to delete are different.

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

T: O(2^n)
"""
import collections


def _beautiful_subsets(start, nums, k, my_hash, result):
    if start == len(nums):
        result[0] += 1
        return

    # Take the number in the set
    # Before taking the current number nums[start] in the set,  check if its neighbour numbers
    # (nums[start] + k and nums[start] - 1) are already present in the set. If they are present then
    # the current number nums[start] can't be taken into the set because then abs difference between nums[start] and
    # nums[start] + k OR nums[start] - k will become k
    if my_hash[nums[start] + k] == 0 and my_hash[nums[start] - k] == 0:
        my_hash[nums[start]] += 1
        _beautiful_subsets(start + 1, nums, k, my_hash, result)
        my_hash[nums[start]] -= 1

    # Don't take the number in the set
    _beautiful_subsets(start + 1, nums, k, my_hash, result)


# Method will loop syntax
def _beautiful_subsets2(start, nums, k, my_hash, result):
    result[0] += 1
    for i in range(start, len(nums)):
        if my_hash[nums[i] + k] == 0 and my_hash[nums[i] - k] == 0:
            my_hash[nums[i]] += 1
            _beautiful_subsets2(i + 1, nums, k, my_hash, result)
            my_hash[nums[i]] -= 1


def beautiful_subsets(nums, k):
    start = 0
    my_hash = collections.defaultdict(lambda : 0)
    result = [0]
    _beautiful_subsets(start, nums, k, my_hash, result)
    return result[0] - 1


def main():
    print(beautiful_subsets([2,4,6], 2))


if __name__ == '__main__':
    main()
