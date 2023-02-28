import json


# def dec_movies(movies):
#     # 여기에 코드를 작성합니다.  
# #.movies폴더 안의 상세 영화들의 정보 받기
# #.개봉일 정보 받기
# #.12월에 개봉한 영화들의 제목을 리스트로 출력하는 dec_movies
def dec_movies(movies):
    for movie in movies:
        dec_movies = ['title','release_date']
        id = movie.get('id')
        movie_details_json = open(f'data/movies/{id}.json', encoding='utf-8')
        #f는 문자열 포맷팅으로, 변동치 위치를 설정하고 설정만 하면 된다()
        #이 경우 변수는 id이므로 id를 설명하면 된다.
        movie_details = json.load(movie_details_json)     
        print(movie_details.get('release_date').split('-')[1])
        if '12' == movie_details.get('release_date').split('-')[1]:
            #날짜는 0000-00-00으로 나열되므로 split('-')하면 0,1,2항목 중 1인 month가 나올 것
            if movie_details.get('title') != None:
                dec_movies.append(movie_details.get('title'))
#죄송합니다..
    #     in_12 = []
    #     id = movie.get('id')
    #     movie_details_json = open(f'data/movies/{id}.json', encoding='utf-8')
    #     movie_details = json.load(movie_details_json)
    # # print(movie_details.get('release_date').split('-')[1])
        # if '12' == movie_details.get('release_date').split('-')[1]:
        #     if movie_details.get('title') != None:
        #         in_12.append(movie_details.get('title'))
            
    # return in_12
    
#    datas =[]
#    result=[]
#    for movie in movies:
#         data{
#             'id' :movie.get('id'),
#             'release_date' : movie.get('release_date')
#         }
#         datas.append(data)
#         if movie.get('release_date').split()
#         id = movie.get('id')
#         movie_details_json = open(f'data/movies/{id}.json', encoding='utf-8')
#         #f는 문자열 포맷팅으로, 변동치 위치를 설정하고 설정만 하면 된다()
#         #이 경우 변수는 id이므로 id를 설명하면 된다.
#         movie_details = json.load(movie_details_json)
#         date = movie_details.get('release_date')
#         if(mxrevenue < revenue):
#             mxrevenue = revenue
#             mxmovie =  movie_details.get('title')
#     return mxmovie
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
