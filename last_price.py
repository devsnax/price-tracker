import csv
import config

def load_last_price():
    try:
        with open(config.FILE, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                return None
            return float(rows[-1]["new price"])
    except FileNotFoundError:
        return None