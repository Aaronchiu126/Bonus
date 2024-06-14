def sum_lists(d):
    dsl = {}
    for key in d:
        sum = 0
        for val in d[key]:
            sum = sum + val
        dsl[key] = sum
return dsl
d = {0:[1,2,3], 3:[2,3,4,0], -1:[-1,3,4]}
print(sum_lists(d))