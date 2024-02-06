# 賣鴨子

n,num = map(int,input().split())

def fs_duck(n,num):

    total = (num + 1) * 2
    duck = total - num
    if n > 1:
        fs_duck(n-1,total)
    else:
        print(f'出發時共 {total} 隻 ')

    print(f'經過第 {n} 個村莊 賣 {duck} 隻,剩 {num} 隻鴨')
    
fs_duck(n,num)
