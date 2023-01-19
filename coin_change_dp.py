import sys
import argparse
import datetime


def min_coin_bottom_up_dp(total, coins):
    T = [sys.maxsize - 1 for x in range(total + 1)]
    S = [-1 for x in range(total + 1)]

    T[0] = 0

    for j in range(len(coins)):
        for i in range(1, total + 1):
            if i >= coins[j]:
                if T[i - coins[j]] + 1 < T[i]:
                    T[i] = 1 + T[i - coins[j]]
                    S[i] = j
    return print_coin_selected(S, coins)


def print_coin_selected(S, coins):
    res = []
    if S[len(S) - 1] == -1:
        print("No solution possible")
        return

    start = len(S) - 1
    print("Coins used ")
    while start != 0:
        j = S[start]
        res.append(coins[j])
        print(coins[j],' ')
        start = start - coins[j]
    return res


def find_minimum_coins_dp(c, k, n):
    return min_coin_bottom_up_dp(n,c)


def write_op(coin_count, time_req):
    f = open("output.txt", "a")
    f.writelines('\nCoin Used: ')
    f.writelines(str(coin_count))
    f.writelines('\nTime taken: ')
    f.writelines(str(time_req))
    f.writelines('\nAlgo used: ')
    f.writelines("dp")
    f.writelines('\n')


def run_dp_change_coin(d,k,n):
    start_time = datetime.datetime.now()
    coin_count = find_minimum_coins_dp(d, len(d), n)
    end_time = datetime.datetime.now()
    total_time_taken = (end_time - start_time)
    total_time_taken_ns = (int(total_time_taken.total_seconds() * 1000000))
    write_op(coin_count, total_time_taken_ns)


if __name__ == "__main__":
    n = input('Enter n (total change in cents): ')
    n = int(n)
    k = input('Enter number of denominations k: ')
    k = int(k)
    c = input('Enter denomination array d of size k (i.e. 1,2,3) : ')
    arr = c.split(',')
    d = [int(numeric_string) for numeric_string in arr]
    run_dp_change_coin(d,k,n)
