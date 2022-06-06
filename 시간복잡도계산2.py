# 2중 반복문을 이용하는 프로그램 예제

array = [3, 5, 1, 2, 4] 
sum = 0
for i in array:
    for j in array:
        temp = i * j
        sum += 1
        print(temp)
print(sum)
#  시간복잡도 : O(N^2)