def change(money):
    # write your code here
    coins = [1,3,4]
    
    min_coin = [float("inf")]*(money+1)
    min_coin [0] = 0
    
    for m in range(1,money+1):
        for coin in coins:
            if m >= coin:
                if min_coin[m-coin] + 1 < min_coin[m]:
                    min_coin [m] = min_coin[m-coin]+1
    
    return min_coin[money]



if __name__ == '__main__':
    m = int(input())
    print(change(m))
