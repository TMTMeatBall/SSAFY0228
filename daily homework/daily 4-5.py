# 코딩테스트 온라인 감독을 하는 중이다. 다음과 같은 딕셔너리를 줬을 때 다음의 요구사항을 수행하라.
test_status = {
    '김코딩': 'solving',
		'이싸피': 'solving',
		'최이썬': 'cheating',
		'오디비': 'sleeping',
		'임온실': 'cheating',
		'조실습': 'solving',
		'박장고': 'sleeping',
		'염자바': 'cheating'
}
# dictionary의 value로 <code>solving</code>, <code>sleeping</code>, <code>cheating</code>이 있다.
# 커닝하고 있는 사람의 상태는 <code>cheating</code>이다.
# 커닝하고 있는 사람을 시험장에서 퇴출해야 한다. <code>test_status</code>에서 상태가 <code>cheating</code>인 요소를 제거하라.
# 커닝을 하고 있는 사람의 리스트를 오름차순으로 출력하라.
# 잠을 자고 있는 사람의 상태는 <code>sleeping</code>이다.
# 잠을 자고 있는 사람을 깨워야 한다. <code>test_status</code>에서 안의 모든 <code>sleeping</code>을 <code>solving</code>으로 바꿔라.
# 위의 모든 요구사항을 수행한 뒤 <code>test_status</code>를 출력하라.
# 출력 예시
# ['염자바', '임온실', '최이썬']
# test_status = {'김코딩': 'solving', '이싸피': 'solving', '오디비': 'solving',
# 		'조실습': 'solving', '박장고': 'solving'}


#컨닝하는 사람을 저장할 리스트
cheaters=[]
for student in test_status:
    if test_status[student]=='cheating':
        cheaters.append(student)
    elif test_status[student]=='sleeping':
        .replace 
    

print(sorted(cheaters))
print(test_status)