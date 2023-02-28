# Point 클래스와 Rectangle 클래스에 대한 명세 및 실행 예시를 참조하여 클래스를 구현하시오.
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
#1. 인스턴스가 기본으로 갖는 self. 그리고 point(x,y)로 출력해야 하므로 인자를 self,x,y       
#2. lp1(x)-p2(x)l값과 lp1(y)-p2(y)l 절대값(abs())을 비교해서 같은 경우 True 로 반환한다. False인 경우에는 False를 반환한다.
#3. 넓이와 둘레를 구한다
class Rectangle():
    def __init__(self,p1,p2):
        self.p1=p1 
        self.p2=p2
    def get_area(self):
        return abs(self.p1.x-self.p2.x)*abs(self.p1.y-self.p2.y) # '.'통해서 메소드와 인자 모두를 콜 하는데 사용 즉, p1의 x값을 출력한다면 self.p1.x 는 p1의 x값, self.p2.y는 p2의 y값
    def get_perimeter(self):
        return abs(self.p1.x-self.p2.x)*2 + abs(self.p1.y-self.p2.y)*2
    def is_square(self):
        return abs(self.p1.x-self.p2.x) == abs(self.p1.y-self.p2.y) 

# # 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# # 출력 예시
# # 4
# # 8
# # True

# # 9
# # 12
# # True
# #1. x,y좌표를 받는다
# #2. lp1(x)-p2(x)l값과 lp1(y)-p2(y)l 절대값(abs())을 비교해서 같은 경우 square 로 반환한다. False인 경우에는 False를 반환한다.
# #3. 넓이와 둘레를 구한다
# #4. 
# class Sagak():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


#     def area(self):
#         return abs(x1-x2)**2

#     def perimeter(self):
#         return abs(x1-x2)*4

#     def square(self):
#         if abs(x1-x2) != abs(x1-x2):
#             return False

#         else:
#             return 'Square'
