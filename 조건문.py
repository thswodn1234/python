x = 15
if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")


#파이썬에서는 코드의 블록을 들여쓰기로 지정합니다

score = 85

if score >= 70:
    print("성적이 70점 이상입니다.")
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print("성적이 70점 미만입니다.")
    print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')