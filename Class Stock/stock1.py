import csv
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

#    def __init__(self,name,shares,price):
#        self.myname
#        self.myshares
#        self.myprice

#    def __str__(self):
#        return "name: " + self.myname +"\nshares: " + str(self.myshares) +"\nprice: " + str(self.myprice)

#    def get_myname(self):
#        return self.myname
#    def get_myshares(self):
#        return self.myshares
#    def get_myprice(self):
#        return self.price