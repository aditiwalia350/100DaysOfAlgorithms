def hanoi(n, source , destination, aux):
    if n == 1:
        print(f"move from {source} to {destination}")
    else:
        hanoi(n-1, source, aux, destination)
        print(f"move from {source} to {destination}")
        hanoi(n-1, aux, destination, source)

hanoi(3, 1, 2, 3)
