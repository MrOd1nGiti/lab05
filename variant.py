text = input("Введите текст: ")

words = text.split()
matched_words = []

for word in words:
    cleaned_word = word.strip(".,!?;:").lower()
    if not cleaned_word:
        continue
    if cleaned_word.startswith("а"):
        matched_words.append(cleaned_word)

if matched_words:
    for word in matched_words:
        print(word)
    print(f"Всего слов: {len(matched_words)}")
else:
    print("Нет совпадений")
    print("Количество: 0")
