def all_strings(n):
    if n == 0:
        return []
    if n == 1:
        return [str(0), str(1)]
    return [digit + bitstring for digit in all_strings(1) for bitstring in all_strings(n-1)]

print(all_strings(3))
