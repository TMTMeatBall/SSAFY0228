#원래의 스테이크 가격과 VAT, VAT가 포함된 실제 결제 금액을 계산하여, 아래와 같이 출력하라.

steak = 50000
vat=int(steak*0.15)
print(vat)
total = steak + vat
print(total)
' {:-4} steak {:-3} vat {:-4} total'.format(steak, vat, total)