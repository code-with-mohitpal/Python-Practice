def group_anagrams(strs):
    d = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in d:
            d[key] = []
        d[key].append(s)
    return list(d.values())
