from datetime import datetime
import os
import csv

import config

def save_price(old_price, new_price, change):
    file_exists = os.path.exists(config.FILE)
    fieldnames = [
    "old price",
    "old time",
    "new price",
    "new time",
    "% Change"
]

    with open(config.FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "old price": old_price,
            "old time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "new price": new_price,
            "new time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "% Change": change
        })