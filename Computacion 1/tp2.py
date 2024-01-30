#1
print('hello, world!')

#2

a = 1;
b = 3;

print(a + b);
print(b - a);
print(a * b);

#3

def print_first_n_perfect_squares(n):
    for i in range(1, n + 1):
        square = i ** 2
        print(square)

n = int(input("Ingrese un número entero: "))
print_first_n_perfect_squares(n)

#4

def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    
    if len(unique_nums) >= 2:
        return unique_nums[-2]
    else:
        return "No hay segundo número más grande."

numbers = [2, 3, 6, 6, 5]
result = second_largest(numbers)
print("El segundo número más grande es:", result)

# 5
def generate_combinations(X, Y, Z, N):
    result = []

    for i in range(X + 1):
        for j in range(Y + 1):
            for k in range(Z + 1):
                if i + j + k != N:
                    result.append((i, j, k))

    return result

X = int(input("Ingrese el valor de X: "))
Y = int(input("Ingrese el valor de Y: "))
Z = int(input("Ingrese el valor de Z: "))
N = int(input("Ingrese el valor de N: "))

combinations = generate_combinations(X, Y, Z, N)
print("Lista de combinaciones:")
for combination in combinations:
    print(combination, end=", ")
