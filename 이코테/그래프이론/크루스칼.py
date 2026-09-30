###
# 크루스칼 알고리즘
# 최소 신장 트리 - 최소비용으로 모든 노드를 포함하며 사이클이 존재하지 않는 부분의 그래프 만들기
# O(ElogE) -> 간선 정렬하는 시간

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
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용 순 정렬 위해 첫번째 원소를 비용으로 설정

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
