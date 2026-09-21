### 
# 최악의 경우에도 O(NlogN)보장하는 정렬 라이브러리
#

array = [7,5,9,0,3,1,6,2,4,8]

# 별도의 정렬된 리스트 반환
result = sorted(array)
print(result)

# 내부 바로 정렬
array.sort()
print(array)

# key 사용
array2 = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array2, key=setting)
print(result)