import time
import datetime
import sys


def recursion_change_coin(arr_coins, k, n):
 
    # if total change is 0
    if (n == 0):
        return 0
 
    # Initializing number of minimum coins to max size of int 
    minimum_coins = sys.maxsize
     
    # Loop trying each coin that has less value than n
    for i in range(0, k):
        if (arr_coins[i] <= n):
            sub_minimum_coins = recursion_change_coin(arr_coins, k, n-arr_coins[i])
 
            # Checking for integer max value  to avoid overflow and if it is true then checking
            # if minimum coins can minimized
            if (sub_minimum_coins != sys.maxsize and sub_minimum_coins + 1 < minimum_coins):
                minimum_coins = sub_minimum_coins + 1
 
    return minimum_coins


def run_recursion_change_coin(d, k, n):
    start_time_recursion_change_coin = datetime.datetime.now()
    coin_count = recursion_change_coin(d, k, n)
    end_time_recursion_change_coin = datetime.datetime.now()
    ttl_time_recursion_change_coin = (end_time_recursion_change_coin - start_time_recursion_change_coin)
    ttl_time_recursion_change_coin = (int(ttl_time_recursion_change_coin.total_seconds()*1000000))
    f = open("output.txt", "a")
    f.writelines('\nMinimum coin-count: ')
    f.writelines(str(coin_count))
    f.writelines('\nTime taken: ')
    f.writelines(str(ttl_time_recursion_change_coin))
    f.writelines('\nAlgo used: ')
    f.writelines("recursion")
    f.writelines('\n')

if __name__ == "__main__":
    sys.setrecursionlimit(1500000000)
    n = input('Enter n (total change in cents): ')
    n = int(n)
    k = input('Enter number of denominations k: ')
    k = int(k)
    c = input('Enter denomination array d of size k (i.e. 1,2,3) : ')
    arr = c.split(',')
    d = [int(numeric_string) for numeric_string in arr]
    print(n)
    print("\n")
    print(k)
    print("\n")
    print(d)
    run_recursion_change_coin(d, k, n)
 

