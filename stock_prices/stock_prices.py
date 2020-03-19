#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(0, len(prices)):
    if prices[i] == max(prices):
      max_num = prices[i]
    if prices[i] == min(prices[:prices.index(max(prices))]):
      min_num = prices[i]    
  # print(max_num-min_num)
  profit = max_num-min_num
  print(f"A profit of ${profit} can be made from the stock prices {prices}.")

find_max_profit([1050, 270, 1540, 3800, 2])  

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))