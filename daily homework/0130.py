class Person:
#     def __init__(self,name,age):
#         print('생성될 떄 자동으로 불려요')
#         self.name = name
#         self.age=age


# aiden = Person('aiden',23)


    count = 0
    def __init__(self,name):
        self.name=name
        Person.count +=1
    
    @classmethod
    def number_of_population(cls):
        print(f'인구수는  {cls.count}입니다.')


Person1=Person('ㅁㅁ')
Person2=Person('ㅇㅇ')

Person.number_of_population()
Person1.number_of_population()
Person2.number_of_population()

a= [1,2,3]
b=[1,2,3]
id(a)
id(b)
a is b
a==b
a=b
id(a)
id(b)
a is b
a == b

class Person:
    def __init__(self):

person1=person

class Person
    def __init__(self,name):
            