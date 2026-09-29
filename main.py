import re

def clean_and_analyze(text):
    text = text.lower()
    # Убираем всё, кроме букв и пробелов
    clean_text = re.sub(r'[^\w\s]', '', text)
    
    words = clean_text.split()
    
    # Считаем частотность слов
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    return len(words), freq

# Тестируем на смеси языков, чтобы проверить, как работает
sample_text = "Bonjour! Comment allez-vous? Or do you prefer English? In 2026, mixing languages is a big trend, n'est-ce pas?"

total_words, word_freq = clean_and_analyze(sample_text)
print(f"Всего слов: {total_words}")
print(f"Частота: {word_freq}")
