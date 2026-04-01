def frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

print(frequency([1, 2, 2, 3, 3, 3]))
