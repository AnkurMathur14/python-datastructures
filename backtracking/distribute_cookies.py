"""
2305. Fair Distribution of Cookies

You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag.
You are also given an integer k that denotes the number of children to distribute all the bags of cookies to.
All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

Example 1:

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

Example 2:

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.

Start with the cookies: Pick the number and put it in one of the suitable k subsets.
Pick cookies[0] and see if it fits in set1 or 2 or 3...set k
Pick cookies[1] amd see if it fits in set1 or 2 or 3...set k
etc.
For each number there are k choices
T: (k^n)
"""


def _distribute_cookies(start, cookies, k, child_cookies, result):
    if start == len(cookies):
        result[0] = min(result[0], max(child_cookies))
        return

    for i in range(k):
        child_cookies[i] += cookies[start]
        _distribute_cookies(start + 1, cookies, k, child_cookies, result)   # Go to next cookie
        child_cookies[i] -= cookies[start]


def distribute_cookies(cookies, k):
    start = 0       # start is the element index og cookies
    child_cookies = [0] * k
    result = [float('inf')]
    _distribute_cookies(start, cookies, k, child_cookies, result)
    return result[0]


def main():
    print(distribute_cookies([8,15,10,20,8], 2))        # 31
    print(distribute_cookies([6,1,3,2,2,4,1,2], 3))     # 7


if __name__ == '__main__':
    main()
