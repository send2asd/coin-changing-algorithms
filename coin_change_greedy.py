import datetime


def greedy_change_coin(c,k,n):
    deno = c
    i = k - 1
    res = []
    numCoins = 0
    while( i >= 0):
        if n/deno[i] >= 1:
            numCoins = numCoins + int(n/deno[i])
            op = [deno[i]]*int(n/deno[i])
            res.extend(op)
            n = n - (int(n/deno[i]) * deno[i])
        i = i - 1
    return res
 
def run_greedy_change_coin(d,k, n):
    start_time_recursion_change_coin = datetime.datetime.now()
    coin_count = greedy_change_coin(d,int(k),n)
    end_time_recursion_change_coin = datetime.datetime.now()
    ttl_time_recursion_change_coin = (end_time_recursion_change_coin - start_time_recursion_change_coin)
    ttl_time_recursion_change_coin = (int(ttl_time_recursion_change_coin.total_seconds()*1000000))
    f = open("output.txt", "a")
    f.writelines('\nCoin Used: ')
    f.writelines(str(coin_count))
    f.writelines('\nTime taken: ')
    f.writelines(str(ttl_time_recursion_change_coin))
    f.writelines('\nAlgo used: ')
    f.writelines("greedy")
    f.writelines('\n')



if __name__ == "__main__":
    n = input('Enter n (total change in cents): ')
    n = int(n)
    k = input('Enter number of denominations k: ')
    k = int(k)
    c = input('Enter denomination array d of size k (i.e. 1,2,3) : ')
    arr = c.split(',')
    d = [int(numeric_string) for numeric_string in arr]
    run_greedy_change_coin(d,k,n)
 