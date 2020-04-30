# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    list_len = max(money+1, 5)
    output = [0]*(list_len)
    output[1] = 1
    output[2] = 2
    output[3] = 1
    output[4] = 1
    for i in range(5,money+1):
        add_1 = output[i-1] + 1
        add_3 = output[i-3] + 1
        add_4 = output[i-4] + 1
        output[i] = min(add_1, add_3, add_4)

    
    return  output[money]
        



if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
