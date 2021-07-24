def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result


if __name__ == '__main__':
    print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
    # --> "abigailtheta
    print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
                                  "oocccffuucccjjjkkkjyyyeehh"], 1))
    # --> "oocccffuucccjjjkkkjyyyeehh"
    print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3))
    # --> "ixoyx3452zzzzzzzzzzzz")

    print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv",
                                  "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
