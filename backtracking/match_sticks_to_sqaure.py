"""
473. Matchsticks to Square

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up,
and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Basically we have to find out if there are 4 subsets with each subset sum is same.
Consider there are 4 boxes (or sides or subsets) and we have to fill the matchsticks from the array into these boxes,
we have to fill in such a way that each box gets same matchsticks count. If this is possible then square can be formed

If matchsticks = [1,1,2,2,2]
4 boxes:
[1 + 1] [2] [2] [2]

Start with the matchsticks: Pick the number and put it in one of the suitable k subsets.
Pick matchsticks[0] and see if it fits in set1 or 2 or 3...set k
Pick matchsticks[1] amd see if it fits in set1 or 2 or 3...set k
etc.
For each number there are k choices
T: (k^n)

"""


def _matchsticks_to_square(start, matchsticks, k, target, sides):
    # 'start' tracks the array element. If all elements are processes.
    if start == len(matchsticks):
        # check if all sides have same sum
        for i in range(k):
            if sides[i] != target:
                return False
        # return True As soon as all sides have same sum and equal to target
        return True

    for i in range(k):
        if sides[i] + matchsticks[start] <= target:
            sides[i] += matchsticks[start]
            # return True As soon as all sides have same sum and equal to target
            if _matchsticks_to_square(start + 1, matchsticks, k, target, sides):
                return True
            sides[i] -= matchsticks[start]
    return False


def matchsticks_to_square(matchsticks):

    # There are 4 sides in square. So total subsets will be 4. Here one subset is one side of square
    k = 4

    sum_of_matchsticks = sum(matchsticks)

    # Each side of square should have sum of sum_of_matchsticks / 4. If there is any remainder then
    # square can not be formed because we have to use all values of array
    if sum_of_matchsticks % k != 0:
        return False

    # sum of each subset (side)
    target = sum_of_matchsticks / k

    # If there is an element in array which is greater than the target then this element can not be fit in any side
    # and since we have to use all the elements of array, square can not be formed.
    if max(matchsticks) > target:
        return False

    # Initializing each side sum as 0
    sides = [0] * k

    # Here start is the index of array element
    start = 0

    return _matchsticks_to_square(start, matchsticks, k, target, sides)


def main():
    print(matchsticks_to_square([1, 1, 2, 2, 2]))   # True
    print(matchsticks_to_square([3, 3, 3, 3, 4]))   # False


if __name__ == '__main__':
    main()
