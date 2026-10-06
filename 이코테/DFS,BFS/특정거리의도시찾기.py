# N번 도시, M개 단방향 도로 
# 도시X 부터 출발해서 도달할 수 있는 모든 도시 중 최단거리가 K인 모든 도시의 번호를 출력하는 프로그램
from collections import deque

n,m,k,x = map(int, input().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)


check = False

for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
