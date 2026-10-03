# 문자열 s가 주어질때, 숫자 사이 x / + 연산자를 넣어 결과적으로 가장 큰수를 구하는 프로그램 
# 연산자 우선순위 무시, 왼->오 연산
# -> 0이 있으면 더하기, 외에는 무조건 곱하기

# 오답노트: 1을 더하는게 더 큰 예외 추가 고려


s = input()
numbers = list(map(int, s))
result = numbers[0]

for i in range(1, len(numbers)):
    # if numbers[i] == 0 or result == 0: 
    if numbers[i] <=1 or result <= 1:
        result += numbers[i]
    else:
        result *= numbers[i]

print(result)