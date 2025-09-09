#take input
print("Mirrored half pyramid pattern of stars (*):")
n = int(input("Enter the number of rows:"))
# Outer loop to handle the number of rows
for i in range(n):
    # Inner loop to handle spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Inner loop to handle the asterisks
    for j in range(i + 1):
        print("*", end="")
    print()