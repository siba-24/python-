file1_name = input("نام فایل اول را وارد کنید: ")
file2_name = input("نام فایل دوم را وارد کنید: ")

# خواندن محتوای فایل اول
with open(file1_name, 'r') as file1:
    content = file1.read()

character_to_remove = input("کاراکتر مورد نظر را وارد کنید: ")

# حذف کاراکتر مورد نظر
new_content = content.replace(character_to_remove, '')

# نوشتن محتوای جدید در فایل دوم
with open(file2_name, 'w') as file2:
    file2.write(new_content)
