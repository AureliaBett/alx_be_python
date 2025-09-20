pattern = int(input("Enter the size of the pattern:"))
i=1

while i <= pattern:
    for j in range(1, pattern+1):
        print("*", end=" ")
    print()
    i += 1