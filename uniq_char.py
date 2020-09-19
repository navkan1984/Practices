def uniq_char(s):
    count = {}
    if len(s) == 0:
        return True

    for letter in s:
        if letter not in count:
            count[letter] = 1
        else:
            return False

    return True


print(uniq_char(' abcdee'))
