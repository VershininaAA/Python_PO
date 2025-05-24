def count_character_occurrences(text):
    """Подсчитывает количество вхождений каждой буквы в тексте"""
    occurrences = {}
    for character in text.lower():
        if character.isalpha():
            occurrences[character] = occurrences.get(character, 0) + 1
    return occurrences

def calculate_relative_frequencies(count_dict):
    """Вычисляет относительную частоту каждой буквы"""
    total = sum(count_dict.values())
    frequencies = {}
    for char, count in count_dict.items():
        frequencies[char] = round(count / total, 3)  
    return frequencies


poem_text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

character_counts = count_character_occurrences(poem_text)
char_frequencies = calculate_relative_frequencies(character_counts)

print("Анализ частоты букв в поэме 'У лукоморья дуб зелёный':")
for char, freq in sorted(char_frequencies.items()):
    print(f"Буква '{char}': относительная частота {freq:.3f}")
