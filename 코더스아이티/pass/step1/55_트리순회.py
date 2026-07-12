from collections import deque

class Node:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.left = None
        self.right = None
        self.low = -1
        self.high = -1
    
    def __lt__(self, other):
        if self.y != other.y:
            return self.y > other.y
        return self.x < other.x

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append(Node(x, y, i + 1))

arr.sort()
level = []
level = [[arr[0]]]

for i in range(1, n):
    if arr[i -1].y != arr[i].y:
        level.append([])
    level[-1].append(arr[i])

arr[0].low = 0
arr[0].high = 1000

q = deque([arr[0]])


for i in range(1, len(level)):
    for v in level[i]: # 자식 레벨 순회 중, 부모 찾아주기
        while True:
            if q[0].low <= v.x <= q[0].x: # 부모 찾음, 부모의 왼쪽 자식
                q[0].left = v
                v.low = q[0].low
                v.high = q[0].x
                break
            if q[0].x <= v.x <= q[0].high:
                q[0].right = v
                v.low = q[0].x
                v.high = q[0].high
                break
            q.popleft()
    q = deque(level[i]) # 다음 부모 큐

def preOrder(node):
    if node is None:
        return
    print(node.v, end = ' ')
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.v, end = ' ')

preOrder(arr[0])
print()
postOrder(arr[0])