import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
#1.movies폴더 안의 상세 id파일들을 받을 것.
#1-1. 수입 정보를 받을 것
#2-1. movie detail에서 revenue 정보를 빼오기
#2-1. 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성할 것  

def max_revenue(movies):
    
    for movie in movies:
        mxrevenue=0
        mxmovie =''
        id = movie.get('id')
        movie_details_json = open(f'data/movies/{id}.json', encoding='utf-8')
        #f는 문자열 포맷팅으로, 변동치 위치를 설정하고 설정만 하면 된다()
        #이 경우 변수는 id이므로 id를 설명하면 된다.
        movie_details = json.load(movie_details_json)
        revenue = movie_details.get('revenue')
        if(mxrevenue < revenue):
            mxrevenue = revenue
            mxmovie =  movie_details.get('title')
    return mxmovie
        # if mx_revenue < revenue:
        #     max_revenue = revenue
        #     max_title = movie.get('title')

    

    # revenue = movie_details.get('revenue')
    # if max_revenue < revenue:
    #     mx_revenue = revenue
    #     max_title = movie.get('title')
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
