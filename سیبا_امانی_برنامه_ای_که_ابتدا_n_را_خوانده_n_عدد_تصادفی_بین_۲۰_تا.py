import random

def reverse_array(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

n = int(input("تعداد اعداد تصادفی: "))
numbers = [random.randint(20, 200) for _ in range(n)]

max_num = max(numbers)
max_index = numbers.index(max_num)

sorted_numbers = sorted(numbers)
second_min_num = sorted_numbers[1]
second_min_index = numbers.index(second_min_num)

reversed_numbers = reverse_array(numbers)

print("بزرگترین عدد:", max_num)
print("مکان بزرگترین عدد:", max_index)
print("دومین کوچکترین عدد:", second_min_num)
print("مکان دومین کوچکترین عدد:", second_min_index)
print("ارایه معکوس شده:", reversed_numbers)
