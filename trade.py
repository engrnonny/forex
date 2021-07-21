
"""
1. Get the lot size, based on the amount willing to risk.


"""

# Calculating Lot size

"""
equity = input('Enter Equity:')

risk = (equity / 100) * 2

"""

equity = float(input('Enter Equity:'))

percentage = float(input('Enter Percentage of Equity willing to risk:'))

risk = (equity / 100) * percentage

lot_size = float(input('Enter Lot Size:'))

pip_value = lot_size * 10

sl_pips = risk / pip_value

print ("Risk = "+ str(risk))

print ("Stop Loss = "+ str(sl_pips))