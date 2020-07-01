def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val in inverse:
            inverse[val].append(key)
        else:
            inverse[val] = [key]
    return inverse

x = {'b': 1, 'a': 3, 'n': 3}
y = invert_dict(x)
print(y)