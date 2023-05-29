# Shinwon Lee Final group project
# [referenced link]
# https://github.com/ndb796/python-for-coding-test/blob/master/5/11.py
# https://wikidocs.net/26

from collections import deque

#read a maze file
f = open("mazes/maze_31x31.txt",'r')
arr = []

while True:
    line = f.readline()
    if not line: break
    arr.append(list(line.strip())) #string to list
f.close()

# list to memorize visited information (2 dimensions)
visited = [[False]*len(arr[0]) for _ in range(len(arr))]

# find the location of 'S'
for i in range(len(arr)):
    if 'S' in arr[i]:
        sx,sy = i,arr[i].index('S')
        break

# define 4 ways to move (up, down, left, right)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# bfs - the algorithm that I choose to solve the maze
def bfs(x,y):
    # deque library used for implementing queue
    queue = deque()
    queue.append((x,y))

    while queue: # until queue is empty
        x,y = queue.popleft()

        for i in range(4): # check the location in 4 directions from the current location
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=len(arr) or ny >= len(arr[0]): #outsize of maze
                continue
            if arr[nx][ny] == 'X': # walls
                continue
            if not visited[nx][ny]: # record shortest path only on first visit
                if arr[nx][ny] == 'G': # if 'G', return the shortest path
                    return arr[x][y]
                else: 
                    arr[nx][ny] = str(int(arr[x][y]) + int(arr[nx][ny])) if arr[x][y] != 'S' else arr[nx][ny] 
                    queue.append((nx,ny))
        
        visited[x][y] = True


print(bfs(sx,sy))     
