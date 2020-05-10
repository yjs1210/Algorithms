# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    dp_grid = [[0]*(capacity+1) for y in range(len(weights)+1)]

    for idx in range(1, len(weights)+1):
        for j in range(1, capacity + 1):
            wt = weights[idx-1]
            if j - wt >= 0:
                dp_grid[idx][j] = max(dp_grid[idx-1][j], dp_grid[idx-1][j - wt] + wt)
            else:
                dp_grid[idx][j] = dp_grid[idx-1][j]

    return dp_grid[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
