"""
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots
into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

T: O(2^n)
"""


def _restore_ip_addresses(start, s, dots, current_ip, result):

    if dots == 0:
        if start == len(s):
            result.append(".".join(current_ip))
        return

    part = ""
    for i in range(start, len(s)):
        part += s[i]
        if int(part) > 255 or len(part) > 3 or (len(part) > 0 and part[0] == '0'):
            continue
        current_ip.append(part)
        _restore_ip_addresses(i + 1, s, dots - 1, current_ip, result)
        current_ip.pop()


def restore_ip_addresses(s):
    if len(s) < 4:
        return []

    result = []
    start = 0
    dots = 4
    current_ip = []
    _restore_ip_addresses(start, s, dots, current_ip, result)
    return result


def main():
    print(restore_ip_addresses("25525511135"))


if __name__ == '__main__':
    main()
