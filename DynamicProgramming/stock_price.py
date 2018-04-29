# Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# For example:

#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# # Returns 6 (buying for $5 and selling for $11)

# No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).




def get_max_profit(stock_prices):

    # Calculate the max profit
    # when I am at an index, i try to find next max and store the difference
    # import math 
    
    # Method-1 O(n^2)
    # max_p = -999999999999999
    
    # if len(stock_prices) < 2:
    #     raise Exception("Too few stock prices")
        
    # for i in range(len(stock_prices)):
    #     for j in range(i+1, len(stock_prices)):
    #         diff = stock_prices[j] - stock_prices[i]
    #         if  diff > max_p:
    #             max_p = diff
                
    # return max_p
    
    # Method-2 : Greedy
    if len(stock_prices) < 2:
        raise Exception("Too few stock prices")
        
    max_profit = stock_prices[1] - stock_prices[0]
    lowest = stock_prices[0]
    
    for i in range(1,len(stock_prices)):
        if stock_prices[i] - lowest > max_profit:
            max_profit = stock_prices[i] - lowest
        if stock_prices[i] < lowest :
            lowest = stock_prices[i]
            
    return max_profit




# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)