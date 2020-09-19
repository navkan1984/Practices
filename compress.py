def compress(s):
    # count = {}
    #
    # for i in s:
    #     if i not in count:
    #         count[i] = 1
    #     else:
    #         count[i] += 1
    #
    # final_output = ''
    # chars = []
    # for i in s:
    #     if i not in chars:
    #         chars.append(i)
    #         final_output = final_output + i + str(count[i])

    if len(s) == 0:
        return None
    if len(s) == 1:
        return s+"1"

    l = len(s)
    cnt = 1
    i = 1
    final_output = ''
    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            final_output = final_output + s[i-1] + str(cnt)
            cnt = 1
        i += 1
    final_output = final_output + s[i-1] + str(cnt)

    print final_output


compress('ABBBCCCCDDDDDDDEE')
