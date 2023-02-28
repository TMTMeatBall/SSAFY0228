a = 3
b = 6
c = - 5


root1= round((-b+(b**2-4*a*c)**0.5)/2*a,5)
root2= round((-b-(b**2-4*a*c)**0.5)/2*a,5)
#1.분기점(+,-)
root = (root1, root2)

print(root)


#2방식 function 지정으로 복잡한 수식을 정리하기

def D (a, b, c):
    z_1 =round((-b - (b**2-4*a*c)**0.5)/2*a,5)
    z_2 =round((-b + (b**2-4*a*c)**0.5)/2*a,5)
    return z_1, z_2
D(3, 6, -5)







# def root():
#     D=(b**2)-(4*a*c)
#     if D>0:
#         rootP = (-b + (b**2-4*a*c)**0.5)/(a*2)
#         rootN = (-b - (b**2-4*a*c)**0.5)/(a*2)
#         print('해는 {} 또는 {}'.format(rootP,rootN))
#     elif D==0:

#     else:
#         rootP = (-b + (b**-4*a*c)**0.5)/(a*2)
#         rootN = (-b - (b**-4*a*c)**0.5)/(a*2)


# def root():
#     rootP = (-b + (b**2-4*a*c)**0.5)/(a*2)
#     rootN = (-b - (b**2-4*a*c)**0.5)/(a*2)
#     print('해는 {} 또는 {}'.format(rootP,rootN))
#     return
# a=3
# b=6
# c=-5

# print(root)

num1 = 0
num2 = 1
def func1(a,b):
    return a+b
def func2(a,b):
    return a-b



# 1. a, b, c로 근의 공식
# 2. 이차방정식의 근을 튜플 형식으로 출력


root = ('')

1=('')

#리스트 뽑고 튜플로