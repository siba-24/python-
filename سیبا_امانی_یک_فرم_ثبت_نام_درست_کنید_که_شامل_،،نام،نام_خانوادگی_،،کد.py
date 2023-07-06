from tkinter import Tk, Label, Entry, Button

def submit():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    national_id = entry_national_id.get()
    phone_number = entry_phone_number.get()

    message = f"اطلاعات شما با موفقیت ثبت شد!\nنام: {first_name}\nنام خانوادگی: {last_name}\nکد ملی: {national_id}\nشماره تلفن: {phone_number}"
    submit_message.config(text=message)

root = Tk()
root.title("فرم ثبت نام")

label_first_name = Label(root, text="نام:")
label_first_name.pack()

entry_first_name = Entry(root)
entry_first_name.pack()

label_last_name = Label(root, text="نام خانوادگی:")
label_last_name.pack()

entry_last_name = Entry(root)
entry_last_name.pack()

label_national_id = Label(root, text="کد ملی:")
label_national_id.pack()

entry_national_id = Entry(root)
entry_national_id.pack()

label_phone_number = Label(root, text="شماره تلفن:")
label_phone_number.pack()

entry_phone_number = Entry(root)
entry_phone_number.pack()

submit_button = Button(root, text="ثبت", command=submit)
submit_button.pack()

submit_message = Label(root)
submit_message.pack()

root.mainloop()
