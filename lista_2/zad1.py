def dhondt(votes_list: list[tuple[str, int]], space):
    votes_sum = sum(i for _, i in votes_list)

    ilorazy = []
    for name, num in votes_list:
        if num < votes_sum * 0.05:
            continue
        for i in range(1, space + 1):
            ilorazy.append((num // i, num, name))
    ilorazy.sort(reverse=True)
    mandaty = {name: 0 for name, _ in votes_list}
    for i in range(space):
        na = ilorazy[i][2]
        mandaty[na] += 1
    return mandaty


if __name__ == "__main__":
    print(dhondt([("A", 720), ("B", 300), ("C", 480)], 8))
