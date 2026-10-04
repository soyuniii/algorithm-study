# n개 동전을 이용해서 만들 수 없는 양의 정수 금액 중 최솟값 구하기
# 보충노트 - target 변수 설정하는 감 잡기

n = int(input())
data= list(map(int, input().split()))
data.sort() # 현재까지 만들 수 있는 금액 범위 확장

target = 1 # 1 ~ (target-1)까지 모든 금액을 만들 수 있는 상태

for x in data:
    if target < x:
        break
    target += x

print(target) # 다음동전 > target이 되는 순간 target이 정답