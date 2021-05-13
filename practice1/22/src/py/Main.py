from Utils import maze,calculate

xy = list(map(int, input('Введите x y игрока: ').split(' ')))

if len(xy) != 2:
    print("Не верные координаты")
    exit(-1)

x = xy[0]
y = xy[1]

if not 0 <= x <= len(maze[0]) or not 0 <= y <= len(maze):
    print("Не верные координаты")
    exit(-1)
if maze[y][x] == '#':
    print("Не верные координаты")
    exit(-1)

result = calculate(maze, x, y)

output = []
for i in result:
    output.append(maze[i.y][i.x])
print(*output)
