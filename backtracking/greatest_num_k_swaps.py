"""
I/P: "1234567"
k = 4
O/P: "7654321"

OR

I/P: "4577"
k = 2
O/P: "7754"

1. Choose the digit for each position e.g. for (1)234567 for fist position choose digit from remaining positions.
2. Criteria for choosing digit:
2.1 Do not choose self digit (i.e. for position start, do not choose digit at start). because it won't change the number
and one swap will be lost.
2.2 Choose the max digit from remaining digits i.e. for digit at start, choose the max digit from start + 1 but this max
digit has to be greater than the digit at start

similarly for second position 7(2)34561 repeate the same process.

T: Number of nodes (i.e. function calls) in recursive tree * work done by the function

                                (1) 2 2 3 3                                 1
                    /2(1)233       /22133       |32213       32231\         n
            /22(1)33  |23213 \23231                                         n * n-1

        total nodes = n + n*(n- 1) + n*(n- 1)(n-2)....4*3*2*1 = O(n!)

        work done by the function : O(n) where ignoring conversion str to array stuff

        T : O(n * n!)
"""

def _largest_num_with_k_swaps(str, k, start, result):
    if k == 0 or start == len(str) - 1:
        return

    max_mum_index = start + 1
    for i in range(start+1, len(str)):
        if int(str[i]) > int(str[max_mum_index]):
            max_mum_index = i

    for i in range(start+1, len(str)):  # This loop is to choose digits for position 'start' from remaining digits str[start+1:]
        if str[i] == str[max_mum_index] and int(str[max_mum_index]) > int(str[start]):

            # Swap
            str = list(str)
            str[start], str[i] = str[i], str[start]
            str = "".join(str)

            # Check for potential max number
            result[0] = max(result[0], int(str))

            # Before this line,  digit for current position (i.e. start) is decided. Now, choose digit for next position
            _largest_num_with_k_swaps(str, k - 1, start + 1, result)

            # backtrack
            str = list(str)
            str[start], str[i] = str[i], str[start]
            str = "".join(str)

    _largest_num_with_k_swaps(str, k, start + 1, result)


def largest_num_with_k_swaps(str, k):
    result = [int(str)]
    _largest_num_with_k_swaps(str, k, 0, result)
    print(result[0])


def main():
    largest_num_with_k_swaps("4577", 2)


if __name__== "__main__":
    main()