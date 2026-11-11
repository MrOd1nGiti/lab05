text = input("Введите текст: ")

cleaned_text = text.lower().replace(" ", "")

if not cleaned_text:
    print("Нет текста")
else:
    if cleaned_text == cleaned_text[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
