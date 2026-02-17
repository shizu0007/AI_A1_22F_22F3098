import pygame
import random
from collections import deque
import heapq

pygame.init()

WIDTH = 600
ROWS = 20
CELL = WIDTH // ROWS

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("GOOD  PERFORMANCE  TIME APP")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
GREY = (200,200,200)

class Node:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.color = WHITE
        self.parent = None
        self.cost = float("inf")

    def draw(self):
        pygame.draw.rect(WIN,self.color,(self.col*CELL,self.row*CELL,CELL,CELL))

def make_grid():
    return [[Node(i,j) for j in range(ROWS)] for i in range(ROWS)]

def draw_grid():
    for i in range(ROWS):
        pygame.draw.line(WIN,GREY,(0,i*CELL),(WIDTH,i*CELL))
        pygame.draw.line(WIN,GREY,(i*CELL,0),(i*CELL,WIDTH))

def draw(grid):
    WIN.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw()
    draw_grid()
    pygame.display.update()

def get_neighbors(node,grid):
    moves=[(-1,0),(0,1),(1,0),(1,1),(0,-1),(-1,-1),(-1,1),(1,-1)]
    neighbors=[]
    for m in moves:
        r=node.row+m[0]
        c=node.col+m[1]
        if 0<=r<ROWS and 0<=c<ROWS:
            if grid[r][c].color!=BLACK:
                neighbors.append(grid[r][c])
    return neighbors

def show_path(end):
    current=end
    while current.parent:
        current=current.parent
        if current.color!=GREEN:
            current.color=PURPLE

def dynamic_obstacle(grid):
    if random.random()<0.02:
        r=random.randint(0,ROWS-1)
        c=random.randint(0,ROWS-1)
        if grid[r][c].color==WHITE:
            grid[r][c].color=BLACK

# BFS
def bfs(grid,start,end):
    queue=deque([start])
    visited=set([start])

    while queue:
        pygame.time.delay(40)
        dynamic_obstacle(grid)

        current=queue.popleft()

        if current==end:
            show_path(end)
            return

        for n in get_neighbors(current,grid):
            if n not in visited:
                visited.add(n)
                n.parent=current
                n.color=BLUE
                queue.append(n)

        current.color=YELLOW
        draw(grid)

# DFS
def dfs(grid,start,end):
    stack=[start]
    visited=set([start])

    while stack:
        pygame.time.delay(40)
        dynamic_obstacle(grid)

        current=stack.pop()

        if current==end:
            show_path(end)
            return

        for n in get_neighbors(current,grid):
            if n not in visited:
                visited.add(n)
                n.parent=current
                n.color=BLUE
                stack.append(n)

        current.color=YELLOW
        draw(grid)

# UCS
def ucs(grid,start,end):
    start.cost=0
    pq=[]
    count=0
    heapq.heappush(pq,(0,count,start))
    visited=set()

    while pq:
        pygame.time.delay(40)
        dynamic_obstacle(grid)

        cost,_,current=heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current==end:
            show_path(end)
            return

        for n in get_neighbors(current,grid):
            new_cost=cost+1
            if new_cost<n.cost:
                n.cost=new_cost
                n.parent=current
                count+=1
                heapq.heappush(pq,(new_cost,count,n))
                n.color=BLUE

        current.color=YELLOW
        draw(grid)

# DLS
def dls(grid,start,end,limit):
    stack=[(start,0)]
    visited=set()

    while stack:
        pygame.time.delay(40)
        dynamic_obstacle(grid)

        current,depth=stack.pop()

        if depth>limit:
            continue

        if current==end:
            show_path(end)
            return True

        visited.add(current)

        for n in get_neighbors(current,grid):
            if n not in visited:
                n.parent=current
                n.color=BLUE
                stack.append((n,depth+1))

        current.color=YELLOW
        draw(grid)
    return False

# IDDFS
def iddfs(grid,start,end):
    for limit in range(ROWS*ROWS):
        if dls(grid,start,end,limit):
            return

# Bidirectional
def bidirectional(grid,start,end):
    q1=deque([start])
    q2=deque([end])
    visited1={start}
    visited2={end}

    while q1 and q2:
        pygame.time.delay(40)

        current1=q1.popleft()
        current2=q2.popleft()

        for n in get_neighbors(current1,grid):
            if n not in visited1:
                visited1.add(n)
                n.parent=current1
                q1.append(n)
                n.color=BLUE
            if n in visited2:
                show_path(n)
                return

        for n in get_neighbors(current2,grid):
            if n not in visited2:
                visited2.add(n)
                q2.append(n)
                n.color=BLUE
            if n in visited1:
                show_path(n)
                return

        draw(grid)

def reset_nodes(grid):
    for row in grid:
        for node in row:
            node.parent=None
            node.cost=float("inf")
            if node.color not in (GREEN,RED,BLACK):
                node.color=WHITE

def main():
    grid=make_grid()
    start=grid[2][2]
    end=grid[15][15]
    start.color=GREEN
    end.color=RED

    running=True

    while running:
        draw(grid)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_r:
                    grid=make_grid()
                    start=grid[2][2]
                    end=grid[15][15]
                    start.color=GREEN
                    end.color=RED

                if event.key==pygame.K_b:
                    grid=make_grid()
                    start=grid[5][5]
                    end=grid[6][6]
                    start.color=GREEN
                    end.color=RED

                if event.key==pygame.K_w:
                    grid=make_grid()
                    start=grid[2][2]
                    end=grid[18][18]
                    start.color=GREEN
                    end.color=RED

                if event.key==pygame.K_1:
                    reset_nodes(grid)
                    bfs(grid,start,end)

                if event.key==pygame.K_2:
                    reset_nodes(grid)
                    dfs(grid,start,end)

                if event.key==pygame.K_3:
                    reset_nodes(grid)
                    ucs(grid,start,end)

                if event.key==pygame.K_4:
                    reset_nodes(grid)
                    dls(grid,start,end,10)

                if event.key==pygame.K_5:
                    reset_nodes(grid)
                    iddfs(grid,start,end)

                if event.key==pygame.K_6:
                    reset_nodes(grid)
                    bidirectional(grid,start,end)

    pygame.quit()
    # Minor update for visualization improvement


main()
# Updated dynamic obstacle behavior

