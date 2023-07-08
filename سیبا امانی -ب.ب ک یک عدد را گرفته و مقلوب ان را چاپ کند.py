num = int(input("لطفاً یک عدد وارد کنید: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10

print("مقلوب عدد وارد شده:", reversed_num)
