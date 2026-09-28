###
# 다익스트라 알고리즘 (우선순위큐)
# 한도시 -> 다른도시 최단거리

import heapq
import sys

input = sys.std.readline()
INF = int(1e9)

n,m,start = map(int, input().split()) # 도시n, 통로m, 메시지 보내는c
graph =[[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int, input().split()) #x->y 통로, 시간z
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start)) #시작노드 최단경로는 0으로 설정
    distance[start] = 0
    while q: #q가 비지 않을 동안
        dist, now = heapq.heappop(q) # 최단거리 가장 짧은 노드 정보 꺼내기
        if distance[now] < dist:
            continue
        for i in graph[now]: # 인접 노드 확인  i: (인접노드, 가중치) -> i[0]: 인접노드, i[1]: 가중치
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재노드 거쳐 다른노드로 이동하는 거리 더 짧으면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 최단거리 업데이트 후 큐에 넣기

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance) # 시작노드 제외!!