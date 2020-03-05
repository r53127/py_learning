def findMinAndMax(L):
    if not L:
        return (None, None)
    min=max=L[0]
    for i in L:
        if i<min:
            min=i
        if i>max:
            max=i
    return (min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!',)
else:
    print('测试成功!')