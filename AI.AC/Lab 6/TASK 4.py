def sum_to_n(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

num = int(input("Enter a number: "))
print(f"Sum of first {num} natural numbers is: {sum_to_n(num)}")