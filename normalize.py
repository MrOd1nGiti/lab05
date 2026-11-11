text = input("Введите текст: ")

words = text.split()
normalized_text = " ".join(words)
word_count = len(words)

print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(normalized_text)}")
print(f"Нормализованный текст: {normalized_text}")
print(f"Количество слов: {word_count}")
