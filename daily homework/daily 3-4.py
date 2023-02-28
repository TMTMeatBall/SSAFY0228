blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

# blood_dict = dict()
blood_types.count('A')
blood_list=['A','B','O','AB']
blood_counts=[blood_types.count('A'),blood_types.count('B'),blood_types.count('O'),blood_types.count('AB')]
blood_dict=dict(zip(blood_list,blood_counts))
blood_dict


# for blood_type in blood_types:
    

    #is in get 등을 사용해서 해결 가능하다
    # if blood_type in blood_dict:
#1. 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, 
#2. key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오.





    # blood_dict.get(blood_type, '(A,O,B,AB)')