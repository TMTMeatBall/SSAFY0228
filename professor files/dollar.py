import requests

url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'

data = requests.get(url).json()[0]
currencyName = data.get('currencyName')
openingPrice = data.get('openingPrice')

print(f'원화와 {currencyName}의 환율은 현재 {openingPrice}원 입니다.')