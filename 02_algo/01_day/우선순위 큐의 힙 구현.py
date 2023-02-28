list1 = [3, 7, 1, 9, 2, 5]
import heapq  # 우선순위 큐를 만들어주는 라이브러리

heapq.heapify(list1)  # 리스트를 heap구조로 만들어주는 heapify()
print(list1)
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(3, list1))
heapq.heappush(list1, 4)
print(list1)
heapq.heappush(list1, 6)
print(list1)
val = heapq.heappop(list1)
print(val)
print(list1)