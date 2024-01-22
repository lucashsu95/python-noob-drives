# Q5 矩陣轉換
def rotateLeft(ary):
    A = list(map(lambda x: x[::-1], ary))
    return list(map(list, (zip(*A))))

def turnOver(a):
    return a[::-1]

while 1:
    try:
        r, c, m = map(int, input().split())
        ary = [input().split() for _ in range(r)]
        options = input().split()

        for op in options[::-1]:
            if op == '0':
                ary = rotateLeft(ary)
            elif op == '1':
                ary = turnOver(ary)

        print(f'{len(ary)} {len(ary[0])}')
        for i in ary:
            print(' '.join(i))
    except:
        break