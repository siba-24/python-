# باز کردن فایل اول برای خواندن
with open('فایل۱.txt', 'r') as file1:
    # خواندن محتوای فایل اول
    content = file1.read()

# باز کردن فایل دوم برای نوشتن
with open('فایل۲.txt', 'w') as file2:
    # نوشتن محتوای فایل اول در فایل دوم
    file2.write(content)
