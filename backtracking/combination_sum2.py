"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

T: (2^n)
"""


def subsets2(start, candidates, current_subset, result, target):

    if target == 0:
        result.append(current_subset.copy())
        return

    if start == len(candidates):
        return

    if target < 0:
        return

    # Include the element at nums[start]
    current_subset.append(candidates[start])
    subsets2(start + 1, candidates, current_subset, result, target - candidates[start])
    current_subset.pop()

    # Skip duplicates
    while start + 1 < len(candidates) and candidates[start + 1] == candidates[start]:
        start += 1

    # Not including the element at nums[start]
    subsets2(start + 1, candidates, current_subset, result, target)


def combination_sum2(candidates, target):
    result = []
    current_subset = []
    start = 0

    # sort the array to eliminate duplicates later
    candidates.sort()

    subsets2(start, candidates, current_subset, result, target)
    return result


def main():
    print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print(combination_sum2([2, 5, 2, 1, 2], 5))  # [[1, 2, 2], [5]]


if __name__ == '__main__':
    main()
