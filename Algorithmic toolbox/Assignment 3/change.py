def change(money):
    # write your code here
    count = 0
    coin = [1,5,10]
    while money >0:
        maxcoin = max(x for x in coin if x <= money) 
        money -= maxcoin
        count +=1
    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
