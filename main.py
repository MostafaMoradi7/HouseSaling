# string len == n
# kth chracter which has not been repeated before
# Mostafa Moradi


def findKthCharacter(string, target):
    chars = {}
    k = 0
    # idx = -1
    for i in range(len(string)):
        if chars.__contains__(string[i]):
            chars[string[i]] = chars[string[i]] + 1
        else:
            chars[string[i]] = 0

    for i in range(len(string)):
        if chars[string[i]] == 0:
            k = k + 1
        if k == target:
            return string[i]


print(findKthCharacter("MostafaMoradi", 3))

# for i in range(len(string)):
#     if chars[string[i]] == 0 and k == target:
#         return chars[string[i]]
#     elif()
# return idx


# same as Divar
# User interactions:
# 1.renting Houses
# 2.buy houses
