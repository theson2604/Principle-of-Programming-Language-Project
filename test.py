from functools import reduce

def flat(param):
    a, b, c, d = param
    print(a,b,c,d)


b = [1,2,3]
a = [[12,3], [2,3,3]]
a[0] = b + a[0]
print(a)