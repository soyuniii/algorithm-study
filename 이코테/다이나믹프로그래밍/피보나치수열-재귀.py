###
# 피보나치 수열 -> 메모이제이션 이용
# O(N) 재귀함수 이용 - 오버헤드 발생 가능
# Top-Down: 큰 문제 해결 위해 작은 문제 호출 (재귀, 하향식, 오버헤드)

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))