def compare_prices(old, new):
    percentage = ((old - new) / old) * 100
    return round(percentage, 2)