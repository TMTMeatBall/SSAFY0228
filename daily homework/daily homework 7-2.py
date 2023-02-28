# 학습주제Python에 대한 기본 지식 - 구문, 
# Python 콘솔에서 함수 작성 및 호출, 변수 생성, 입력 읽기 및 출력 생성Python 실행 환경을 위한 텍스트 편집기 또는 IDE 사용에 대한 지식
# Python 프로그램을 실행하는 방법에 대한 정보Python 키워드Python에서 예외를 발생시키는 방법 이해  학습목표OOP(개체 지향 프로그래밍) 개념을 사용하여 문제를 모델링하는 방법을 이해한다.
# 클래스, 특성 및 메서드와 같은 OOP 개념을 사용하여 모델을 작업 코드로 변환하는 방법을 학습한다.
# # 개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라. 
# i.        초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.    
# ii.        bark() 메서드를 호출하면 개는 짖을 수 있다.    
# iii.        클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.                       
# 개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다. 개가 죽으면 num_of_dogs의 값이 1 감소한다.    
# iv.        get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다 

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        Doggy.num_of_dogs+=1
        Doggy.birth_of_dogs +=1

    def __del__ (self):
        Doggy.num_of_dogs=Doggy.num_of_dogs - 1
    
        
    def bark(self):
        return '멍멍으르렁컹컹왈랄랄루'
    def get_status(self):
        return Doggy.birth_of_dogs,Doggy.num_of_dogs


dog1=Doggy('뽀삐','시츄')
dog2=Doggy('맥스','리트리버')
dog3=Doggy('몰루','코커스패니얼')
dog4=Doggy('코코','허스키')
dog5=Doggy('야스오','시바')
print(dog4.bark())
print(dog3.bark())
print(dog2.get_status())
dog4.__del__()
print(Doggy.get_status(dog4))

# dog_instance=Doggy()
# del dog_instance
# dog_instance.dog_attribute
# dog_instance.dog_method



#     # 인스턴스가 메모리에 올라가지 않아서 오류가 난다?

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def hello(self):
#         return f'안녕하세요 {self,name} 입니다.'



# person1 = Person('지민')
# print(person1.name)
# # 또는 person 에 직접 hello 를 호출하기
# #print(person1.hello())
# #print(person.hello(person1))