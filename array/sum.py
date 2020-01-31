
# method 1
# def _sum(arr):
#     return(sum(arr))

# print(_sum([1, 2, 3]))

def _sum1(arr):
    result = 0
    for i in range(len(arr)):
        result = result + arr[i]
    return result

print(_sum1([1, 2, 3]))


