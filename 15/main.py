def main():
    grid = [[[0, 0] for _ in range(21)] for _ in range(21)]

    x = 20
    y = 20

    grid[y][x][0] = 1

    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        queue.extend(progress(grid, x, y))

    print(grid[0][0][0])

def progress(grid, x, y) -> list[tuple[int, int]]:
    if x == 0 and y == 0:
        return []

    next = []

    if x > 0:
        x2 = x - 1
        grid[y][x2][0] += grid[y][x][0]
        grid[y][x2][1] += 1

        if y == len(grid) - 1 or grid[y][x2][1] == 2:
            next.append((x2, y))

    if y > 0:
        y2 = y - 1
        grid[y2][x][0] += grid[y][x][0]
        grid[y2][x][1] += 1

        if x == len(grid[0]) - 1 or grid[y2][x][1] == 2:
            next.append((x, y2))

    return next

if __name__ == '__main__':
    main()
