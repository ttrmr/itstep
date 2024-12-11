# class Human:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city
#     def info(self):
#         print('Вітаю! Мене звати',self.name,'мені',self.age,'я з міста',self.city)
# class Pupil(Human):#наслідування
#     def __init__(self,name,age,city,classroom):
#         super().__init__(name,age,city)
#         self.classroom=classroom
#     def stydu(self):
#         return self.name +' я навчаюся у '+str(self.classroom)+' класі'
#
# h1=Human('Антон', 12, 'Запоріжжя')
# h1.info()
# p1=Pupil('Яна',12,'Дніпро',7)
# print(p1.stydu())
# p1.info() #метод info знаход у кл Human