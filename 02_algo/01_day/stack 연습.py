# # 큐에 값을 넣는 함수
# # 큐의 값을 뺴는 함수
# def enqueue(item):
#     global rear
#     if is_full():
#         print('queue is full')
#     rear += 1  # rear 가 한칸 뒤로 밀려나면서 해당 위치의 아이템을 삭제
#     queue[rear] = item
#
#
# def dequeue(item):
#     global front
#     if is_empty():
#         print('queue is empty')
#     front += 1  # front 가 한칸 앞으로 오면서
#     return queue[front]
#
#
# max_size = 100
# queue = [0] * max_size
# front = -1
# rear = -1
#
#
# def is_empty():
#     global front, rear
#     return front == rear
#
#
# def is_full():
#     global front, rear
#     return rear == max_size - 1
#
#
# def Qpeek():
#     global front
#     return queue
#
#
# enqueue(1)
# enqueue(2)
# enqueue(3)
#
#
# def enqueue(item):
#     queue.append(item)
#
#
# def dequeue():
#     if is_empty():
#         print('queue is empty')
#     return queue.pop(0)
#
#
# def is_empty():
#     return len(queue) == 0
#
#
# # def is_full():
# #     return #사실상 만들 이유없음
# def qpeek():
#     if is_empty():
#         print('queue is empty')
#     return queue[0]

#파이썬에 기본 내장된 queue모듈 두 가지의 소개
#1. queue 모듈 자료구조
# from queue import Queue
# q = Queue()
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(40)
# print(q.get())
# print(q.get())
# print(q.get())
#print(q.get())#큐가 비어있으면 정지한다..
# print('코드 끝!')
#2. collections 모듈 deque 자료구조
from collections import deque #기본적인 queue자료구조보다 더욱 자유롭다.
q = deque()
#앞 삽입
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
#뒤 빼기
print(q.pop())
print(q.pop())
print(q.pop())
