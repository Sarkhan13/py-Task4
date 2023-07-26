#1

dict1 = {'adiniz': 'Serxan', 'soyadiniz': 'Elili', 'mailiziz': 'serxan95.elili@gmail.com'}

dict2 = {'adiniz': 'Vusal', 'soyadiniz': 'Heyderov', 'mailiziz': 'vusal.heyderli@gmail.com'}

dict3 = {'adiniz': 'Ferid', 'soyadiniz': 'Veliyev', 'mailiziz': 'ferid2010@gmail.com'}

for key, value in dict1.items():
    print('Istifadecinin ' + key + ' ' + value+'dir')

for key, value in dict2.items():
    print('Istifadecinin ' + key + ' ' + value+'dir')

for key, value in dict3.items():
    print('Istifadecinin ' + key + ' ' + value+'dir')


#2

def func(**kwargs):
    for key, value in kwargs.items():
        print('Istifadecinin ' + key + ' ' + value+'dir')
        print('---------')

print(func(adiniz = 'Serxan', soyadiniz = 'Elili', mailiniz = 'serxan95.elili@gmail.com'))

print(func(adiniz = 'Vusal', soyadiniz = 'Heyderov', mailiniz = 'vusal.heyderli@gmail.com'))

print(func(adiniz = 'Ferid', soyadiniz = 'Veliyev', mailiniz = 'ferid2010@gmail.com'))