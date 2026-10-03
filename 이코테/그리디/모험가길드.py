# n명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날 수 있는 그룹 수의 최댓값은?
# 예) n=5, 공포도: 2 3 1 2 2 , 공포도가 x인 모험가는 x명 이상으로 구성해야함

n = int(input())
data = list(map(int, input().split()))

data.sort() # 1 2 2 2 3

result = 0 # 총 그룹 수
size = 0 # 현재 그룹 모험가 수

for i in data:
    size += 1
    if size >= i:
        result += 1
        size = 0

print(result)