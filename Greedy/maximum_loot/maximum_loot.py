# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    values = [0]*len(weights)
    for i in range(len(weights)):
        values[i] = prices[i] / weights[i]

    zipped = zip(values, prices, weights)
    zipped = sorted(zipped, key = lambda t: -t[0])
    
    
    curr_weight = 0
    total_value = 0
    for _, price, weight in zipped:
        remaining = capacity - curr_weight
        if (remaining > weight):
            curr_weight += weight
            total_value += price
        else:
            total_value = total_value + (capacity - curr_weight)*price/weight
            curr_weight = capacity
        
    return total_value
        
        

    


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
