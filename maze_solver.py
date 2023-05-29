#Shinwon Lee Final group project
from collections import deque

f = open("mazes/maze_31x31.txt",'r')
arr = []

while True:
    line = f.readline()
    if not line: break
    arr.append(list(line.strip()))
f.close()

visited = [[False]*len(arr[0]) for _ in range(len(arr))]

for i in range(len(arr)):
    if 'S' in arr[i]:
        sx,sy = i,arr[i].index('S')
        break
print(sx,sy)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=len(arr) or ny >= len(arr[0]):
                continue
            if arr[nx][ny] == 'X':
                continue
            if not visited[nx][ny]:
                if arr[nx][ny] == 'G':
                    return arr[x][y]
                else:
                    arr[nx][ny] = str(int(arr[x][y]) + int(arr[nx][ny])) if arr[x][y] != 'S' else arr[nx][ny]
                    queue.append((nx,ny))
        
        visited[x][y] = True


print(bfs(sx,sy))     

    
