"""
131. Palindrome Partitioning

Given a string s, partition s such that every  substring of the partition is a  palindrome.
Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

T : No of function calls (no. of nodes) * work done by function
No of function calls (no. of nodes) = no. of potentials subsets/partitions = O(2^(n - 1))
work done by function = O(n) to check if string is palindrome

T: O(n * 2^(n - 1))

                                    aab
                            /           |       \
                        a(ab)           aa(b)   aab()
                        /                |
                    a a (b)            aa b ()
                    /
                a a b ()
"""


def is_palindrome(palindromic_string):
    if len(palindromic_string) == 1:
        return True

    start = 0
    end = len(palindromic_string) - 1

    while start < end:
        if palindromic_string[start] != palindromic_string[end]:
            return False
        start += 1
        end -= 1
    return True


def _palindromic_partitions(start, my_string, current_set, result):
    if start == len(my_string):
        result.append(list(current_set))
        return

    palindromic_string = ""
    for i in range(start, len(my_string)):
        palindromic_string += my_string[i]
        if is_palindrome(palindromic_string):
            current_set.append(palindromic_string)
            _palindromic_partitions(i + 1, my_string, current_set, result)
            current_set.pop()


def palindromic_partitions(my_string):
    start = 0
    result = []
    current_set = []
    _palindromic_partitions(start, my_string, current_set, result)
    return result


def main():
    print(palindromic_partitions("aab"))    # [['a', 'a', 'b'], ['aa', 'b']]
    print(palindromic_partitions("a"))      # [['a']]
    print(palindromic_partitions(""))       # [[]]


if __name__ == '__main__':
    main()
