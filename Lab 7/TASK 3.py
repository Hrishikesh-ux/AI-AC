# This code writes "Hello, world!" to example.txt without errors
with open("example.txt", "w") as f:
    f.write("Hello, world!")

with open("data1.txt", "w") as f1, open("data2.txt", "w") as f2:
    f1.write("First file content\n")
    f2.write("second file content\n")

print("Files written successfully")

# Ensure output.txt exists before reading
with open("output.txt", "w") as output:
    output.write("This is a sample line.\nAnother line.")

with open("output.txt", "r") as data, open("output_upper.txt", "w") as output:
    for line in data:
        output.write(line.upper())
    print("Processing done")

# Ensure numbers.txt exists before reading
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5\n")

with open("numbers.txt", "r") as f:
    nums = f.readlines()
squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")
    print("Squares written")