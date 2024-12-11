#симулятор життя студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.progress=0 #100
        self.lvLife=True
        self.mood=50 #100

    # методи класу
    def study(self): #навчання
        print("Час для навчання")
        self.progress+=r.randint(3,10)
        self.mood-=r.randint(1,7)
    def sleep(self): #сон
        print("Час для сну")
        self.mood += r.randint(1, 7)

    def chill(self):#відпочинок
        print("Час для відпочинку")
        self.mood += r.randint(3, 10)
        self.progress -= r.randint(1, 7)

    def isLvLife(self):#рівень студ життя
        if self.progress<4:
            print('Ймовірність виключення із закладу')
            self.lvLife=False
        elif self.progress<9:
            print('Підготовка до сесія\nБезсонні ночі')
            self.lvLife=False
        elif self.progress<13:
            print('Екзамен екстерном\nЗбільшення часу на відпочинок')
            self.lvLife = False
    def everyday(self):
        print("\033[32mУспішність:", self.progress,"\nНастрій:",self.mood,"\033[0m")
    def lifeStud(self,day):
        day="\033[34mДень №"+str(day)+"\033[0m"
        print(day)
        rnd=r.randint(1,3)
        if rnd==1:
            self.study()
        elif rnd==2:
            self.sleep()
        elif rnd==3:
            self.chill()
            self.everyday()
            self.isLvLife()

st1=Student("Сашка")
# print(st1.name, "успішність:",st1.progress,st1.lvLife,"настрій:",st1.mood)
print("\033[44mСтуденське життя:", st1.name,"\n\033[0m")#30-37 колір тексту, 40-47 колір фону
for i in range(1,31):
    if st1.lvLife==False:
        break
    st1.lifeStud(i)

st2=Student('Маринки')
# print(st1.name, "успішність:",st1.progress,st1.lvLife,"настрій:",st1.mood)
print("\n\n\033[44mСтуденське життя:", st2.name,"\n\033[0m")#30-37 колір тексту, 40-47 колір фону
for i in range(1,31):
    if st2.lvLife==False:
        break
    st2.lifeStud(i)