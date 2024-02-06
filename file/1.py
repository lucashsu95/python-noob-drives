# 賣鴨子

n,num = map(int,input().split())

for i in range(n):
    num = (num + 1) * 2
    sell = num // 2 + 1
    print(f'經過第 {n - i} 個村莊 賣 {sell} 隻,剩 {num - sell} 隻鴨')
print(f'出發時共 {num} 隻')