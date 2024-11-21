def T(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 4 * x
    else:
        return 2 * T(n - 1, x) - T(n - 2, x)

# Menghitung T(30, 25)
result = T(30, 25)
print(f"T(30, 25) = {result}")