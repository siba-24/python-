with open('file.txt', 'w') as file:
    while True:
        # دریافت جمله از کاربر
        sentence = input("لطفاً جمله را وارد کنید: ")
        
        # نوشتن جمله در فایل
        file.write(sentence + "\n")
        
        # بررسی خاتمه وارد شدن توسط کاربر
        if sentence == "":
            break

# بستن فایل
file.close()
