# Day 4 - Python Basics Practice

# 1. If-Else
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2. For Loop
print("\nPrinting numbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# 3. While Loop
print("\nCountdown using while loop:")
count = 5
while count > 0:
    print(count)
    count -= 1


# 4. Function
def add(a, b):
    return a + b

result = add(10, 20)
print("\nSum using function:", result)