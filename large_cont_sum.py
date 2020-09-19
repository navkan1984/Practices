def large_count_sum(arr):

    length = len(arr)
    if length == 0:
        return 0

    large_sum = arr[0]
    sum = arr[0]
    for num in arr[1:]:
        sum = max(sum + num, num)
        large_sum = max(sum, large_sum)
    print large_sum


large_count_sum([1,2,-1,3,4,10,10,-10,-1])
