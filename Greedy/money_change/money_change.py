
def money_change(money):
    assert 0 <= money <= 10 ** 3
    

    tally = 0 
    if (money % 10) != money:
        tens = money // 10 
        money = money - tens*10 
        tally += tens

    if (money % 5) != money:
        fives = money // 5 
        money = money - fives*5
        tally += fives
    
    tally += money

    return tally 


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
