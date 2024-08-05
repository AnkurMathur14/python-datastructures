"""
Find subsets of size k

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

                        [1, 2, 3, 4]
                    /           |       \
                1 [2, 3, 4]   2 [3, 4]   3 [4]
               /    \    \      /     \     |
            12[3,4] 13[4] 14[] 23[4]  24[]  34[] <============= k == 2
            /   \      |        |
        123[4]  124[]  134[]   234[]
        /
      1234[]

T: O(nCr) = O(nCk)
"""


def _combinations(start, nums, k, result, current_set):
    if k == 0:
        result.append(list(current_set))
        return

    for i in range(start, len(nums)):
        current_set.append(nums[i])
        _combinations(i + 1, nums, k - 1, result, current_set)
        current_set.pop()


def combinations(n, k):
    start = 0
    result = []
    current_set = []
    nums = [i for i in range(1, n + 1)]
    _combinations(start, nums, k, result, current_set)
    return result


def main():
    print(combinations(4, 2))
    print(combinations(4, 3))


if __name__ == '__main__':
    main()