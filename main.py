import schedule
import time

from fetcher import fetch_price
from last_price import load_last_price
from compare import compare_prices
from save_price import save_price

def main():
    old_price = load_last_price()
    new_price = fetch_price()
    
    if old_price is None:
        print("First run. saving initial price.")
        save_price(new_price, new_price, 0)
        return
    
    percent_change = compare_prices(old_price, new_price)
    save_price(old_price, new_price, percent_change)
    print("Updated price_changes.csv")

if __name__ == '__main__':
    schedule.every(8).seconds.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1.5)