# 알파벳 대문자, 숫자로 구성된 s -> 알파벳 오름차순 정렬 + 숫자합 출력
# 오답노트 - 숫자가 존재하지 않는경우 예외처리 주의@

# string = input()

# num = 0
# array = []
# has_digit = False

# for s in string:
#     if s.isdigit():
#         num += int(s)
#         has_digit = True
#     else:
#         array.append(s)

# array.sort()

# if has_digit:
#     print("".join(array) + str(num))
# else:
#     print("".join(array))


# 책 풀이

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))