data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {
    '홍길동': 97,
    '이순신': 98
}

print(b)
print(b['이순신'])

key_list = b.keys()
print(key_list)

key_list = list(b.keys())
print(key_list)