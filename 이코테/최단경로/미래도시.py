###
# 플로이드 워셜 알고리즘
# "a에서 b로 바로 가는 기존 거리"와 "k번 노드를 거쳐서 가는 거리"를 비교해서 더 짧은 거리로 갱신

INF = int(1e9)

n,m = map(int, input().split())
# 1부터 n까지 사용하므로 n+1 x n+1 그래프 만들기
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자신 -> 자신 비용 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 양방향 그래프, 가중치는 1

x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1번 노드 -> k번 노드를 거쳐 -> x번 노드까지 가는 총 거리
distance = graph[1][k] + graph[k][x] 

if distance >= INF:
    print("-1")
else:
    print(distance) 