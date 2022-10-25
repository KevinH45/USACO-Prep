def array_diff(a, b):
    b_set = set(b)
    new_a = []
    for i in a:
        if i not in b_set:
            new_a.append(i)
    return new_a
