import requests

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=vIY5bgArwFbizC8ynM7%2FaH%2FXhc8AgX5uepTc%2F94eHgXt2O0fP6wUf1fO9qPZZFC%2FhnoTNmfjfQV%2F0oeuFb4n4g%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%8C%80%EA%B5%AC&ver=1.0'

response = requests.get(url, verify=False)
data = response.json()

count = data.get('response').get('body').get('totalCount')
hap = 0
for item in data.get('response').get('body').get('items'):
    hap += int(item.get('pm10Value'))

print(f"대구의 미세먼지 농도는 : {hap / count:.2f}")

