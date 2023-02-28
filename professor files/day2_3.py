text = 'saFe eMotion Nail' #input()
text = text.lower()

def is_valid(words):
    for idx in range(len(words) - 1):
        if words[idx][-1] != words[idx+1][0]:
            return False
    return True


words = text.split()

if is_valid(words):
    print('Fail')
else:
    print('success')
