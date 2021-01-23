def check(A):
    if len(A) == 1:
        return True
    return A[0] < A[1] and check(A[1:])


print(check([1, 2, 3, 4, 5, 2]))
print(check([1]))
print(check([-10, 1, 2]))