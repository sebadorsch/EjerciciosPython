from collections import OrderedDict


def solution(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


if __name__ == '__main__':

    print(solution(4), 'IV', "solution(4),'IV'")
    print(solution(6), 'VI', "solution(6),'VI'")
    print(solution(14), 'XIV', "solution(14),'XIV")
    print(solution(21), 'XXI', "solution(21),'XXI'")
    print(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
    print(solution(91), 'XCI', "solution(91),'XCI'")
    print(solution(984), 'CMLXXXIV', "solution(984),'CMLXXXIV'")
    print(solution(1000), 'M', 'solution(1000), M')
    print(solution(1889), 'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
    print(solution(1989), 'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")
