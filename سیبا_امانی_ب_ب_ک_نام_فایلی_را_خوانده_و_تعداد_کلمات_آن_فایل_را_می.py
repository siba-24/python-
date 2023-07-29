def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("فایل مورد نظر یافت نشد.")
        return -1

file_name = input("لطفاً نام فایل را وارد کنید: ")
word_count = count_words_in_file(file_name)
if word_count != -1:
    print("تعداد کلمات در فایل:", word_count)
