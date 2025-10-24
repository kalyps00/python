def ok(g, r, c, n):
    if any(g[r][j] == n for j in range(9)):
        return False
    if any(g[i][c] == n for i in range(9)):
        return False
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if g[i][j] == n:
                return False
    return True


def solve(g):
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                for n in range(1, 10):
                    if ok(g, i, j, n):
                        g[i][j] = n
                        for sol in solve(g):
                            yield sol
                        g[i][j] = 0
                return
    yield [row[:] for row in g]


def pretty(g):
    for r in g:
        print(" ".join(str(x) for x in r))
    print()


if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Plansza początkowa:")
    pretty(board)

    print("Rozwiązanie:")
    for solution in solve(board):
        pretty(solution)
        break
