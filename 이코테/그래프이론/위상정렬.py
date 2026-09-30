###
# 위상정렬 알고리즘
# 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열'
# 진입차수 0인 노드 큐에 삽입 -> 큐가 빌때까지 (원소 꺼내 해당 노드에서 출발 간선 제거, 진입차수 0 된 노드 큐에 삽입)
# O(V+E)

from collections import deque

v, e = map(int, input().split())
indegree = [0]*(v+1) # 진입차수
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 진입차수 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]: # graph[now] = [후행 노드] (예시: graph[1] = [2, 3])
            indegree[i] -= 1 # 연결된 노드들 진입차수 - 1
            if indegree[i] == 0: # 새롭게 진입차수 0되는 노드 큐에 삽입
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()