import itertools

def rec_sum(n):
    if n == 0:
        return n
    else:
        return n + rec_sum(n - 1)


def sum_func(n):
    if n == 0:
        return n
    else:
        return n % 10 + sum_func(n / 10)


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output


def reverse(s):
    n = len(s)
    if n <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


def permute(s):
    permutations = list(itertools.permutations(s))
    print([''.join(permutation) for permutation in permutations])


def permutate(s, cand=""):
    if len(s) == 0:
        print(cand)

    for i in range(len(s)):
        newcand = cand + s[i]
        newrem = s[:i] + s[i+1:]
        print newcand, newrem
        permutate(newrem, newcand)
permutate('abc')

#print(reverse('a'))

# print rec_sum(6)

# print sum_func(4315)

# print(word_split('ilovedogsjohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'john']))
