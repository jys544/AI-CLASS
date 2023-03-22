# pcost.py

import csv
from stock import Stock

def portfolio_cost(filename):
    for s in filename:
        portfolio_cost += s['shares'] * s['price']
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    
def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
