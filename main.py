import argparse
import coin_change_greedy as greedy
import recursion as rec
import coin_change_dp as dp




# Parser to take the system argument
parser = argparse.ArgumentParser(description="This program is to get the minimum coin required")

parser.add_argument("change_req", help="total change in cents")
parser.add_argument("no_of_denomination", help="number of denomination")
parser.add_argument("denomination", help="Enter denomination comma serprated ex- 1,2,3")
args = parser.parse_args()

if __name__ == "__main__":
    denomination = args.denomination
    denomination = denomination.split(',')
    k = args.no_of_denomination
    denomination = [int(i) for i in denomination]
    greedy.run_greedy_change_coin(denomination,k, int(args.change_req))
    rec.run_recursion_change_coin(denomination, int(k),int(args.change_req))
    dp.run_dp_change_coin(denomination, int(k), int(args.change_req))