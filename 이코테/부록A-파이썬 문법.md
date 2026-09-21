### 리스트 컴프리헨션

```python
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i*i for i in range(1, 10)]
print(array)

# 2차원 배열 초기화 시
n=3
m=4
array = [[0]*m for _ in range(n)]
print(array)
```

### remove_all 기능 구현

```python
a=[1,2,3,4,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)
```

### 딕셔너리

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
print(data[key])
```

### 집합 자료형

```python
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a|b)
print(a&b)
print(a-b)

data=set([1,2,3])
data.add(4)
data.update([5,6])
data.remove(3)

print(data)
```

### 조건부 표현식

```python
score = 85

if score >= 80: result = "Success"
else: result = "Fail"
print(result)

result = "Success" if score >= 80 else "Fail"
print(result)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = []
for i in a:
if i not in remove_set:
result.append(i)

result = [i for i in a if i not in remove_set]

print(result)
```

### global 키워드

→ 함수 밖 변수 바로 참조하기 (지역변수 만들 필요x)

```python
a = 0

def func():
global a
a+=1

for i in range(10):
func()

print(a)
```

### 람다 표현식

```python
def add(a,b):
return a+b

print(add(3,7))

print((lambda a, b: a+b)(3,7))
```

### 입출력

```python
n = int(input())

data = list(map(int, input().split()))

a, b, c = map(int, input().split())

** 빠르게 입력받기
import sys
sys.stdin.readline().rstrip()
```

```python
print("정답은", str(answer), "입니다")
print(f"정답은 {answer}입니다.")
```

### itertools

순열 구하기

```python
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
```

조합 구하기

```python
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
```

순열 구하기 (중복 허용)

```python
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)
```

중복, 순서 상관없이 구하기

```python
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)
```

### heapq

힙정렬

```python
import heapq

def heapsort(iterable):
    h=[]
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

최대힙, 내림차순 힙정렬

```python
import heapq

def heapsort(iterable):
    h=[]
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

### bisect

이진탐색, 정렬된 배열에서

- 특정 원소 찾기

```python
from bisect import bisect_left, bisect_right

a=[1,2,4,4,8]
x=4

print(bisect_left(a,x))
print(bisect_right(a,x))

```

- 특정 범위 원소 개수

```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index

a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4)) #값이 4인 데이터개수
print(count_by_range(a,-1,3)) #값이 [-1,3]범위 데이터 개수
```

### collections

파이썬 큐 → `deque` 사용해서 구현

```python
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
```

`counter` 등장횟수 세기

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
```

### math

```python
import math
print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14)) #최대공약수
print(math.pi)
print(math.e)
```