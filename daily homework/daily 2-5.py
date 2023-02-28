# 다음과 같이 tuple를 저장한 list가 있다. 각 tuple의 첫 번째 요소는 해야할 일, 두 번째 요소는 남은 일 수이다.새로운 일정을 입력받아 list에 추가하고 출력하라.
# todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
# 해야 할 일, 그리고 남은 일수까지 총 두 번 입력받는다.
# 입력받은 해야 할 일과 남은 일수는 tuple로 묶는다.
# 남은 일수는 int 형태로 저장한다.

# 입력예시
# Soccer Contest
# 10
# 출력예시
# [("Python Homework", 3), ("Assay", 4), ("Vacation", 100), ("Soccer Contest", 10)]

todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
todo.extend([("Soccer Contest", int(10))])
print(todo)
# todo.insert(3,("Soccer Contest", 10))
print(todo)


type(("Python Homework", 3))
#1 일정을 새로 받아 추가하기
#2 해야할 일, 남은 일수 두번 입력하기
#3 tuple 로 묶기
#4 숫자를 int형태로 저장하기
