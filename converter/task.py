# slovnik = {
#     'name': 'John',
#     'age': 27
# }

# # print(slovnik['name'])

# # for i in slovnik:
# #     print(i)

# # for i in slovnik.values():
# #     print(i)

# # for keys, values in slovnik.items():
# #     print(f'{keys}, {values}')


# slovnik['occupation'] = 'ingeneer'

# # print(slovnik)

# elem = slovnik.get('name')

# # print(elem)


# uah_to_eur  = 43.39

# uah_to_usd  = 42.10

# eur_to_uah = 1 / 43.39

# usd_to_uah  = 1 / 42.10

# def convert_currency(amount, from_currency, to_currency):
#     if from_currency == "USD" and to_currency == "UAH":              
#      return amount * usd_to_uah
#     elif from_currency == "EUR" and to_currency == "UAH":
              
#      return amount * eur_to_uah
#     elif from_currency == "UAH" and to_currency == "USD":
    
#      return amount * uah_to_usd  
#     elif from_currency == "UAH" and to_currency == "EUR":

#      return amount * uah_to_eur
#     elif from_currency == "USD" and to_currency == "EUR":

#      return amount * usd_to_uah * uah_to_eur 
#     elif from_currency == "EUR" and to_currency == "USD":

#      return amount * eur_to_uah * uah_to_usd 
#     else:
#      print("Поддерживаются только конверсии между USD, EUR и UAH.")

# from_currency = input("Введите исходную валюту (USD, EUR, UAH): ").upper()

# to_currency = input("Введите целевую валюту (USD, EUR, UAH): ").upper()

# amount = float(input("Введите сумму для конвертации: "))

# result = convert_currency(amount, from_currency, to_currency)

# result = convert_currency(amount, from_currency, to_currency)

# if result:
#     print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

x = 0

while x < 10:
    x+=3
    print(x)