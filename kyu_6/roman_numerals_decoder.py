from functools import reduce


def solution(roman):
    """
    Roman Numerals Decoder
    https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

    Create a function that takes a Roman numeral as its argument and
    returns its value as a numeric decimal integer.  You don't need to
    validate the form of the Roman numeral. Modern Roman numerals are
    written by expressing each decimal digit of the number to be encoded
    separately, starting with the leftmost digit and skipping any 0s.

    So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
    and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).

    The Roman numeral for 1666, "MDCLXVI", uses each letter in descending
    order.
    """
    alphabet = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def aux(symbols_list, acc=0.0):
        if len(symbols_list) == 1:
            return acc + alphabet[symbols_list[0]]
        elif not len(symbols_list):
            return acc
        else:
            first = alphabet[symbols_list[0]]
            second = alphabet[symbols_list[1]]
            if first < second:
                return aux(symbols_list[2:], acc + second - first)
            else:
                return aux(symbols_list[1:], acc + first)

    return aux(list(roman))


# Smart solutions: https://www.codewars.com/kata/51b6249c4612257ac0000005/solutions/python


def solution(roman):
    dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total


def solution(roman):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return reduce(lambda x, y: x + y if x >= y else y - x, (d[c] for c in roman))
