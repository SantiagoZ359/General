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
