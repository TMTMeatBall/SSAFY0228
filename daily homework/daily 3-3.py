
infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

print(sum([infos[i].get('ages') for i in range(len(infos))])) #range(infos) 니까 0,1 range(0,2) info 안에서 회차를 도는 i 를 넣은 infos 안의 값들의 합
infos[0].get('age') 
total=0
for i in range(len(infos)): #range(infos) 니까 0,1 range(0,2) info 안에서 회차를 도는 i 를 넣은 infos 안의 값들의 합
    total += infos[i].get('age') #total은 그런 infos[i](딕셔너리이므로.get).get('age') 들의 순차적인 합

print(total)

# info = 
# infos[0].get('age') + infos[1].get('age')

# total=0
# for info in infos:
#     info.get['age']


# for info in infos:
#     total = 0
#     #info의 타입은 딕
#     info['age']
#     #info['age']를 total 에 누적시킨다
# # total = sum(info['age']) 새로 쓸 것
#     total = info['age']

# print(total)

# for info in infos[0:]:
#     total=0
#     total += info.get('age')

# print(total)

# infos

# for i in range():
#     infos[i].get('age')

# ages=0
# for i in range(len(infos)):
#     infos[i].values()[1]
#     ages+=infos[i].values()[1]

# print(ages)

