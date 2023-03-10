import os
from dotenv import load_dotenv
import pandas as pd


def get_timestamp(date, time):
    date = date + " " + time
    date = pd.to_datetime(date)
    date = date.timestamp()
    date = date * 1000
    return int(date)


load_dotenv()


def get_curr_day():
    try:
        curr_day = os.getenv("curr_day")
        return curr_day
    except:
        print("curr_day not found in .env file")


def get_prev_day():
    try:
        prev_day = os.getenv("prev_day")
        return prev_day
    except:
        print("prev_day not found in .env file")
