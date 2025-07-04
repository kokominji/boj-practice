import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = {}

for i in range(n):
    root, left, right = map(str, input().split())
    tree[root] = left, right
    
def preorder(v):
    if v != ".":
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])
        
def inorder(v):
    if v != ".":
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])
        
def postorder(v):
    if v != ".":
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")
        
preorder("A")
print("")
inorder("A")
print("")
postorder("A")