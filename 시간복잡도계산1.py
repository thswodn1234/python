# N개의 데이터의 합을 계산하는 프로그램 예제

array = [3, 5, 1, 2 ,4]
summary = 0

for x in array:
    summary += x

print(summary)

# 수행 시간은 데이터의 개수 N에 비례할 것임을 예측할 수 있습니다.
#  - 시간복잡도: O(N)