def rev_word(s):
    length = len(s)
    space = ' '
    words = []
    i = 0
    while i < length:
        if s[i] != space:
            word_start = i
            while i < length and s[i] != space:
                i += 1
            words.append(s[word_start:i])
        i += 1
    print words


rev_word('      space before')
