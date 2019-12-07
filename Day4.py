#!/usr/bin/env python3

def check_double_chars(string):
    for sub in range(11,110,11):
        if str(string).find(str(sub)) >= 0: return True
    return False

def check_decrease(string):
    for n, digit in enumerate(string):
        if n == len(string)-1: break
        if int(digit) > int(string[n+1]): return False
    return True

def check_exact_doubles(string):
    for sub in range(11,110,11):
        sub = str(sub)
        if sub in string: 
            if string.find(sub) == string.rfind(sub): return True
    return False


# Part1:
def get_passwords_pt1(inputlist):
    validlist = []
    for pwd in inputlist:
        pwdstring = str(pwd)
        # Two adjacent digits are the same (like 22 in 122345).
        if not check_double_chars(pwdstring):
            continue
        # Going from left to right, the digits never decrease
        if not check_decrease(pwdstring):
            continue
        #print(pwd)
        validlist.append(pwd)
    #print(validlist)
    return validlist

def get_passwords_pt2(inputlist):
    validlist = []
    for pwd in inputlist:
        pwdstring = str(pwd)
        # the two adjacent matching digits are not part of a 
        # larger group of matching digits.
        if not check_exact_doubles(pwdstring):
            continue
        # Going from left to right, the digits never decrease
        if not check_decrease(pwdstring):
            continue
        validlist.append(pwd)
    return validlist


if __name__ == "__main__":

    assert [222222] == get_passwords_pt1([222222])
    assert [223450] != get_passwords_pt1([223450])
    assert [234789] != get_passwords_pt1([234789])
    assert [112233] == get_passwords_pt2([112233])
    assert [123444] != get_passwords_pt2([123444])
    assert [111122] == get_passwords_pt2([111122])
    print("Number of passwords part1: ", 
        len(get_passwords_pt1(range(134564,585160))))
    print("Number of passwords part2: ", 
        len(get_passwords_pt2(range(134564,585160))))
    