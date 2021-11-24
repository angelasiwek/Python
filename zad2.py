def sumOfitems(l: list):
    result = []
    for item in l:
        if isinstance(item, (list, tuple)):
            result.append(sum(item))
        else:
            result.append(0)
    return result

l = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(sumOfitems(l))