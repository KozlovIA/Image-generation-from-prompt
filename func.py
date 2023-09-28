import pymorphy2
from nltk.stem import *
from nltk.tokenize import word_tokenize

_lemmatizer = WordNetLemmatizer()    # для английского текста
_morph = pymorphy2.MorphAnalyzer()
def lemmatize(texts):
    """Функция лемматизации для списка текстов
    text - исходный текст
    res - список лемматизированных текстов
    """
    res = list()
    for text in texts:
        text = str(text)
        text = text.lower()
        nltk_tokens = word_tokenize(text) # разбиваем текст на слова
        line = ''
        for word in nltk_tokens:
            parse = _morph.parse(word)[0].normal_form  # Это было для русских слов
            # дальше обрабатываем все части речи
            lemm_word = _lemmatizer.lemmatize(parse, pos='n')
            lemm_word = _lemmatizer.lemmatize(lemm_word, pos='v')
            lemm_word = _lemmatizer.lemmatize(lemm_word, pos='r')
            lemm_word = _lemmatizer.lemmatize(lemm_word, pos='a')
            lemm_word = _lemmatizer.lemmatize(lemm_word, pos='s')
            line += ' ' + lemm_word
        res.append(line[1:]) # lemmatize для английских слов
    return res

