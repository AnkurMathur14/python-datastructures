
"""
I/P: n = 2
O/P: [12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35,
    36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89]

I/P: n = 3
O/P: [123, 124, 125, 126, 127, 128, 129, 134, 135, 136, 137, 138, 139, 145, 146, 147,
    148, 149, 156, 157, 158, 159, 167, 168, 169, 178, 179, 189, 234, 235, 236, 237, 238,
     239, 245, 246, 247, 248, 249, 256, 257, 258, 259, 267, 268, 269, 278, 279, 289, 345,
      346, 347, 348, 349, 356, 357, 358, 359, 367, 368, 369, 378, 379, 389, 456, 457, 458,
       459, 467, 468, 469, 478, 479, 489, 567, 568, 569, 578, 579, 589, 678, 679, 689, 789]

T: no. of nodes (i.e. function calls) * work done of function
no. of nodes = O(9^n)
work done of function = O(1

T: O(9^n)

"""

# Pure recursion
# Note: Here, using n in base condition. We can also pass 'start' and increase start + 1 for next digit
# and use start > n in  base condition.
def _n_digit_num_with_increasing_digits2(n, choice_start, num, mul, result):
    if n == 0:
        result.append(num)
        return

    # Exploring choices for position at 'start'
    for digit_choice in range(choice_start, 10):
        new_num = num * mul + digit_choice
        _n_digit_num_with_increasing_digits2(n - 1, digit_choice + 1, new_num, 10, result)


def n_digit_num_with_increasing_digits2(n):
    result = []
    if n == 1:
        result = [n for n in range(10)]
        print(result)
        return

    start = 1
    choice_start = 1
    _n_digit_num_with_increasing_digits2(n, choice_start, 0, 1, result)
    print(result)

# Backtracking method

# Note: Here, using n in base condition. We can also pass 'start' and increase start + 1 for next digit
# and use start > n in  base condition.
def _n_digit_num_with_increasing_digits(n, number_list, result):
    if n == 0:
        number = 0
        for num in number_list:
            number = number * 10 + num
        result.append(number)
        return

    for digit_choice in range(1, 10):
        if not number_list or digit_choice > number_list[-1]:
            number_list.append(digit_choice)
            _n_digit_num_with_increasing_digits(n - 1, number_list, result)
            number_list.pop()


def n_digit_num_with_increasing_digits(n):
    result = []
    if n == 1:
        result = [n for n in range(10)]
        print(result)
        return

    number_list = []
    _n_digit_num_with_increasing_digits(n, number_list, result)
    print(result)


def main():
    #n_digit_num_with_increasing_digits(1)
    n_digit_num_with_increasing_digits(2)
    n_digit_num_with_increasing_digits(3)


if __name__ == "__main__":
    main()