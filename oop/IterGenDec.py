#скорочення спрощення коду, але без повторного використання
#ітератори
# class Counter:
#     def __init__(self,maxNum):
#         self.maxNum=maxNum
#         self.kol=0
#     def __iter__(self):
#         self.kol=0
#         return self
#     def __next__(self):
#         self.kol +=1
#         if self.kol >self.maxNum:
#             raise StopIteration
#         return self.kol
#
# count=Counter(3)
# # for i in count:
# #     print(i,end=' ')
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(iter(count))
# print(next(count))

# num=[4,5,9,6,1]
# numIter=iter(num)
# print(next(numIter))
# print(next(numIter))
# print(next(numIter))

#Реалізувати ітератор для обходу списку слів та виведення їх довжин.
# class WordLen:
#     def __init__(self,word):
#         self.word=word
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>=len(self.word):
#             raise StopIteration
#         listWordLen=len(self.word[self.index])
#         self.index+=1
#         return listWordLen
#
# wordList=["python","c++","java","js","php"]
# wordIter=WordLen(wordList)
# for i in wordIter:
#     print(i,end=' ')

#генератори def ..yield
#Написати генератор для послідовності ступенів числа 3 (3^0, 3^1, 3^2...).
# def powerNum(num):
#     for i in range(num+1):
#         yield 3**i
# for i in powerNum(4):
#     print(i)

#Реалізувати генератор, який видає послідовність випадкових букв алфавіту.
# import  random as r
# def abc(num):
#     letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     for i in range(num):
#         yield r.choice(letters)
# for i in abc(7):
#     print(i,end=' ')

#декоратори @ допоміжна функція (вкладеність функцій)

# def calcAudit(num,*args,**kwargs):
#     try:
#         res=num(*args,**kwargs)
#     except Exception as e:
#         print('Сталася якась проблема',e)
#     else:
#         print('Результат: ',res)
# def calc(num):
#     return eval(num)
# calcAudit(calc,'(12+2)*3-1')


# def calcAudit(num):
#     def calcAudit(*args,**kwargs):
#         try:
#             res=num(*args,**kwargs)
#         except Exception as e:
#             print('Сталася якась проблема',e)
#         else:
#             print('Результат: ',res)
#     return calcAudit
# @calcAudit
# def calc(num):
#     return eval(num)
# calc('(12+2)*3-1')


# Завдання 1
class NumbersIterator:
    def __init__(self, numbers, max_iterations):
        self.numbers = numbers
        self.max_iterations = max_iterations
        self.current_index = 0
        self.iteration_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration_count >= self.max_iterations:
            raise StopIteration

        while self.current_index < len(self.numbers):
            number = self.numbers[self.current_index]
            self.current_index += 1
            if number % 2 == 0:
                self.iteration_count += 1
                return number
        raise StopIteration


numbers = list(range(1, 21))
iterator = NumbersIterator(numbers, max_iterations=5)
for even_number in iterator:
    print(even_number)

# Завдання 2
import random
import string


def random_letter_generator():
    while True:
        yield random.choice(string.ascii_lowercase)


def YgadaiBykvy():
    generator = random_letter_generator()
    target_letter = next(generator)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = input("Угадайте букву: ").lower()
        if guess == target_letter:
            print("\nВи угадали букву!")
            return
        else:
            print("Не правильно! спробуй знову!")
            attempts += 1
    print(f"\nУ тебе немає спроб угадати літеру! Літера була='{target_letter}'.")


YgadaiBykvy()

#Завдання 3
def ScaningErorrors(func):
    def Scaner(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            print("Error: All arguments must be numbers.")
            return None
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
        return Scaner
@ScaningErorrors
def divide(a, b):
    return a / b
print(divide(15, 3))
print(divide(10, 0))
print(divide(15, "2"))