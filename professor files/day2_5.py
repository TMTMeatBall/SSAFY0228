todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

task = input('해야할 일을 입력: ')
d_day = input('남은 일 수 입력: ')

d_day_integer = int(d_day)

todo.append((task, d_day_integer))

print(todo)