# 점수 n을 반으로 나눴을때 양 옆의 각 자릿수의 합이 동일한 상황일때 럭키 스트레이트 기술 사용 가능
# 사용 가능하면 LUCKY, 불가능하면 READY
# Pass

# n = int(input())

# array = []

# while n != 0:
#     array.append(n % 10)
#     n //= 10

# half = len(array)//2

# n1 = sum(array[:half])
# n2 = sum(array[half:])

# if n1 == n2:
#     print("LUCKY")
# else:
#     print("READY")



# 추천 풀이 - 문자열로 저장해서 쓰기
n = input()
half = len(n) // 2

left = sum(int(x) for x in n[:half])
right = sum(int(x) for x in n[half:])

if left == right:
    print("LUCKY")
else:
    print("READY")

