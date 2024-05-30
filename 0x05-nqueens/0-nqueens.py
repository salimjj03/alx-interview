#!/usr/bin/python3


from sys import argv


def backtrack(s, ls, step, ss):
    if step == 0:
        if s in ls or ss in ls:
            return True
        return False

    if s in ls or ss in ls:
        return True
    return backtrack(
            [s[0] - 1, s[1] - 1],
            ls, step - 1, [ss[0] - 1, ss[1] + 1]
            )


def queen_position():
    if len(argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    ls = []
    h = 0
    for a in range(int(argv[1])):
        n = range(int(argv[1]))
        queen = []
        position = []
        for i in n:
            for j in n[a:]:
                a = 0
                if j not in queen and backtrack(
                        [i, j],
                        position,
                        i,
                        [i, j]
                        ) is False:

                    queen.append(j)
                    position.append([i, j])
                    break
        if len(position) > h:
            ls = []
            ls.append(position)
            h = len(position)
        elif len(position) == h:
            ls.append(position)
            h = len(position)

    for i in ls:
        print(i)


if __name__ == "__main__":
    queen_position()
