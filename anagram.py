def anagram(s1, s2):
    s1, s2 = s1.replace(' ', '').lower(), s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    counter = {}

    for letter in s1:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

    for letter in s2:
        if letter in counter:
            counter[letter] -= 1
        else:
            counter[letter] = 1

    for k in counter:
        if counter[k] != 0:
            return False

    return True


print(anagram('dog', 'gad'))
