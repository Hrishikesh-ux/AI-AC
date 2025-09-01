def print_multiples(number):
    print(f"First 10 multiples of {number} are:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

num = int(input("Enter a number: "))
print_multiples(num)