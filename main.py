import re

def clean_and_analyze_text(raw_text):
    # Приводим всё к нижнему регистру
    text = raw_text.lower()
    
    # Удаляем знаки препинания и цифры с помощью регулярных выражений
    clean_text = re.sub(r'[^\w\s]', '', text)
    clean_text = re.sub(r'\d+', '', clean_text)
    
    # Разбиваем текст на отдельные слова
    words = clean_text.split()
    
    # Считаем общее количество слов и частоту каждого слова
    word_count = len(words)
    word_frequency = {}
    
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
        
    return word_count, word_frequency

# Пример текста для проверки
sample_text = "Bonjour! Hello, NLP world! Natural Language Processing is amazing, isn't it? 123"

total, freq = clean_and_analyze_text(sample_text)
print(f"Total words: {total}")
print(f"Word frequency: {freq}")
