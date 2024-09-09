import argparse
import logging

import json_handler as jh

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Initializing main.py")
parser = argparse.ArgumentParser(description="To Do List CLI written in Python.")

parser.add_argument('-a', '--add', help="Add an item to the list.", metavar="Item")
parser.add_argument('-l', '--list', help="List out all items on the list.", action="store_true")

args = parser.parse_args()
logging.debug(f"Arguments passed are %% \"{args}\"")

if args.add:
	logging.debug("'--add' argument found.")
	added_item_id = jh.add_item(args.add)
	print(f" %%% Item added successfully. (ID: {added_item_id})")

if args.list:
	logging.debug("'--list' argument found")
	jh.list_items()
