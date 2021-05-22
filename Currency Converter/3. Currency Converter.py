import json
import requests

dt = {}

def get_cur(curr):
    if cur_inhand == curr:
        dt[curr] = 1
    else:
        url = f"http://www.floatrates.com/daily/{cur_inhand.lower()}.json"
        r = requests.get(url)
        curr_json = r.text
        curr_dict = json.loads(curr_json)
        rate = curr_dict[curr.lower()]["rate"]
        dt[curr] = rate

# get_cur("usd")
# get_cur("eur")

while True:
    cur_inhand = input("Please enter currency you have: ")
    new_cur = input("Please enter currency you want: ")
    amount = float(input("Please enter the amount: "))
    if new_cur in dt.keys():
        print("Checking the cache...\nOh! It is in the cache!")
        print(f"You received {(dt[new_cur] * amount):.2f} {new_cur.upper()}.")
    elif new_cur not in dt.keys():
        print("Checking the cache...\nSorry, but it is not in the cache!")
        get_cur(new_cur)
        print(f"You received {(dt[new_cur] * amount):.2f} {new_cur.upper()}.")
