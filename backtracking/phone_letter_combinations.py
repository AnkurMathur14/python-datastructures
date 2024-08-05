"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"2": ["a", "b", "c"],
"3": ["d", "e", "f"],
"4": ["g", "h", "i"],
"5": ["j", "k", "l"],
"6": ["m", "n", "o"],
"7": ["p", "q", "r", "s"],
"8": ["t", "u", "v"],
"9": ["w", "x", "y", "z"]

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:

Input: digits = ""
Output: []


Example 3:

Input: digits = "2"
Output: ["a","b","c"]

A phone key number can have max 4 chars.
So there will be 4 choices for each phone key n
T: O(4^n)
"""

mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def _letter_combinations(start, digits, current_set, result):
    if start == len(digits):
        result.append("".join(list(current_set)))
        return

    for digit in mapping[digits[start]]:
        current_set.append(digit)
        _letter_combinations(start + 1, digits, current_set, result)
        current_set.pop()


def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    result = []
    start = 0
    current_set = []
    _letter_combinations(start, digits, current_set, result)
    return result


def main():
    print(letter_combinations(""))      # []
    print(letter_combinations("23"))    # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print(letter_combinations("234"))   # ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh',
    # 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
    return


if __name__ == '__main__':
    main()