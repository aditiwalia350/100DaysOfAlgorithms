def rangeToList(k):
    result = []
    for i in range(0, k):
        result.append(str(i))
    return result


def base(n, k):
    if n == 0:
        return []
    if n == 1:
        return rangeToList(k)

    return [str(digit) + str(bitstring) for digit in base(1, k) for bitstring in base(n - 1, k)]


print(base(3, 4))
