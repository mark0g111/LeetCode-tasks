# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set,
# if it is not already in the infinite set.

class SmallestInfiniteSet:

    def __init__(self):
        self.values = [i for i in range(1, 1001)]

    def popSmallest(self) -> int:
        el = self.values.pop(0)
        return el

    def addBack(self, num: int) -> None:
        if num not in self.values:
            for i in range(len(self.values)):
                if self.values[i] > num:
                    self.values.insert(i, num)
                    break

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
