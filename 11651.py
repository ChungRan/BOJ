def solution():
    N = int(input())
    table = list()
    for x in range(N):
        x, y = map(int,input().split())
        table.append({
            'x' : x,
            'y' : y
        })
    table.sort(key = lambda get : (get['y'], get['x']))

    for i in table:
        print(i['x'], i['y'])

solution()