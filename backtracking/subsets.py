"""
78. Subsets

Generate all subsets of a set  (Power set)

Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Power Set: Power set P(S) of a set S is the set of all subsets of S.
For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
If S has n elements in it then P(s) will have 2^n elements
We can use backtracking here, we have two choices first consider that element then don’t consider that element.

Generating power set is basically generating combinations.
(nCr is number of combinations can be made by taking r items from total n items)

formula: nCr = n!/((n-r)! * r!)
Example:Power Set for {1,2,3} is {{}, {1}, {2}, {3}, {1,2}, {2,3}, {1,3} {1,2,3}} = 8 = 2^3

1) 3C0 = #combinations possible taking 0 items from 3 = 3! / ((3-0)! * 0!) = 1
2) 3C1 = #combinations possible taking 1 item from 3 = 3! / ((3-1)! * 1!) = 3
3) 3C2 = #combinations possible taking 2 items from 3 = 3! / ((3-2)! * 2!) = 3
4) 3C3 = #combinations possible taking 3 items from 3 = 3! / ((3-3)! * 3!) = 1
if you add above 4 it comes out 1 + 3 + 3 + 1 = 8 = 2^3. So basically it turns out to be 2^n possible sets in a power
set of n items.

So in an algorithm if you are generating a power set with all these combinations, then it is going to take time
proportional to 2^n. And so the time complexity is 2^n.

T: O(2^n)


                                                {} [1, 2, 3]
                                        /                           \
                                {1} [2, 3]                          {}[2, 3]                    i = 0
                                /           \                       /          \
                        {1, 2}[3]          {1}[3]               {2}[3]              {} [3]      i = 1
                        /       \           /     \             /     \             /     \
                {1, 2, 3} []  {1, 2}[]   {1, 3}[]   {1} []   {2, 3}[] {2} []     {3}[]    {}[]  i = 2
"""


def _subsets(start, nums, result, current_subset):
    if start == len(nums):
        result.append(current_subset.copy())
        return

    # Include the element at nums[start]
    current_subset.append(nums[start])
    _subsets(start + 1, nums, result, current_subset)
    current_subset.pop()

    # Not including the element at nums[start]
    _subsets(start + 1, nums, result, current_subset)


def subsets(nums):
    result = []
    current_subset = []
    start = 0

    _subsets(start, nums, result, current_subset)
    return result


# Method 2
def solve(start, nums, current_set, result):
    result.append(list(current_set))
    for i in range(start, len(nums)):
        current_set.append(nums[i])
        solve(i+1, nums, current_set, result)
        current_set.pop()


def subsets_2(nums):
    result = []
    current_set = []
    start = 0
    solve(start, nums, current_set, result)
    return result


def main():
    print(subsets([1, 2, 3]))   # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    print(subsets([1, 2, 3, 4]))    # [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4], [1, 3],
    # [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2], [3, 4], [3], [4], []]
    return True


if __name__ == "__main__":
    main()
