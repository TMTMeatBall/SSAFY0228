# 990101-1999999
# -> 990101*******

def de_identify(text):
    text = text.replace('-', '')
    text = text[:-7] + '*******'
    return text

print(de_identify('990101-1999999'))