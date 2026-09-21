n,m = map(int, input().split())
d = [[0]*m for _ in range(n)] # 방문 위치 저장할 맵

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북,동,남,서 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    # 미래좌표 계산
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가본적 없고 육지라면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        # 미래좌표 갱신
        x=nx
        y=ny
        count+=1
        turn_time=0 # 방문 성공하면 회전횟수 초기화
        continue
    else:
        turn_time+=1

    # 네 방향 모두 막혔을때
    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]

        # 육지라면 후진
        if array[nx][ny] == 0:
            x=nx
            y=ny
        else:
            break
        turn_time = 0

print(count)