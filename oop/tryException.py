# try:
#     n1=int(input('Число №1: '))
#     if n1 < 0:
#         raise TypeError
#     n2=int(input('Число №2: '))
#     if n2<0:
#         raise TypeError
#     print(n1/n2)
# # except ValueError:
# #     print('Потрібно вводити ЧИСЛО')
# # except ZeroDivisionError:
# #     print('Ділення на нуль НЕМОЖЛИВО')
# # except TypeError:
# #     print('Потрібно вводити лише ДОДАТНІ числа')
# except Exception:
#     print('Щось пішло не так... Щось ввели не вірно... Помилка 404')
# finally:
#     print('='*10,'END','='*10)

# banknotes={
#     20:'Іван Франко',
#     50:'Михайло Грушевський',
#     100:'Тарас Шевченко',
#     200:'Леся Українка',
#     500:'Григорій Сковорода',
#     1000:'Володимир Вернадський'
# }
# ans='1'
# while ans=='1':
#     try:
#         nominal = str(input('Введіть номінал банкноти або видатну людину: '))
#         if nominal.isdigit():
#             nominal=int(nominal)
#             print('На банкноті\033[35m', nominal,'\033[0mзображено видатну людину -\033[35m',banknotes[nominal],"\033[0m")
#         else:
#             for key,value in banknotes.items():
#                 if value==nominal:
#                     print('\033[36m',nominal,'\033[0mзображено на купюрі\033[36m',key,'\033[0m')
#                     break
#             else:
#                     raise ValueError
#     except ValueError:
#          print('Неіснуюча видатна людина на банкноті')
#     except KeyError:
#         print('Неіснуюча банкнота')
#     ans=input('Продовжити програму? \nтак-1, ні-0: ')

#ДЗ
import random
my=[random.randint(1,100) for i in range(10)]
# for i in my:
#     print(i,end=" ")
print()
it=iter(my)
print(it)
print(next(it)) #отримати результат наступної ітерації
# Результат залишився без змін, тому що ітератор  –
# одноразовий об’єкт. Тож під час роботи з ним треба не
# допускати його повторного використання

# Як ми вже знаємо, для проведення ітерацій та перетворення об’єктів на ітератори треба мати ітеровані дані.
# Та як зробити ітерованими власні об’єкти? У цьому допоможе стандартний метод __iter__(),
# який має повертати посилання на об’єкт ітератора.
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count = Counter(5)
for elem in count:
            print(elem)