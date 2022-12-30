""" ENCAPSULATION """


class Grocery:

    def __init__(self, maxi_price=800):
        self.__maxiprice = maxi_price

    @property
    def max_price(self):
        return self.__maxiprice

    @max_price.setter
    def max_price(self, maxiprice):
        self.__maxiprice = maxiprice


c = Grocery()
# c.max_price()

# c.Grocery = 1000
# print(c.max_price())
print(c.max_price)

# change the price
c._Grocery__maxiprice = 1000
print(c.max_price)

# using setter function
c.max_price = 1000
print(c.max_price)
