# count(char, start, end) - підрахунок певнеого елемента

a = 'lorem ipsuM'

# print(a.count('m'))

# lower()
b = 'LOREM IPSUM Abraham'

# print(b.lower())

#upper()

# print(b.upper())

#capitalize()

c = 'lorem ipsum'

# print(c.capitalize())


#swapcase()

g = 'AbCdEfGh'

# print(g.swapcase())

# title()

f = 'lorem ipsum'
# print(f.title())


#find('symbols', start, end) - повертає індекс першого входження шуканого підрядка. повертає -1, якщо не знайдено збігів

s = 'Lorem ipsum dolorem'

# print(s.find('em'))
# print(s.rfind('em'))


# Ввести довільне повідомлення з клавіатури. Якщо в повідомленні трапляються слова «купити», «продати», «реклама», 
# то помітити це повідомлення як спам.

# spqm_words = ["купити", "продати", "реклама"]

# txt = input('Enter some text: ')

# for w in spqm_words:
#     if txt.find(w) != -1:
#         print('spam detected')
#         break



s = "I am learning strings; in Python. ; Some; new methods got now."
sent = s.split('; ') # розділяє рядок за розділювачем. за замовчуванням по пробілу
# print(sent)


sentences = ["I am learning strings in Python", "Some new methods got now."]

txt = '. '.join(sentences)
# print(txt)


# strip() - прибирає пробіли

e = ' slovo '

# print(e.strip())



# replace()

text = 'cats eat korn and cats meow loud'

text1 = text.replace('t', 'dogs')
# print(text1)


#translate()

map = {ord('ж'): 'zh', ord('з'): 'z'}

tr = "жаба з'їла журавля".translate(map)
# print(tr)


#форматування: %   format()   f

r = 'My name is %s. I am %d years' % ('John', 37)
# print(r)


r1 = 'I am {0}. meni {1} years'.format('Oleh', 12)
# print(r1)

name = 'Ololo'
age= 123

s = f'My name is {name}. I am {age} years'
# print(s)


#специфікація

# print('pi: {:0.3}'.format(3.1415926))


# print('"{}", "{:+}", "{:-}", "{: }"'.format(1, 2, -3, 4))

print('|{:-<30}{:-^12}{:->20}|'.format('', '', ''))
print('|{:_<30}|{:*^10}|{:_>20}|'.format('name', 'price', 'weight'))
print('|{:-<30}{:-^12}{:->20}|'.format('', '', ''))



a = '12345678'
print(a[:6])