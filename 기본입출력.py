#input() 함수는 한 줄의 문자열을 입력 받는 함수입니다
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용합니다.

#데이터의 개수 입력 5
n = int(input())
#각 데이터를 공백을 기준으로 구분하여 입력 65 90 75 34 99
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# n, m , k를 공백을 기준으로 구분하여 입력 3 5 7
n , m , k = map(int, input().split())

print(n, m , k)
