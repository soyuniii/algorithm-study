# 최소한의 비용으로 2개의 최소신장트리로 분할

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0]*(v+1)

edges = []
result = 0 # 전체 노드를 하나의 트리로 연결할때 드는 총비용

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0 # 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우만 집합에 포함시키기
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last) # 최소비용으로 2개의 신장트리 만든 결과