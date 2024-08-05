"""
Combination sum:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Subsets whose sum is equal to target.
Note: Same number can be picked infinite times
Each subset must be unique

# T: O(2^n)
"""


def subsets(start, candidates, current_subset, result, target):

    # This check has to be at top
    if target == 0:
        result.append(current_subset.copy())
        return

    if start == len(candidates):
        return

    if target < 0:
        return

    # Include the element at nums[start]
    current_subset.append(candidates[start])
    subsets(start, candidates, current_subset, result, target - candidates[start])
    current_subset.pop()

    # Not including the element at nums[start]
    subsets(start + 1, candidates, current_subset, result, target)


def combination_sum(candidates, target):
    result = []
    current_subset = []
    start = 0
    subsets(start, candidates, current_subset, result, target)
    return result


def main():
    print(combination_sum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
    print(combination_sum([2], 1))  # []


if __name__ == '__main__':
    main()
