"""
698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

There are two techniques to solve this:
1. Start with subsets: Pick numbers from the array and fill up the first subset with the required number to reach the target.
and mark these numbers already used in subset 1 and then pick up the remaining numbers for subset2 and fill up the
second subset with these number and marked them used...till kth subset

Pick subset[0] and search for suitable number(s) from array
Pick subset[1] and search for suitable number(s) from remaining array
etc.

T: for each subset we have to pick numbers from the array (take or don't take)
T: O(k * 2^n)

2. Start with the numbers: Pick the number and put it in one of the suitable k subsets.
Pick nums[0] and see if it fits in set1 or 2 or 3...set k
Pick num[1] amd see if it fits in set1 or 2 or 3...set k
etc.
For each number there are k choices
T: (k^n)

This is an important pattern. question based on this pattern:
698. Partition to K Equal Sum Subsets
2305. Fair Distribution of Cookies
1723. Find Minimum Time to Finish All Jobs
473. Matchsticks to Square
"""



"""
[5,4,3,3,2,2,1]
subset1 = [5] , [(5),4,3,3,2,2,1] 5 is used 
subset2 = [4, 1] , [(5),(4),3,3,2,2,(1)] 5, 4, 1 are used 
subset3 = [3, 2] , [(5),(4),(3),3,(2),2,(1)] 5, 4, 1, 3, 2 are used 
subset4 = [3, 2] , [(5),(4),(3),(3),(2),(2),(1)] 5, 4, 1, 3, 2, 3, 2 are used 
"""


def _canPartitionKSubsets(start, nums, k, target, current_sum, visited):

    # All subsets are successfully formed
    if k == 0:
        return True

    # One Subset is formed, not fill up the next subset
    if current_sum == target:
        return _canPartitionKSubsets(0, nums, k - 1, target, 0, visited)

    # For subset[0] picks up suitable number from nums
    # Then For subset[1] picks up suitable number from unused nums
    for i in range(start, len(nums)):
        if not visited[i] and current_sum + nums[i] <= target:
            visited[i] = True
            if _canPartitionKSubsets(start + 1, nums, k, target, current_sum + nums[i], visited):
                return True
            visited[i] = False
    return False


"""
Pick nums[0] and see if it fits in set1 or 2 or 3...set k
Pick num[1] amd see if it fits in set1 or 2 or 3...set k
etc
Here, start is the number index of array
"""


def _canPartitionKSubsets2(start, nums, k, target, subsets_sum, visited):
    # All numbers are processed, and they are put into suitable k subsets
    if start == len(nums):
        # Check if the sum of all k subsets are equal to target
        for i in range(k):
            if subsets_sum[i] != target:
                return False
        return True

    # check if nums[start] will fit into subset[0], subset[1]...subset[k - 1]
    # then check if nums[start + 1] will fit into subset[0], subset[1]...subset[k - 1]
    # Hence, here for each number, there are k choices. k * k * k ...n times
    # T: O(k^n)
    for i in range(k):
        if subsets_sum[i] + nums[start] <= target:
            subsets_sum[i] += nums[start]
            if _canPartitionKSubsets2(start + 1, nums, k, target, subsets_sum, visited):
                return True
            subsets_sum[i] -= nums[start]
        if subsets_sum[i] == 0:
            break
    return False


def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    sum_of_numbers = sum(nums)

    # The sum of each partition will be exactly sum / k
    if sum_of_numbers % k != 0:
        return False
    target = sum_of_numbers / k

    # If the max num of array is greater than the target, then this number can't be fit in any subset
    max_number = max(nums)
    if max_number > target:
        return False

    start = 0
    current_sum = 0
    visited = [False] * len(nums)
    nums.sort(reverse=True)
    #return _canPartitionKSubsets(start, nums, k, target, current_sum, visited)

    subsets_sum = [0] * k
    return _canPartitionKSubsets2(start, nums, k, target, subsets_sum, visited)


def main():
    print(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))        # True
    print(canPartitionKSubsets([1, 2, 3, 4], 3))                 # False


if __name__ == '__main__':
    main()
