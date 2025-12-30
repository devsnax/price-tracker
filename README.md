# Bitcoin Price Tracker

## Overview
This project automatically fetches Bitcoin price data, processes it, tracks changes over time, and sends saves the data to a CSV file.

## How it works
- Fetches latest price data from the Coingecko API
- Compares new data with previously saved values
- Calculates changes
- Stores results in CSV
- Runs automatically using a scheduler

## Project Structure
- main.py – orchestrates the workflow
- fetcher.py – fetches latest data
- compare.py – computes changes
- save_price.py – persists results
- config.py – configuration values

## How to run
1. Clone the repo
2. Install dependencies
3. Run `python main.py`

## Why I built this
I wanted to build a real automation tool that runs continuously, handles state, and produces useful output.
