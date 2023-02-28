a = ['BCCCACCB', 'CABCACAB', 'BAACCCAC', 'BBABBABC', 'CCABABCA', 'CABABACC', 'CBACACAB', 'CBCCCBAB']
#행 출력해보기
print(len(a))

for i in range(len(a)):
    print(a[i])
#열 출력
#열은 고정시키면서,행은 바뀐다. 고정된 열의 행이 끝까지 닿으면, 열이 다음 것으로 바뀐다.
#배열 내 배열의 원소에 접근해야 한다.
for i in range(len(a[0])):
    for j in range(len(a)):
        print(a[j][i], end=' ')
    print()
