flag = True
count = 0
combination = []
for i in range(100) :
    for j in range(100) :
        for k in range(100) :
            if(i*j + j*k == i * j* k) :
                #count 가 올라갈 떄의 i j k 조합을 저장하기
                combination.append([i,j,k])
                count+=1
            if(count == 3) :
                flag = True
                break
        if(flag) :
            break
    if(flag) :
        break
print(combination) #[0, 0, 0, 0, 0, 1, 0, 0, 2]extend 메서드
#[[0,0,0],[0,0,1],[0,0,2]] append 메서드
