# ###
# 피보나치 수열의 잘못된 예시 
# O(2^N) -> 동일함수 반복 호출

def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(4))

