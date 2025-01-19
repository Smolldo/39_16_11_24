# Завдання 1 - Видалення дублікатів слів у рядку
# Імплементуйте функцію, яка приймає рядок тексту і повертає новий рядок, де всі дублікати слів видалені.

txt = 'lorem ipsum dolores ipsum ipsum ipsum'

def del_dulps(t):
    word = t.split()
    uniq = set(word)
    return uniq
    # return set(word)


# print(del_dulps(txt))

# Напишіть функцію, яка рахує кількість цифр у заданому рядку.
t = 'jsfhsdfgw34234jhksfhjsdbyujk324234234jlsdfhszdhf3472341'

def num_count(t):
    return sum(1 for i in t if i.isdigit())

# print(num_count(t))


# Створіть функцію, яка аналізує текст та виводить слово, що найчастіше зустрічається.
txt = 'lorem lorem ipsum dolores ipsum ipsum ipsum'

def most_common(t):
    words = t.split()
    lst1 = []
    for i in set(words):
        lst1.append([i, words.count(i)])
    return lst1

# print(most_common(txt))


from collections import Counter

def mc(t):
    words = t.split()
    wc = Counter(words)
    return wc.most_common(1)[0][0]

print(mc(txt))


