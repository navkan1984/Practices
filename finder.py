def finder(arr1, arr2):

    count = {}

    for num in arr1:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    for num in arr2:
        if num not in count:
            count[num] = 1
        else:
            count[num] -= 1

    for keys, values in count.iteritems():
        if values > 0:
            print keys


finder([1,2,3,4,5,6,7,5], [3,7,2,1,6,4,5])