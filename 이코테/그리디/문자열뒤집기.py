# 0과 1로만 이로어진 문자열 s에서 연속된 하나 이상의 숫자를 잡고, 모두 뒤집는 행동의 최소 횟수 구하기. 
# 오답노트 - 마지막 그룹 카운트 안됨

string = input()

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우


now = string[0]

for s in string:
    if now != s:
        if now == '0':
            count0 += 1
        else:
            count1 += 1
        now = s

# 마지막 묶음 처리
if now == '0':
    count0 += 1
else:
    count1 += 1


# 다른 풀이 (now없이)

# data = input()

# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

print(min(count0, count1))