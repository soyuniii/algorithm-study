# n개 볼링공, 1~m무게 (같은무게 존재가능)
# 각 볼링공에 번호를 부여했을때 두사람이 서로 다른 무게의 볼링공을 고르는 경우의 수 구하기


# 풀이1) 내 풀이
# from itertools import combinations
# n,m = map(int, input().split())
# data = list(map(int, input().split()))

# index_pairs = combinations(range(n),2)

# result = 0

# for i,j in index_pairs:
#     if data[i] != data[j]:
#         result += 1

# print(result)

# 풀이2) combinations없이
# n,m = map(int, input().split())
# data = list(map(int, input().split()))

# result = 0

# for i in range(n):
#     for j in range(i+1, n): #i보다 뒤에있는 공만 비교
#         if data[i] != data[j]:
#             result += 1

# print(result)

# 풀이3) 책 풀이(최소 시간복잡도: O(M)) - A가 공 선택했을때, B가 선택할 수 있는 남은 공의 개수 곱해서 더하는 방식
# n,m = map(int, input().split())
# data = list(map(int, input().split()))

# array = [0]*11 # 1-10 무게 담는 리스트

# for x in data:
#     array[x] += 1 # 각 무게 해당 볼링공 수 카운트

# result = 0

# for i in range(1, m+1):
#     n -= array[i] 
#     result += array[i]*n

# print(result)
