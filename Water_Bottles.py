# There are numBottles water bottles that are initially full of water.
# You can exchange numExchange empty water bottles from the market with one full water bottle.
#
# The operation of drinking a full water bottle turns it into an empty bottle.
#
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            full_bottles += empty_bottles // numExchange
            empty_bottles = empty_bottles // numExchange + empty_bottles % numExchange
        return full_bottles