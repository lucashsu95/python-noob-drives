import sys
# 題目 3：搜尋(Search)問題 (10%)
node_count = int(input())
root = input().strip()
tree = [line.strip().split(', ') for line in sys.stdin]
paths = ''

def dfs(n):
    global paths
    paths += n
    for u,v in tree:
        if v == n:
            dfs(u)

dfs(root)
print(', '.join(paths))