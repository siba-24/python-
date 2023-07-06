numbers = []
while True:
    num = input("Enter a number (or '1' to exit): ")
    if num == '1':
        break
    elif num not in numbers:
        numbers.append(num)
numbers.sort()
print(numbers)
