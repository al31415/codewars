"""
Roman Numerals Decoder
https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

Modern Roman numerals are
written by expressing each decimal digit of the number to be encoded
separately, starting with the leftmost digit and skipping any 0s.

So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).

The Roman numeral for 1666, "MDCLXVI", uses each letter in descending
order.

MMCXX(IV) 1000, 1000, 100, 10, 10, 1 , 5

"""


def roman_numerals_decoder(roman):
    alphabet = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    numbers = [alphabet[x] for x in list(roman)]
    numbers.reverse()
    total = 0
    for i, e in enumerate(numbers):
        if i == 0 or e >= numbers[i - 1]:
            total += e
        else:
            total -= e
    return total


assert roman_numerals_decoder("XC") == 90
assert roman_numerals_decoder("IV") == 4
assert roman_numerals_decoder("XIV") == 14
assert roman_numerals_decoder("XXI") == 21
assert roman_numerals_decoder("I") == 1
assert roman_numerals_decoder("MMCXXIV") == 2124
assert roman_numerals_decoder("II") == 2
assert roman_numerals_decoder("MMVIII") == 2008
assert roman_numerals_decoder("MDCLXVI") == 1666
