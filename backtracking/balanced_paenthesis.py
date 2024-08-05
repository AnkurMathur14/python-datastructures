"""
Method to generate all balanced parenthesis of given length.
Length given is actually the length of pair. i.e. if n = 3, then total 3 pair of parentheses can be generated.
That means there will be 3 open and 3 closed.

T: O(2^(2n))
"""


def __generate_parenthesis(open, close, result, temp=[]):
    if open == 0 and close == 0:
        result.append("".join(list(temp)))
        return

    # Take open
    if open != 0:
        temp.append("(")
        __generate_parenthesis(open - 1, close, result, temp)
        temp.pop()

    # Take close
    if close > open:
        temp.append(")")
        __generate_parenthesis(open, close - 1, result, temp)
        temp.pop()


def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    result = []
    open = close = n
    __generate_parenthesis(open, close, result)
    return result


def main():
    print(generate_parenthesis(0))   # ['']
    print(generate_parenthesis(1))   # ['()']
    print(generate_parenthesis(2))   # ['(())', '()()']
    print(generate_parenthesis(3))   # ["((()))","(()())","(())()","()(())","()()()"]


if __name__ == "__main__":
    main()