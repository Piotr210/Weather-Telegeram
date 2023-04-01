# def cats(y):
#     print(y)
#
#     def mer(b):
#         b = b + 1
#         print('hello', b)
#         print(kot())
#         return b
#
#
#     return (mer(y))
#
#
# def kot():
#     return ('zhopa')
#
#
# x = 5
# print(cats(x))


a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if i==[3,4]:
            return i
        if type(i) == list:
            return rec(i, level + 1)


print(rec(a))

# def rec(f):
#     if len(f)==1:
#         return f
#     if f[0]=='(':
#         f=f.replace('(',')',1)
#     return rec(f[1:])+f[0]
#
#
#
# a = input()
# print(a+rec(a))
