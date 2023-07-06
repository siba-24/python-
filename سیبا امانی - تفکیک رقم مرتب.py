number = input("Enter a number: ")
digit_list = list(number)

# shifting digits
if len(digit_list) > 1:
    last_digit = digit_list.pop()
    second_last_digit = digit_list.pop()
    digit_list.append(last_digit)
    digit_list.insert(-1, second_last_digit)

print(digit_list)
