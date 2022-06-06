# N X M 크기의 2차원 리스트 초기화
from array import array


n = 4
m = 3
array = [[0] * m for _ in range(n)] 
#파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자
#할 때 언더바(_)를 자주 사용합니다.
print(array)