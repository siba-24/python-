input_string = "Hello World"
print("طول رشته:", get_string_length(input_string))
print("تبدیل حروف کوچک به بزرگ و برعکس:", convert_case(input_string))

substring = "o"
print("تعداد تکرار رشته '{}' در رشته '{}':".format(substring, input_string), count_substring(input_string, substring))

old_substring = "World"
new_substring = "Universe"
print("جایگزینی رشته '{}' با رشته '{}' در رشته '{}':".format(old_substring, new_substring, input_string), replace_substring(input_string, old_substring, new_substring))

print("جدا کردن کلمات رشته:", separate_words(input_string))
