import json
from pprint import pprint
import requests

def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
def movie_info(movies, genres):
    datas=[]
    #1. movies -> movie 하나씩 가져와서 반복하는 코드 작성
    for movie in movies:

    #1.1. genre_ids -> genre_names 바꿔주는 로직 작성하기 
        genre_ids = movie.get('genre_ids')
        genre_names = []#장르에 대한 이름 저장을 리스트화
        #장르순회하면서 거기에 id값이 genre_ids에 들어있다면
        # genre_names에 추가
        for genre in genres:
            if genre.get('id')  in genre_ids:
                genre_names.append(genre.get('name'))
    #1.2. id, overview, poster_path, title, vote_average 키 값 가져오기
    data = {
        'id':movie.get('id'),
        'genre_names': genre_names,
        'overview':movie.get('overview'),
        'poster_path':movie.get('poster_path'),
        'title':movie.get('title'),
        'vote_average':movie.get('vote_average')

    }
        #1.3. movie 정보를 담은 딕셔너리를 담고, 그 결과를 리스트에 추가
    datas.append(data)
    return datas
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
