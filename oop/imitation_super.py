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

class Comp:
    def __init__(self,model):
        super().__init__()
        self.model=model
        self.memory=256
class Display:
    def __init__(self):
        super().__init__()
        self.resolution='4k'

class Smart(Comp,Display): #множинне наслідування
    def info(self):
        print('Смартфон моделі',self.model,'має параметри:',self.memory,"Мб пам'яти та розширення дісплея",self.resolution)

telephone1=Smart('Xioma')
telephone1.info()