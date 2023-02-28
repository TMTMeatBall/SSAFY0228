steak = 50000
vat = int(steak * 0.15)
print(f'스테이크{steak:>9,}\n+ VAT{vat:>11,}\n총계 \\{(steak + vat):>10,}')